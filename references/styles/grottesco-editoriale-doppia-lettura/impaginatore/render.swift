import Foundation
import CoreText
import CoreGraphics
import ImageIO

typealias Object = [String: Any]
enum RenderError: Error { case invalid(String) }
func fail(_ message: String) throws -> Never { throw RenderError.invalid(message) }
func number(_ object: Object, _ key: String) -> CGFloat { (object[key] as! NSNumber).doubleValue }
func xml(_ value: String) -> String {
    value.replacingOccurrences(of: "&", with: "&amp;").replacingOccurrences(of: "<", with: "&lt;")
        .replacingOccurrences(of: ">", with: "&gt;").replacingOccurrences(of: "\"", with: "&quot;")
}
func f(_ value: CGFloat) -> String { String(format: "%.4f", Double(value)) }
func color(_ hex: String) -> CGColor {
    let value = UInt32(hex.dropFirst(), radix: 16)!
    return CGColor(srgbRed: CGFloat((value >> 16) & 255) / 255,
                   green: CGFloat((value >> 8) & 255) / 255,
                   blue: CGFloat(value & 255) / 255, alpha: 1)
}
func axisTag(_ text: String) -> NSNumber { NSNumber(value: text.utf8.reduce(UInt32(0)) { ($0 << 8) | UInt32($1) }) }

struct FontFile {
    let spec: Object
    let graphicsFont: CGFont
    init(_ spec: Object) throws {
        self.spec = spec
        let url = URL(fileURLWithPath: spec["absolute_file"] as! String)
        guard let provider = CGDataProvider(url: url as CFURL), let font = CGFont(provider) else {
            try fail("Impossibile caricare il file font: \(url.path)")
        }
        graphicsFont = font
    }
    func at(_ size: CGFloat) -> CTFont {
        var axes: [NSNumber: NSNumber] = [:]
        for (key, value) in spec["axes"] as! Object { axes[axisTag(key)] = value as? NSNumber }
        let descriptor = CTFontDescriptorCreateWithAttributes([kCTFontVariationAttribute as String: axes] as CFDictionary)
        return CTFontCreateWithGraphicsFont(graphicsFont, size, nil, descriptor)
    }
    func details() throws -> Object {
        let font = at(100)
        let family = CTFontCopyFamilyName(font) as String
        guard family == spec["family"] as! String else { try fail("Famiglia font inattesa: \(family)") }
        let variation = CTFontCopyVariation(font) as? [NSNumber: NSNumber] ?? [:]
        let definitions = CTFontCopyVariationAxes(font) as? [Object] ?? []
        var effective: Object = [:]
        for (key, value) in spec["axes"] as! Object {
            let identifier = axisTag(key)
            let axis = definitions.first { ($0[kCTFontVariationAxisIdentifierKey as String] as? NSNumber) == identifier }
            let actual = variation[identifier] ?? axis?[kCTFontVariationAxisDefaultValueKey as String] as? NSNumber
            guard let actual, abs(actual.doubleValue - (value as! NSNumber).doubleValue) < 0.001 else {
                try fail("Asse \(key) del font \(family) non applicato.")
            }
            effective[key] = actual
        }
        return ["family": family, "postscript_name": CTFontCopyPostScriptName(font) as String,
                "version": CTFontCopyName(font, kCTFontVersionNameKey) as String? ?? "",
                "effective_axes": effective, "sha256": spec["sha256"]!, "file_loaded": spec["local_file"]!]
    }
}

func line(_ text: String, font: CTFont, tracking: CGFloat, hex: String) -> CTLine {
    let attributes: [NSAttributedString.Key: Any] = [
        NSAttributedString.Key(kCTFontAttributeName as String): font,
        NSAttributedString.Key(kCTKernAttributeName as String): tracking * CTFontGetSize(font),
        NSAttributedString.Key(kCTForegroundColorAttributeName as String): color(hex)
    ]
    return CTLineCreateWithAttributedString(NSAttributedString(string: text, attributes: attributes))
}

