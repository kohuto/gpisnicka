# Programování pokročilé

## Přehled

1. [Porovnani programovacich jazyků](#porovnani-programovacich-jazyků)
2. [Interpretovane a kompilované jazyky](#interpretovane-a-kompilované-jazyky)
3. [Virtuální prostředí](#virtuální-prostředí)
4. [Datové typy](#datové-typy)
5. [Čtení ze souborů](#čtení-ze-souborů)
6. [Výjimky](#výjimky)
7. [Moduly](#moduly)
8. [Testy](#testy)
9. [Proces vývoje softwaru](#proces-vývoje-softwaru)

## Porovnani programovacich jazyků
Doposud jsme se naučily základní programovací konstrukce v Pythonu. Víme, co je proměnná, umíme pracovat s podmínkami a cykly, víme, jak něco vypsat do konzole, víme dokonce, co jsou podprogramy (funkce / metody). Když se člověk naučí tyto základní konstrukce v jednom programovacím jazyce, tak mu to usnadní naučení se jiných programovacích jazyků. Většina těchto konstrukcí se totiž bude používat i v jných programovacích jazycích, bude se akorát lišit to, jak daný konstrukt zapíšeme. Nyní si proto ukážeme, co je společné všem jazykům a zároveň si ukážeme, v čem se naopak Python od ostatních jazyků liší.

### Co je stejné
Jak již zaznělo, všechny základní konstrukce, které jsme doposud probrali, najdeme i v ostatních programovacích jazycích.
#### Proměnná
Python:
```python
x = 5
```
JavaScript:
```javascript
let x = 5;
```
C#:
```c#
int x = 5;
```

#### Cyklus
Python:
```python
for i in range(5):
    print(i)
```
JavaScript:
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```
C#:
```c#
for (int i = 0; i < 5; i++) {
    Console.WriteLine(i);
}
```

#### Větvení
Python:
```python
if x > 0:
    print("X je kladné")
else:
    print("X je záporné nebo nulové")
```
JavaScript:
```javascript
if (x > 0) {
    console.log("X je kladné");
} else {
    console.log("X je záporné nebo nulové");
}
```
C#:
```c#
if (x > 0) {
    Console.WriteLine("X je kladné");
} else {
    Console.WriteLine("X je záporné nebo nulové");
}
```

#### Funkce
Python:
```python
def pozdrav(jmeno):
    print(f"Ahoj, {jmeno}!")
```
JavaScript:
```javascript
function pozdrav(jmeno) {
    console.log(`Ahoj, ${jmeno}!`);
}
```
C#:
```c#
void Pozdrav(string jmeno) {
    Console.WriteLine($"Ahoj, {jmeno}!");
}
```
### Co je jiné
Již v předchozích ukázkách jste si mohli všimnout drobných odlišností ostatních jednotlivých jazyků

#### Indetnace vs. složené závorky

Python používá indentaci (odsazení řádků) pro strukturování kódu:
```python
if x > 0:
    print("Kladné")
```
JavaScript, C#, Java používají složené závorky:
```javascript
if (x > 0) {
    console.log("Kladné");
}
```

#### Deklarace typů proměnných
Python automaticky rozpoznává typy:
```python
x = 5  # Python rozpozná, že jde o celé číslo
```
JavaScript je dynamicky typovaný (typy se kontrolují za běhu):
```javascript
let x = 5;
```
C# a Java jsou staticky typované (nutná deklarace typu):
```c#
int x = 5;
```

#### Konec příkazů
Python nepoužívá středníky na konci příkazů:
```python
x = 5
print(x)
```
JavaScript, C# a Java vyžadují středník:
```javascript
let x = 5;
console.log(x);
```
#### Jiné
Rozdílů mezi jazyky je samozřejmě obrovské množství. Cílem této kapitoly bylo však ukázat, že naprosté základy zůstanou vždy stejné, tudíž není potřeba se je učit pořád dokola.

## Virtuální prostředí

projekty tvoříme ve [virtuálním prostředí](https://code.visualstudio.com/docs/python/environments).

k čemu to je?

Jak vytvořit virtuální prostředí (virtual enviroment - venv)?

1. otevřete paletu příkazů (Ctrl+Shift+P)
2. vyhledejte položku `Python: Create Environment` a vyberte ji
3. objeví se dvě možnosti `Venv` nebo `Conda`.
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

---

### **Úloha: Překladač slov**

**Popis úlohy:**

Vytvořte program, který bude fungovat jako jednoduchý překladač slov z angličtiny do češtiny. Program by měl:

1. **Vytvořit slovník**, který obsahuje alespoň 5 anglických slov jako klíče a jejich české překlady jako hodnoty. 
2. **Požádat uživatele**, aby zadal anglické slovo, které chce přeložit do češtiny.
3. **Vyhledat** zadané slovo ve slovníku:

   - Pokud je slovo ve slovníku, program vypíše jeho český překlad.
   - Pokud slovo není ve slovníku, program vypíše zprávu, že překlad nebyl nalezen.

4. **Umožnit uživateli** přidat nové slovo do slovníku:

   - Zeptat se, zda chce uživatel přidat překlad neznámého slova.
   - Pokud ano, umožnit mu zadat český překlad a uložit jej do slovníku.

5. **Opakovat** kroky 2–4, dokud uživatel nezvolí ukončení programu.

**Příklad běhu programu:**

```
Zadejte anglické slovo k překladu (nebo 'konec' pro ukončení): cat
Český překlad slova 'cat' je 'kočka'.

Zadejte anglické slovo k překladu (nebo 'konec' pro ukončení): dog
Český překlad slova 'dog' je 'pes'.

Zadejte anglické slovo k překladu (nebo 'konec' pro ukončení): lion
Slovo 'lion' nebylo nalezeno ve slovníku.
Chcete přidat překlad slova 'lion'? (ano/ne): ano
Zadejte český překlad slova 'lion': lev
Slovo 'lion' bylo přidáno do slovníku.

Zadejte anglické slovo k překladu (nebo 'konec' pro ukončení): lion
Český překlad slova 'lion' je 'lev'.

Zadejte anglické slovo k překladu (nebo 'konec' pro ukončení): konec
Program ukončen.
```

**Tipy pro řešení:**

- **Vytvoření slovníku:**
  - Definujte slovník s několika anglickými slovy a jejich českými překlady.

- **Načítání vstupu od uživatele:**
  - Použijte funkci `input()` k načtení anglického slova od uživatele.
  - Ujistěte se, že program rozpozná příkaz k ukončení (např. pokud uživatel zadá `'konec'`).

- **Vyhledávání ve slovníku:**
  - Použijte konstrukci `if slovo in slovnik:` pro kontrolu, zda slovo existuje ve slovníku.
  - Pokud slovo není nalezeno, nabídněte uživateli možnost jej přidat.

- **Přidávání nových položek do slovníku:**
  - Pokud uživatel souhlasí, načtěte český překlad a přidejte jej do slovníku pomocí `slovnik[anglicke_slovo] = cesky_preklad`.

- **Opakování procesu:**
  - Použijte cyklus `while` pro opakování dotazování, dokud uživatel nezvolí ukončení programu.

---

### **Úloha: Analýza nákupního košíku**

**Popis úlohy:**

Napište program, který bude simulovat jednoduchý (a trochu nepraktický) nákupní košík v e-shopu. Program by měl:

1. **Načíst počet položek**, které chce uživatel přidat do košíku (celé číslo).
2. **Pro každou položku**:
   - Načíst **název produktu** (řetězec).
   - Načíst **cenu za jeden kus** produktu (desetinné číslo).
   - Načíst **počet kusů**, které chce uživatel koupit (celé číslo).
3. **Uložit všechny informace** o produktech do **seznamu slovníků**, kde každý slovník reprezentuje jednu položku s klíči `'nazev'`, `'cena'` a `'pocet'`.
4. Po zadání všech položek program:
   - **Vypíše seznam všech produktů** v košíku s jejich celkovou cenou za položku (jednotková cena \* počet kusů).
   - **Spočítá a vypíše celkovou cenu** za celý nákup.
   - **Najde a vypíše nejdražší položku** v košíku (podle celkové ceny za položku).

**Tipy pro řešení:**

- Použijte funkce `input()`, `int()`, `float()` pro načítání a konverzi vstupů.
- Seznam slovníků můžete vytvořit takto:

  ```python
  kosik = []
  produkt = {'nazev': ..., 'cena': ..., 'pocet': ...}
  kosik.append(produkt)
  ```

- Pro výpočet celkové ceny položky vynásobte jednotkovou cenu počtem kusů.
- Pro iteraci přes seznam položek použijte cyklus `for`.
- Pro nalezení nejdražší položky můžete porovnávat celkové ceny položek během iterace.

**Příklad vstupu a výstupu:**

```
Zadejte počet položek v košíku: 2

Zadejte název produktu: Kniha
Zadejte jednotkovou cenu produktu: 250.50
Zadejte počet kusů: 2

Zadejte název produktu: Sluchátka
Zadejte jednotkovou cenu produktu: 1500
Zadejte počet kusů: 1

Položky v košíku:
- Kniha: 2 ks x 250.5 Kč = 501.0 Kč
- Sluchátka: 1 ks x 1500.0 Kč = 1500.0 Kč

Celková cena nákupu: 2001.0 Kč
Nejdražší položka: Sluchátka (1500.0 Kč)
```
## Interpretovane a kompilované jazyky

Jazyky rozdělujeme na interpretované a kompilované, jaký je mezi nimi rozdíl se dočtete v tomto článku: https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/

### Interpreter jazyka Brainfuck
Jazyk Brainfuck je minimalistický ezoterický programovací jazyk. Byl vytvořen pro pobavení a jako výzva programátorům, pro praktické účely není vhodný. Jak tento jazyk funguje se dočtete v tomto článku: https://cs.wikipedia.org/wiki/Brainfuck.
Napište interpretr tohoto jazyka. Tzn. Vytvořte kód v pythonu, který dostane na vstupu kód (text) napsaný v jazyce brainfuck. Váš program tento kód (text) projde znak po znaku a vykoná jednotlivé instrukce. Práci si zjednodušte tím, že nebudete interpretovat znaky `[` a `]`. Tato verze brainfucku tedy nebude podporovat cykly.
1) vytvořte seznam určité délky, který bude reprezentovat paměťovou pásku Brainfucku
2) inicializujte všechny hodnoty seznamu na nulu
3) vytvořte si proměnnou, která bude ukazatel na aktuální pozici na pásce
4) iterujte přes každý znak vstupního kódu. Každý znak ve vstupním textu lze porjít nejjednodušeji tak, že napiíšte `for znak in vstup`. `for` cyklus takto proiteruje přes každý znak řetězce (řetezec je totiž v podstatě seznam znaků, a víme, že cyklus umí iterovat přes všechny prvky seznamu).
5) pro každý znak pomocí série if/elif/else příkazu rozhodněte, zda se jedná o validní znak / instrukci
6) pokud se jedna o validní instrukci, vykonejte ji v příslušné if větvi. Pokud se nejedná o validní instrukci, pokračuj na dalši znak
7) u znaku `.` použijte funkci `chr()` pro převod čísla na znak a `print()` pro výpis
8) u znaku `,` použijte funkci `input()` pro načtení vstupu a `ord()` pro převod znaku na číslo.

Kód, který vypíše text `HI!`:
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++.
```

Kód, který dostane na vstupu znak a vypíše tento znak a následující znak v ASCII tabulce:
```
,.+.
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
aa
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

## Proces vývoje softwaru

1. Analýza požadavků:
- Cílem této fáze je zjistit, co přesně software má dělat, jaké funkce a vlastnosti od něj očekává uživatel nebo zadavatel.
- Výstupem je dokumentace s jasně definovanými požadavky (tzv. "specifikace").
2. Návrh (Design):
- V této fázi se na základě požadavků vytváří návrh architektury softwaru. Návrh zahrnuje strukturu programu, modulární rozdělení (jak budou jednotlivé části systému spolupracovat), výběr technologií a databázový návrh.
3. Implementace (Programování):
- Po dokončení návrhu přichází fáze programování, kdy vývojáři píší kód podle návrhu a specifikace.
- Implementují jednotlivé moduly, funkce a propojují je do funkčního celku.
4. Testování:
- Testování je kritická fáze, kde je software kontrolován z hlediska funkčnosti, správnosti a spolehlivosti. Cílem je odhalit a opravit chyby, které se mohly objevit během implementace.
5. Nasazení (Deployment):
- Po úspěšném testování je software připraven k nasazení do produkčního prostředí, kde bude používán koncovými uživateli.
- Nasazení může být jednorázové nebo postupné (např. při zavádění nových verzí).
- Zahrnuje také přípravu dokumentace a školení uživatelů.
6. Údržba (Maintenance):
- Po nasazení software pokračuje fáze údržby, která zahrnuje opravy chyb, aktualizace a přidávání nových funkcí.
- Údržba je dlouhodobý proces, protože software je často v provozu několik let a je potřeba ho přizpůsobovat změnám požadavků a technologií.
