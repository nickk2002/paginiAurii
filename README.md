## PaginiAurii
Web scraper care cauta pe site-ul [Pagini Aurii](https://www.paginiaurii.ro/cauta/Autogara/) si salveaza rezultatele in format json.

## Instalare
1. Download la zip
2. Extract la zip
3. Ruleaza din terminal `pip install -r requirements.txt`
4. Fiind in folder-ul din unzip ruleaza `python main.py`
5. Introdu numele de cautat
6. Rezultatul va fi salvat in folder `json/numele_query` deci daca cauti `autogara` informatia va fi salvata in folder-ul `json/autogara.json`

## Format
Pentru fiecare rezultat se extrag urmatoarele informatii:
- titlul
- adresa
- numarul de telefon
- stelele

Exemplu de rezultat primit
```json
  {
    "title": "AUTOGARA AUGUSTINA S.R.L.",
    "address": "STR. PORTULUI, Nr. 28, TULCEA, Cod Postal 820243, Jud. TULCEA",
    "phone_number": "0743-334 827",
    "stars": 3
  }
```
In fisierul json va fi o lista de rezultate.