struct PlacedLine {
    let text: String
    let shaped: CTLine
    let origin: CGPoint
    let topBounds: CGRect
    let hex: String
    let family: String
    let size: CGFloat
    let section: String
}
struct Rule { let x1: CGFloat; let x2: CGFloat; let y: CGFloat; let thickness: CGFloat; let hex: String }

let jobURL = URL(fileURLWithPath: CommandLine.arguments[1])
let output = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)
let job = try JSONSerialization.jsonObject(with: Data(contentsOf: jobURL)) as! Object
let card = job["card"] as! Object
let renderer = job["renderer"] as! Object
let layout = card["layout"] as! Object
let details = job["layout_details"] as! Object
let palette = card["palette"] as! [String: String]
let outputs = job["outputs"] as! [String: String]
let dimensions = renderer["output_size_px"] as! [Int]
let W = CGFloat(dimensions[0]), H = CGFloat(dimensions[1])
let primary = try FontFile((job["fonts"] as! Object)["primary"] as! Object)
let secondary = try FontFile((job["fonts"] as! Object)["secondary"] as! Object)
let primaryDetails = try primary.details(), secondaryDetails = try secondary.details()
let margin = number(layout, "margin_x_W") * W
let gutter = number(layout, "gutter_W") * W
let column = (W - 2 * margin - 3 * gutter) / 4
let fit = renderer["fit"] as! Object
let safety = number(fit, "horizontal_safety_px")
var placed: [PlacedLine] = []
var metrics: [Object] = []
var rules: [Rule] = []

func fittedSize(_ lines: [String], _ file: FontFile, _ requested: CGFloat, _ tracking: CGFloat, _ width: CGFloat) -> CGFloat {
    func maximum(_ size: CGFloat) -> CGFloat {
        lines.map { CTLineGetImageBounds(line($0, font: file.at(size), tracking: tracking, hex: "#000000"), nil).width }.max() ?? 0
    }
    if maximum(requested) <= width - safety { return requested }
    var low: CGFloat = 1, high = requested
    for _ in 0..<35 {
        let middle = (low + high) / 2
        if maximum(middle) <= width - safety { low = middle } else { high = middle }
    }
    return low
}

@discardableResult
func place(_ lines: [String], file: FontFile, requested: CGFloat, size: CGFloat, tracking: CGFloat,
           leading: CGFloat, left: CGFloat, top: CGFloat, hex: String, section: String) throws -> CGRect {
    let font = file.at(size)
    let shaped = lines.map { line($0, font: font, tracking: tracking, hex: hex) }
    let firstBounds = CTLineGetImageBounds(shaped[0], nil)
    let firstBaseline = H - top - firstBounds.maxY
    var union = CGRect.null
    var previous: CGRect?
    for (index, item) in shaped.enumerated() {
        let bounds = CTLineGetImageBounds(item, nil)
        let baseline = firstBaseline - CGFloat(index) * size * leading
        let origin = CGPoint(x: left - bounds.minX, y: baseline)
        let pageBounds = bounds.offsetBy(dx: origin.x, dy: origin.y)
        let topBounds = CGRect(x: pageBounds.minX, y: H - pageBounds.maxY, width: pageBounds.width, height: pageBounds.height)
        guard topBounds.minX >= -0.01, topBounds.maxX <= W + 0.01,
              topBounds.minY >= 0, topBounds.maxY <= H else { try fail("Testo fuori tavola: \(lines[index])") }
        if let previous, topBounds.minY < previous.maxY - 0.01 { try fail("Collisione fra righe in \(section)") }
        for run in CTLineGetGlyphRuns(item) as! [CTRun] {
            let runAttributes = CTRunGetAttributes(run) as NSDictionary
            let runFont = runAttributes[kCTFontAttributeName as String] as! CTFont
            guard (CTFontCopyFamilyName(runFont) as String) == file.spec["family"] as! String else {
                try fail("Font sostitutivo rilevato in \(section)")
            }
            var glyphs = [CGGlyph](repeating: 0, count: CTRunGetGlyphCount(run))
            CTRunGetGlyphs(run, CFRange(location: 0, length: 0), &glyphs)
            guard !glyphs.contains(0) else { try fail("Glifo mancante in \(section)") }
        }
        placed.append(PlacedLine(text: lines[index], shaped: item, origin: origin, topBounds: topBounds,
                                 hex: hex, family: file.spec["family"] as! String, size: size, section: section))
        previous = topBounds
        union = union.union(topBounds)
    }
    metrics.append(["section": section, "requested_font_size_px": requested, "font_size_px": size,
                    "font_family": file.spec["family"]!, "line_count": lines.count,
                    "line_height_px": size * leading, "tracking_em": tracking,
                    "bounds_top_left_px": [union.minX, union.minY, union.width, union.height]])
    return union
}

