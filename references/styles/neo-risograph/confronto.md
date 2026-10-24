# Risograph: quanto overprint?

## Esito

Scelta dell'utente: un solo profilo **Risograph**, che include sempre
overprint con mescolanza visibile degli inchiostri. L'esempio con
overprint è quello corrente del catalogo; il knockout resta soltanto
un controllo storico nel repository di sviluppo e non è incluso nello
ZIP né offerto come variante dello stile. Si può variare
l'estensione della sovrapposizione, non eliminarla.

La ricerca distingue i due concetti sul piano tecnico. La loro unione
obbligatoria è invece una decisione estetica di questo profilo.

| Prova | Che cosa guardare |
| --- | --- |
| [Overprint selettivo](esempio-overprint.png) | Il ramo corallo attraversa la mano blu e gli incroci diventano prugna; i dettagli dei due soggetti restano percepibili |
| Controllo storico · knockout, non incluso | Il ramo resta corallo anche sopra la mano; variante non scelta, conservata nel repository di sviluppo |

Entrambe conservano carta calda, toni fotografici a grana fine e piccoli
vuoti d'inchiostro. Non si tratta di Halftone con grossi punti, né della
sola ricolorazione bicroma di una foto. Le immagini indipendenti hanno un
ruolo semantico: mano e ramo esprimono incontro e crescita.

## Protocollo e limiti

La frase dimostrativa originale è «Le idee crescono quando si incontrano.»
La visualizzazione mantiene esattamente tre righe e il punto finale:

```text
LE IDEE CRESCONO
QUANDO SI
INCONTRANO.
```

La prima card usa due reference materiali, ricavate da
`presentation-9-o.avif` e `presentation-4-o.avif`. La seconda è un editing
della prima come unico input: non una nuova generazione indipendente.
Una generazione per variante, nessuna correzione successiva. I prompt
effettivi e le osservazioni sono salvati separatamente:

- [Prompt overprint](prompt-overprint.md) e [note](note-overprint.md).
- Prompt e note knockout sono conservati soltanto nel repository di sviluppo.

I due PNG nativi misurano 1122 × 1402 px. La verifica è stata fatta a
dimensione nativa e a 375 px di larghezza: testo integro, punto presente e
differenza degli incroci leggibile. La modalità dominante, altre frasi e
le altre famiglie compositive non sono ancora state testate.

La revisione conserva l'impianto, non tutti i pixel: grana, carta e alcuni
bordi sono rigenerati. Non è quindi una prova quantitativa o un confronto
con/senza skill. Il piccolo scarto di registro richiesto non è abbastanza
chiaro da considerarlo verificato. Non si certificano fluorescenza,
separazioni spot né comportamento di una stampa fisica.

## Integrazione

Il [profilo YAML](profilo.yaml) richiede overprint con mescolanza e almeno
due inchiostri. Offre soltanto `selective` e `dominant`, entrambe con
mescolanza, senza modalità `none` o knockout. La
[libreria compositiva](composizioni.yaml) offre tre famiglie che rispettano
questo vincolo, senza imporre mano, pianta, palette o impaginato del test.
La [ricerca](ricerca.md) documenta le fonti e gli allegati.

L'ID storico `neo-risograph` è conservato nel catalogo esteso; il nome
visibile diventa Risograph. La selezione V1 non cambia. Vecchio profilo,
immagini precedenti e controllo knockout restano nel repository di
sviluppo, fuori da questo ZIP e dagli esempi correnti del catalogo.

Il pacchetto contiene soltanto lo stile corrente e l'esempio con mescolanza.
Non pubblica automaticamente la gallery Sites.
