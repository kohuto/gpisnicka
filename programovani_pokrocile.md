# Programování pokročilé

## Přehled

1. [Datové typy](#datové-typy)
1. [Čtení ze souborů](#čtení-ze-souborů)
1. [Výjimky](#výjimky)
1. [Moduly](#moduly)
1. [Testy](#testy)

## Datové typy

## Čtení ze souborů

### Úkol 1

Vytvoř textový soubor `basnicka.txt` a napiš do něj libovolný text. Poté vytvoř následující program:

```python
with open('basnicka.txt', 'r') as soubor:
    content = soubor.read()
print(content)
```

Program ulož do stejného adresáře, kde je uložen soubor `basnicka.txt`. Co vypíše program po spuštění?

### Úkol 2

funkce `open()` vrací hodnotu, která představuje otevřený soubor. Tahle hodnota má vlastní metody. Tady používáme metodu `read()`, která najednou přečte celý obsah souboru a vrátí ho jako řetězec.

Soubory se dají přirovnat k ledničce:

> abys něco mohl/a z ledničky vzít, nebo dát dovnitř, musíš ji předtím otevřít a potom zavřít. Bez zavření to sice na první pohled funguje taky, ale pravděpodobně potom brzo něco zplesniví.

Analogicky je potřeba zavřít soubor poté, co s ním přestaneš pracovat. Existují např. limity na počet současně otevřených souborů. Na Windows navíc nemůžeš soubor, který je stále otevřený, otevřít znovu.

Příkaz `with` vezme otevřený soubor (který vrací funkce open) a přiřadí ho do proměnné `soubor`. Pak následuje práce se souborem – v tomhle případě pomocí metody `read` čteme jeho obsah jako řetězec. Na konci od odsazeného bloku se soubor automaticky zavře.

### Úkol 3

Stáhni tento [soubor](https://drive.google.com/file/d/1o5l-Qe7hZTiRG6ggefP-nChuTSmTET7T/view?usp=drive_link) a vytvořte podprogram:

1. `head`, který dostane parametr `n` a vypíš prvních `n` řádků souboru
2. `tail`, který dostane parametr `n` a posledních `n` řádků souboru

Pomoct může následující funkce `readlines()`

```python
content = input_file.read()  # nacteni celeho obsahu souboru do jednoho retezce
lines = input_file.readlines()  # nacteni souboru souboru jako seznam radku
```

### Úkol 4

Slovník v Pythonu umožňuje ukládat párová data ve formátu `klíč:hodnota`. To znamená, že místo toho, abyste přistupovali k hodnotám pomocí jejich indexu (jako v seznamu), používáte k tomu unikátní klíč.

Příklad slovníku:

```python
osoba = {
    "jmeno": "Anna",
    "věk": 30,
    "město": "Praha"
}
```

V tomto slovníku jsou klíče: `"jmeno"`, `"věk"`, `"město"`. Jejich odpovídající hodnoty jsou: `"Anna"`, `30`, `"Praha"`.

K hodnotám můžete přistupovat pomocí klíče:

```python
print(osoba["jmeno"])  # vypíše "Anna"
```

Případně hodnoty měnit, podobně jako v seznamu:

```python
osoba["jmeno"] = "Pepa"
print(osoba["jmeno"])  # vypíše "Pepa"
```

Pokud dvojice `klíč:hodnota` ve slovníku není, tak se dvojice přidá:

```python
osoba["pohlaví"] = "žena"
print(osoba)
# vypíš {'jmeno': 'Anna', 'věk': 30, 'město': 'Praha', 'pohlaví': 'žena'}
```

### Úkol 5

Stáhněte tento [soubor](https://drive.google.com/file/d/1JQcyoNW9EKbc9jssgXmwLTSvdP6N2ubV/view?usp=sharing) a vypište prvních 10 slov v textu. Zkuste vypsat pouze slova, která mají alespoň 3 písmena.

### Úkol 6

Stáhněte tento [soubor](https://drive.google.com/file/d/1JQcyoNW9EKbc9jssgXmwLTSvdP6N2ubV/view?usp=sharing) a vypište 10 nejčastěji se vyskytujících slov v textu. Zkuste vypsat pouze slova, která mají alespoň 3 písmena.

### Úkol 7

Analyzujte text v tomto [souboru](https://drive.google.com/file/d/1o5l-Qe7hZTiRG6ggefP-nChuTSmTET7T/view?usp=drive_link) a vraťte průměrný počet slov ve větě.

### Úkol 8

Proveďte frekvenční analýzu některého z výše uvedených souborů. Vypište, kolikrát se v textu vyskytují jednotlivá písmena.

Tip: pro ověření, že je daný znak písmeno, můžete použít funkci `isalpha`.

### Úkol 9

Pro každé písmeno v textu vypište 5 písmen, které za ním následují nejčastěji.

### Úkol 10

Napište podprogram, který analyzuje text v [souboru](https://drive.google.com/file/d/1JQcyoNW9EKbc9jssgXmwLTSvdP6N2ubV/view?usp=sharing). Podprogram pak vygeneruje pseudo-náhodný text o `length` slovech. Text se generuje po slovech. Další generované slovo se náhodně vybírá z těch, které v původním textu po naposledy vygenerovaném slově následovaly.

## Výjimky

### Úkol 1

Podívej se na kód níže a vymysli příklad, kdy program selže:

```python
def nacti_cislo():
    """Získá od uživatele celé číslo a vrátí ho"""
    odpoved = input('Zadej číslo: ')
    return int(odpoved)
```

### Úkol 2

Jak docílíme následující chybové hlášky?

```
Traceback (most recent call last):
  File "ukazka.py", line 4, in nacti_cislo
    cislo = int(odpoved)
ValueError: invalid literal for int() with base 10: 'pes'
```

### Úkol 3

Řešením problémů v předchozích úkolech by mohla být nějaká funkce `obsahuje_jen_cislice()`, existuje v pythonu podobná funkce? Je vhodné je používat?

### Úkol 4

Jaké budou výstupy následujícího kódu:

```python
print('123'.isnumeric())
print('abc'.isnumeric())
print('½'.isnumeric)
print(int('½'))
print(int(1/2))
print('௩三๓໓'.isnumeric())
print(int(' 42'))
print(' 42'.isdecimal())
```

### Úkol 5

Chceme-li tedy zjisti, zda funkce `int` umí převést řetězec na číslo, je nejlepší na to skutečně použít funkci `int`.

V případě, že by došlo k selhání, existuje v pythonu příkaz `try/except`. Zkus spustit následující kód a zadávat různé platné i neplatné vstupy:

```python
def nacti_cislo():
    while True:
        vstup = input('Zadej číslo: ')
        try:
            return int(vstup)
        except ValueError:
            print('Toto není číslo!')
```

Jak to funguje? Příkazy v bloku `try` se provedou, ale když nastane uvedená výjimka, Python přeskočí zbytek bloku `try` a provede všechno v bloku `except`. Pokud výjimka nenastala, přeskočí se celý blok `except`.

### Úkol 6

V úkolu 5 bylo za slovíčkem `except` uvedeno ještě `ValueError`. To je název chyby. Všechny názvy jsou uvedeny [zde](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).

Vytvořte podprogram, v němž bude použit příkaz `try/except` a bude využívat nějaký jiný druh chyby.

### Úkol 7

Vymysli, jak by vypadalo tělo podprogramu `neco_udelej()`, aby se vypsalo vždy některé z čísel. Lze vypsat všechna čísla (ne nutně najednou)?

```python
try:
    neco_udelej()
except ValueError:
    print('1')
except NameError:
    print('2')
except Exception:
    print('3')
except TypeError:
    print('4')
else:
    print('5')
finally:
    print('6')
```

### Úkol 8

Napište podprogram, který dostane jako parametr délku strany čtverce a následně vypočítá jeho obsah.

### Úkol 9

Co nám vrátí předchozí podprogram, když ho zavoláme následujícím způsobem?

```python
obsah_ctverce(-5)
```

V takovéme případě bychom asi chtěli, aby program zahlásil chybu. Prakticky to lze provést následovně:

```python
def obsah_ctverce(strana):
    if strana > 0:
        return strana ** 2
    else:
        raise ValueError(f'Strana musí být kladná, číslo {strana} kladné není!')
```

Podobně jako `return` i příkaz `raise` ukončí funkci. A nejen tu – pokud na tuhle konkrétní chybu není program předem připravený, ukončí se celý program.

## Moduly

## Testy

Nyní si ukážeme, jak psát testy v jazyce Python pomocí knihovny `pytest`. Pytest je populární nástroj pro psaní a spouštění testů, který usnadňuje vytváření a organizaci testovacího kódu.

Zatím jsme programy testovali tak, že jsme je zkusili spustit, něco jsme zadali a podívali se, jestli jsou výsledky v pořádku. U větších programů už by to bylo náročné kontrolovat. Proto se v praxi napíše jiný program, které náš program testuje za nás. Jedná se o funkce s parametrem a použití modulů, které program spouští a ověří, že se při změně nerozbilo nic, co dříve fungovalo.

### Instalace pytest

Knihovnu `pytest` je potřeba nainstalovat následujícím příkazem:

```
pip install pytest
```

### Adresářová struktura

Vytvořte následující adresářovou strukturu:

```
my_project/
├─ calculator.py
└─ test_calculator.py
```

Do souboru `calculator.py` vložte následující kód

```python
def add(a, b):
    return a + b
```

Do souboru `test_calculator.py`

```python
from calculator import add

def test_addition():
    result = add(2, 3)
    assert result == 5
```

### Spuštění

Vytvořili jsme funkci `test_addition`, která testuje funkci `add` z naší kalkulačky. Příkaz `assert` vyhodnotí výraz za ním a pokud výsledek není pravdivý, vyvolá výjimku, která způsobí, že test selže.

Testy můžeme nyní spustit pomocí následujícího příkazu:

```
pytest
```

### Úkol 1

### Úkol 2

### Úkol 3

### Úkol 4