let headers = (card["header"] as! [String]).map { $0.components(separatedBy: "\n") }
let footers = (card["footer"] as! [String]).map { $0.components(separatedBy: "\n") }
let microRequested = W * number(details, "micro_font_size_W")
let microSize = fittedSize((headers + footers).flatMap { $0 }, secondary, microRequested,
                           number(details, "micro_tracking_em"), column)
let ruleThickness = W * number(details, "rule_thickness_W")
for (index, texts) in headers.enumerated() {
    let bounds = try place(texts, file: secondary, requested: microRequested, size: microSize,
                          tracking: number(details, "micro_tracking_em"), leading: number(details, "micro_line_height_em"),
                          left: margin + CGFloat(index) * (column + gutter), top: H * number(layout, "header_y_H"),
                          hex: palette["secondary"]!, section: "header-\(index + 1)")
    guard bounds.maxY + 8 < H * number(layout, "header_rule_y_H") else { try fail("Header troppo alto") }
}
func addRules(_ spans: [[Int]], _ y: CGFloat) {
    for span in spans {
        let left = margin + CGFloat(span[0]) * (column + gutter)
        let width = CGFloat(span[1]) * column + CGFloat(span[1] - 1) * gutter
        rules.append(Rule(x1: left, x2: left + width, y: y, thickness: ruleThickness, hex: palette["rules"]!))
    }
}
addRules(details["header_rule_spans"] as! [[Int]], H * number(layout, "header_rule_y_H"))
addRules(details["footer_rule_spans"] as! [[Int]], H * number(layout, "footer_rule_y_H"))
let quoteLines = card["quote_lines"] as! [String]
let emphasisLines = card["emphasis_lines"] as! [String]
let tracking = number(card, "main_tracking_em")
let quoteRequested = W * number(layout, "quote_font_size_W")
let emphasisRequested = W * number(layout, "emphasis_font_size_W")
let quoteSize = fittedSize(quoteLines, primary, quoteRequested, tracking, W - 2 * margin)
let emphasisSize = fittedSize(emphasisLines, primary, emphasisRequested, tracking, W - 2 * margin)
let quoteBounds = try place(quoteLines, file: primary, requested: quoteRequested, size: quoteSize, tracking: tracking,
                            leading: number(layout, "quote_line_height_em"), left: margin,
                            top: H * number(layout, "quote_top_H"), hex: palette["quote"]!, section: "complete-quote")
let emphasisBounds = try place(emphasisLines, file: primary, requested: emphasisRequested, size: emphasisSize, tracking: tracking,
                               leading: number(layout, "emphasis_line_height_em"), left: margin,
                               top: H * number(layout, "emphasis_top_H"), hex: palette["emphasis"]!, section: "repeated-excerpt")
guard quoteBounds.maxY + 8 < emphasisBounds.minY else { try fail("Collisione fra frase ed estratto") }
guard emphasisBounds.maxY + 8 < H * number(layout, "footer_rule_y_H") else { try fail("Estratto troppo vicino al footer") }
let footerColumns = details["footer_text_columns"] as! [Int]
for (index, texts) in footers.enumerated() {
    _ = try place(texts, file: secondary, requested: microRequested, size: microSize,
                  tracking: number(details, "micro_tracking_em"), leading: number(details, "micro_line_height_em"),
                  left: margin + CGFloat(footerColumns[index]) * (column + gutter),
                  top: H * number(layout, "footer_text_top_H"), hex: palette["secondary"]!, section: "footer-\(index + 1)")
}

