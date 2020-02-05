# Sběr geodat v adresářové struktuře

Program `geocrawler.py` nalezene všechna geodata v adresáři a jeho podadresářích a podle geometrie vytvoří tři soubory - s body, liniemi a polygony.

## Vstup

Vstupem je absolutní cesta adresáře, který chceme spolu s jeho podadresáři procházet.

## Průběh

Program `geocrawler.py` je souštěn z příkazové řádky spolu se vstupem ve formátu `py geocrawler.py adresář`, tedy například `py du3_anna_krusova.py C:\Users\zvukar\Desktop\du3_testdata`. V průběhu program vypisuje s jakým souborem momentálně pracuje a v případně chybného souboru vypíše chybovou hlášku. Validním geodatům je přiřazen nový atribut `filepath`, který obsahuje absolutní cestu do adresáře, ze kterého pochází.


## Výstup

Výstupem jsou tři soubory ve formátu `GeoJSON`, v nichž jsou rozděleny podle geometrie všechna godata z procházeného adresáře a jeho podadresářů, která navíc obsahují nový atribut `filepath`.
