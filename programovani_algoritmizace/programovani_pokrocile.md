# Programování pokročilé

## Přehled

1. [Virtuální prostředí](#virtuální-prostředí)
2. [Datové typy](#datové-typy)
3. [Čtení ze souborů](#čtení-ze-souborů)
4. [Výjimky](#výjimky)
5. [Moduly](#moduly)
6. [Testy](#testy)
7. [Co dál?](#co-dál)

## Virtuální prostředí

projekty tvoříme ve [virtuálním prostředí](https://code.visualstudio.com/docs/python/environments).

k čemu to je?

Jak vytvořit virtuální prostředí (virtual enviroment - venv)?

1. otevřete paletu příkazů (Ctrl+Shift+P)
2. vyhledejte položku `Python: Create Environment` a vyberte ji
3. objeví se dvě možnosti `Venv` or `Conda`.
4. vybereme možnost `Venv`
5. vybereme požadovaný interpretr

## Datové typy

### Připomenutí načítání vstupu

#### Kalkulačka

Pro načtení vstupu z konzole používáme funkci `input()`. Napište program, který načte dvě čísla `a` a `b`. Program vypíše jejich součet, rozdíl, podíl a součin.

#### BMI

Napište program, který dostane na vstupu výšku v metrech a váhu v kg a na výstup vypíše BMI uživatele.

### Shrnutí datových typů

Už jsme viděli následující datové typy:

#### Celá čísla

```python
x = 5
y = -10
```

#### Desetinná čísla

```python
a = 3.14
b = -0.5
```

#### Řetězce

```python
text1 = 'Ahoj, světe!'
text2 = "Python je skvělý."
```

#### Logická hodnota

```python
pravda = True
nepravda = False
```

#### Seznamy

```python
cisla = [1, 2, 3, 4, 5]
jmena = ['Anna', 'Petr', 'Eva']
```

#### Slovníky

```python
osoba = {
    'jmeno': 'Jan',
    'prijmeni': 'Novák',
    'vek': 30
}
```

Na datový typ je potřeba myslet napřiklad při načítání vstupu, jak jsme viděli v úvodním příkladu. Funkce `input()` vrací řetězec, proto je potřeba provést konverzi na požadovaný datový typ:

```python
cislo = int(input("Zadejte celé číslo: "))
print(cislo * 2)
```

## Čtení ze souborů

### Úkol 1

Vytvoř textový soubor `basnicka.txt` a napiš do něj libovolný text. Poté vytvoř následující program:

```python
with open('basnicka.txt', 'r', encoding='utf-8') as soubor:
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

Vytvoř podprogram, který spočítá, kolik je v souboru `basnicka.txt` znaků.

### Úkol 4

Vytvoř podprogram, který spočítá, kolik má soubor `basnicka.txt` řádků. Doporučuji použít funkci `readlines()`.

```python
content = input_file.read()  # nacteni celeho obsahu souboru do jednoho retezce
lines = input_file.readlines()  # nacteni souboru souboru jako seznam radku
```

### Úkol 5

Vytvořte podprogram:

1. `head`, který dostane parametr `n` a vypíš prvních `n` řádků ze souboru `basnicka.txt`
2. `tail`, který dostane parametr `n` a posledních `n` řádků souboru `basnicka.txt`

### Úkol 6

Napište podprogram, který ze souboru básnička vypíše prvních 10 slov. Doporučuji použít funkci `split()`.

### Úkol 7

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
# vypíše {'jmeno': 'Anna', 'věk': 30, 'město': 'Praha', 'pohlaví': 'žena'}
```

### Úkol 8

Proveďte frekvenční analýzu písmen v souboru básnička. Vypište, kolikrát se v souboru vyskytují jednotlivá písmena.

Tip: pro ověření, že je daný znak písmeno, můžete použít funkci `isalpha`.

### Úkol 9

Upravte program ze cvičení 8, aby písmena ve slovníku seřadil podle toho, jak často se v textu vyskytovala. Poté vypište 5 nejčastěji se vyskytujících písmen v textu.

### Úkol 10

Vytvořte program, který spočítá průměrný počet slov ve větě v souboru `basnicka.txt`.

### Úkol 11 \*

Pro každé písmeno v textu vypište 5 písmen, které za ním následují nejčastěji.

### Úkol 12 \*

Napište podprogram, který analyzuje text v [souboru](https://drive.google.com/file/d/1JQcyoNW9EKbc9jssgXmwLTSvdP6N2ubV/view?usp=sharing). Podprogram pak vygeneruje pseudo-náhodný text o `length` slovech. Text se generuje po slovech. Další generované slovo se náhodně vybírá z těch, které v původním textu po naposledy vygenerovaném slově následovaly.

## Výjimky

### Úkol 1

Podívej se na kód níže a vymysli příklad, kdy program selže:

```python
def prevracena_hodnota():
    cislo = int(input('Zadej číslo: '))
    return cislo
```

### Úkol 2

Řešením problémů v předchozím úkolu by mohla být nějaká hypotetická funkce `obsahuje_jen_cislice()`. Zkuste takovou funkci najít a upravte předchozí program pomocí příkazu `if` a této funkce tak, aby se text převáděl na číslo pouze, pokud obsahuje jen číslice.

### Úkol 3

Jaké budou výstupy následujícího kódu:

```python
print('123'.isnumeric())
print('abc'.isnumeric())

print('½'.isnumeric)
print(int('½'))
print(int(1/2))

print('௩三๓໓'.isnumeric())
print(int('௩三๓໓'))

print(' 42'.isnumeric())
print(int(' 42'))
```

### Úkol 4

Chceme-li tedy zjistit, zda funkce `int` umí převést řetězec na číslo, je nejlepší na to skutečně použít funkci `int`.

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

Za slovíčkem `except` je uvedeno ještě `ValueError`. To je název chyby. Všechny názvy jsou uvedeny [zde](https://docs.python.org/3/library/exceptions.html#exception-hierarchy).

### Úkol 6

V programu největší společný dělitel ošetřete pomocí odchytávání výjimek dělení nulou.

### Úkol 7

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

V takovém případě bychom asi chtěli, aby program zahlásil chybu. Prakticky to lze provést následovně:

```python
def obsah_ctverce(strana):
    if strana > 0:
        return strana ** 2
    else:
        raise ValueError(f'Strana musí být kladná, číslo {strana} kladné není!')
```

Podobně jako `return` i příkaz `raise` ukončí funkci. A nejen tu – pokud na tuhle konkrétní chybu není program předem připravený, ukončí se celý program.

## Moduly

Vytvořte ve složce, kde jsou uložené programy `gsd.py`, `is_in_array.py` a `is_prime_number.py` čtvrtý soubor `main.py`.

Na začátek souboru `main.py` umístěte tento kód:

```python
import is_in_array
```

Nyní můžete volat v souboru `main.py` funkci `is_in_array()` tímto způsobem:

```python
import is_in_array
is_in_array.is_in_array()
```

Zápis vlastně říká _Ze souboru is_in_array.py zavolej funkci is_in_array()_

Pokud nechceme pořád psát `is_in_array.is_in_array()` můžeme na záčátek souboru napsat tento kód:

```python
from is_in_array import is_in_array
```

Nyní lze zavolat funkci tímto způsobem:

```python
from is_in_array import is_in_array
is_in_array()
```

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

Vytvořte sadu testů pro funkci `add()`.

### Úkol 2

Rozšiřte program `calculator.py` o další funkce, aby se jednalo o dobře vychovanou kalkulačku. Pro každou funkci vytvořte sadu testů.

### Úkol 3

Vytvořte testy pro funkci `gsd()`

### Úkol 4

Vytvořte testy pro funkci `is_in_array()`

### Úkol 5

Vytvořte testy pro funkci `is_prime_number()`