func drawCard(_ context: CGContext) {
    context.setFillColor(color(palette["background"]!))
    context.fill(CGRect(x: 0, y: 0, width: W, height: H))
    context.setShouldAntialias(true)
    context.setShouldSmoothFonts(false)
    for rule in rules {
        context.setStrokeColor(color(rule.hex)); context.setLineWidth(rule.thickness)
        context.move(to: CGPoint(x: rule.x1, y: H - rule.y)); context.addLine(to: CGPoint(x: rule.x2, y: H - rule.y)); context.strokePath()
    }
    context.textMatrix = .identity
    for item in placed {
        context.textPosition = item.origin
        CTLineDraw(item.shaped, context)
    }
}
func imageContext(_ width: Int, _ height: Int) -> CGContext {
    CGContext(data: nil, width: width, height: height, bitsPerComponent: 8, bytesPerRow: width * 4,
              space: CGColorSpace(name: CGColorSpace.sRGB)!, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)!
}
func writePNG(_ image: CGImage, _ name: String) throws {
    guard let destination = CGImageDestinationCreateWithURL(output.appendingPathComponent(name) as CFURL, "public.png" as CFString, 1, nil) else {
        try fail("Impossibile scrivere PNG")
    }
    CGImageDestinationAddImage(destination, image, nil)
    guard CGImageDestinationFinalize(destination) else { try fail("Export PNG fallito") }
}
let raster = imageContext(dimensions[0], dimensions[1])
drawCard(raster)
let cardImage = raster.makeImage()!
try writePNG(cardImage, outputs["card_png"]!)

var mediaBox = CGRect(x: 0, y: 0, width: W, height: H)
guard let pdf = CGContext(output.appendingPathComponent(outputs["card_pdf"]!) as CFURL, mediaBox: &mediaBox, nil) else {
    try fail("Impossibile creare il PDF")
}
pdf.beginPDFPage(nil); drawCard(pdf); pdf.endPDFPage(); pdf.closePDF()

func svgPath(_ path: CGPath) -> String {
    var parts: [String] = []
    path.applyWithBlock { pointer in
        let element = pointer.pointee, p = pointer.pointee.points
        switch element.type {
        case .moveToPoint: parts.append("M\(f(p[0].x)) \(f(p[0].y))")
        case .addLineToPoint: parts.append("L\(f(p[0].x)) \(f(p[0].y))")
        case .addQuadCurveToPoint: parts.append("Q\(f(p[0].x)) \(f(p[0].y)) \(f(p[1].x)) \(f(p[1].y))")
        case .addCurveToPoint: parts.append("C\(f(p[0].x)) \(f(p[0].y)) \(f(p[1].x)) \(f(p[1].y)) \(f(p[2].x)) \(f(p[2].y))")
        case .closeSubpath: parts.append("Z")
        @unknown default: break
        }
    }
    return parts.joined(separator: " ")
}
var svg = ["""
<svg xmlns="http://www.w3.org/2000/svg" width="\(dimensions[0])" height="\(dimensions[1])" viewBox="0 0 \(dimensions[0]) \(dimensions[1])" role="img" aria-labelledby="title description">
<title id="title">\(xml(card["quote"] as! String))</title>
<desc id="description">Impaginazione con Archivo Bold 700 e Libre Caslon Text Regular. Testo convertito in tracciati dai font reali.</desc>
<rect width="100%" height="100%" fill="\(palette["background"]!)"/>
<g transform="translate(0 \(f(H))) scale(1 -1)">
"""]
for rule in rules { svg.append("<path d=\"M\(f(rule.x1)) \(f(H - rule.y)) L\(f(rule.x2)) \(f(H - rule.y))\" fill=\"none\" stroke=\"\(rule.hex)\" stroke-width=\"\(f(rule.thickness))\"/>") }
for item in placed {
    svg.append("<g fill=\"\(item.hex)\" aria-label=\"\(xml(item.text))\" data-font=\"\(xml(item.family))\" data-font-size=\"\(f(item.size))\">")
    for run in CTLineGetGlyphRuns(item.shaped) as! [CTRun] {
        let runFont = (CTRunGetAttributes(run) as NSDictionary)[kCTFontAttributeName as String] as! CTFont
        let count = CTRunGetGlyphCount(run)
        var glyphs = [CGGlyph](repeating: 0, count: count), positions = [CGPoint](repeating: .zero, count: count)
        CTRunGetGlyphs(run, CFRange(location: 0, length: 0), &glyphs)
        CTRunGetPositions(run, CFRange(location: 0, length: 0), &positions)
        for index in 0..<count {
            guard let path = CTFontCreatePathForGlyph(runFont, glyphs[index], nil) else { continue }
            var transform = CGAffineTransform(translationX: item.origin.x + positions[index].x, y: item.origin.y + positions[index].y)
            if let transformed = path.copy(using: &transform) { svg.append("<path d=\"\(svgPath(transformed))\"/>") }
        }
    }
    svg.append("</g>")
}
svg.append("</g></svg>")
try svg.joined(separator: "\n").write(to: output.appendingPathComponent(outputs["card_svg"]!), atomically: true, encoding: .utf8)

let comparison = job["comparison"] as! Object
let generatedURL = URL(fileURLWithPath: comparison["absolute_image"] as! String)
let generatedSource = CGImageSourceCreateWithURL(generatedURL as CFURL, nil)!
let generatedImage = CGImageSourceCreateImageAtIndex(generatedSource, 0, nil)!
let compareW = 1748, compareH = 1130
let sheet = imageContext(compareW, compareH)
sheet.setFillColor(color("#EEEDE8")); sheet.fill(CGRect(x: 0, y: 0, width: compareW, height: compareH))
let labels = comparison["labels"] as! [String]
let labelFont = primary.at(22)
for (index, image) in [generatedImage, cardImage].enumerated() {
    let x = CGFloat(50 + index * 848)
    let label = line(labels[index], font: labelFont, tracking: 0, hex: "#18212E")
    sheet.textPosition = CGPoint(x: x, y: CGFloat(compareH) - 40)
    CTLineDraw(label, sheet)
    let previewWidth = CGFloat(image.width) / CGFloat(image.height) * 1000
    sheet.interpolationQuality = .high
    sheet.draw(image, in: CGRect(x: x + (800 - previewWidth) / 2, y: 44, width: previewWidth, height: 1000))
}
try writePNG(sheet.makeImage()!, outputs["comparison_png"]!)

let data = raster.data!.assumingMemoryBound(to: UInt8.self)
var backgroundSamples: [[Int]] = []
for point in [(10, 10), (30, 600), (10, 1200), (1420, 100), (1420, 1700)] {
    let index = point.1 * dimensions[0] * 4 + point.0 * 4
    backgroundSamples.append([Int(data[index]), Int(data[index + 1]), Int(data[index + 2])])
}
guard Set(backgroundSamples.map { $0.map(String.init).joined(separator: ",") }).count == 1 else { try fail("Fondo non uniforme") }
let result: Object = ["renderer": "Apple CoreText / CoreGraphics", "os_version": ProcessInfo.processInfo.operatingSystemVersionString,
                      "dimensions_px": dimensions, "fonts": ["primary": primaryDetails, "secondary": secondaryDetails],
                      "quote": card["quote"]!, "excerpt": card["emphasis"]!, "font_fallbacks_detected": false,
                      "missing_glyphs_detected": false, "text_out_of_bounds": false, "line_collisions_detected": false,
                      "palette": palette, "background_srgb_samples": backgroundSamples,
                      "font_size_ratio_effective": emphasisSize / quoteSize,
                      "blocks": metrics, "svg_outlined": true, "outputs": outputs]
let resultData = try JSONSerialization.data(withJSONObject: result, options: [.prettyPrinted, .sortedKeys])
try resultData.write(to: output.appendingPathComponent(outputs["metrics_json"]!))
print("Card impaginata: \(dimensions[0]) × \(dimensions[1]) px")
print("Archivo: \(primaryDetails["postscript_name"]!) · corpo frase \(f(quoteSize)) px · estratto \(f(emphasisSize)) px")
print("Font reali verificati; nessun fallback, glifo mancante, taglio o collisione fra righe.")
