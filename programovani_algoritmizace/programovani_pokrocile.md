# Přehled

1. [Porovnani programovacich jazyků](#porovnani-programovacich-jazyků)
2. [Debugging]()
2. [Virtuální prostředí](#virtuální-prostředí)
3. [Načítání vstupu](#načítání-vstupu)
4. [Cyklus While](#cyklus-while)
5. [Příkaz Return](#příkaz-return)
6. [Datové typy](#datové-typy)
7. [Slovníky](#co-jsou-slovníky)
8. [Interpretovane a kompilované jazyky](#interpretovane-a-kompilované-jazyky)
9. [Čtení ze souborů](#čtení-ze-souborů)
10. [Synktatický cukr]()
11. [Výjimky](#výjimky)
12. [Moduly](#moduly)
13. [Testy](#testy)
14. [Proces vývoje softwaru](#proces-vývoje-softwaru)

# Porovnani programovacich jazyků
Doposud jsme se naučily základní programovací konstrukce v Pythonu. Víme, co je proměnná, umíme pracovat s podmínkami a cykly, víme, jak něco vypsat do konzole, víme dokonce, co jsou podprogramy (funkce / metody). Když se člověk naučí tyto základní konstrukce v jednom programovacím jazyce, tak mu to usnadní naučení se jiných programovacích jazyků. Většina těchto konstrukcí se totiž bude používat i v jných programovacích jazycích, bude se akorát lišit to, jak daný konstrukt zapíšeme. Nyní si proto ukážeme, co je společné všem jazykům a zároveň si ukážeme, v čem se naopak Python od ostatních jazyků liší.

## Co je stejné
Jak již zaznělo, všechny základní konstrukce, které jsme doposud probrali, najdeme i v ostatních programovacích jazycích.
##  Proměnná
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

##  Cyklus
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

##  Větvení
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

##  Funkce
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
## Co je jiné
Již v předchozích ukázkách jste si mohli všimnout drobných odlišností ostatních jednotlivých jazyků

##  Indetnace vs. složené závorky

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

##  Deklarace typů proměnných
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

##  Konec příkazů
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
##  Jiné
Rozdílů mezi jazyky je samozřejmě obrovské množství. Cílem této kapitoly bylo však ukázat, že naprosté základy zůstanou vždy stejné, tudíž není potřeba se je učit pořád dokola.

# Debugging
Bug = chyba
Debugging = "hledání a odstraňování chyby"

Vy pythonu nemusíme spustit celý kód najednou. Můžeme ho spouštět "krok po kroku". Takto snadněji odhalíme případné chyby v kódu. Jak na to ukazuje následující shorts: [Debugging python code in VS Code](https://www.youtube.com/shorts/wPkXrf5rGCY).

Pokud potřebujete detailnější vysvětlení, tak ho najdete v tomto tutoriálu:
[Debugging in VS code](https://www.youtube.com/watch?v=oCcTiRGPogQ)

## Úkol: Debugging
Vyzkoušejte se odkrokovat (provést debugging) na libovolném programu, který již máte vytvořený (například `Opilcova procházka`).

# Virtuální prostředí

projekty tvoříme ve [virtuálním prostředí](https://code.visualstudio.com/docs/python/environments).

k čemu to je?

Jak vytvořit virtuální prostředí (virtual enviroment - venv)?

1. otevřete paletu příkazů (Ctrl+Shift+P)
2. vyhledejte položku `Python: Create Environment` a vyberte ji
3. objeví se dvě možnosti `Venv` nebo `Conda`.
4. vybereme možnost `Venv`
5. vybereme požadovaný interpretr

# Načítání vstupu

## Kalkulačka

Pro načtení vstupu z konzole používáme funkci `input()`. Napište program, který načte dvě čísla `a` a `b`. Program vypíše jejich součet, rozdíl, podíl a součin.

## BMI

Napište program, který dostane na vstupu výšku v metrech a váhu v kg a na výstup vypíše BMI uživatele.

# Cyklus While
Co vypíše následující blok kódu?
```python
x = 0
while(x < 10)
    print(x)
    x += 1
```
Rozdíl mezi `for` a `while` cyklem je ten, že cyklus `for` má pevný počet opakování (tzn. dopředu víme, kolikrát se cyklus vykoná), zatímco `while` cyklus nemá pevný počet opakování (dopředu nevíme, kolikrát se cyklus zopakuje). Cyklus `while` opakuje blok kódu, dokud je daná podmínka pravdivá. Před každou iterací se podmínka vyhodnotí – pokud je pravdivá, kód se provede, pokud ne, cyklus se ukončí.

## Úkol: Sčítadlo
Vytvoř program, který pomocí cyklu `while` sečte čísla od 1 do 10 a součet na konci vypíše.

## Úkol: Hádání náhodného čísla
Napiš program, který vygeneruje náhodné číslo mezi 1 a 10. Program bude opakovaně vyzývat uživatele, aby hádal toto číslo. Po každém pokusu program sdělí, zda je tipované číslo příliš nízké, příliš vysoké nebo správné. Cyklus `while` se použije k opakování hádání, dokud uživatel neuhodne správné číslo.

## Úkol: Faktoriál
Vytvoř program, který požádá uživatele o zadání kladného celého čísla. Poté pomocí cyklu `while` vypočítá a zobrazí faktoriál tohoto čísla.

# Příkaz Return
Co vypíše následující blok kódu?
```python
def soucet(a):
    plusjedna = a + 1
    return plusjedna

výsledek = soucet(3)
print(výsledek)
```

V Pythonu se příkaz `return` používá uvnitř funkcí k ukončení jejich provádění a vrácení hodnoty volajícímu kódu. Když funkce dosáhne příkazu `return`, okamžitě se ukončí a vrátí zadanou hodnotu.

# Úkol: Kalkulačka
Vytvoř tři funkce s názvy `soucet`, `rozdil` a `soucin`, které přijímají dvě čísla jako argumenty. Každá funkce by měla pomocí příkazu `return` vrátit:

- `soucet`: součet dvou čísel,
- `rozdil`: rozdíl dvou čísel (první minus druhé),
- `soucin`: součin dvou čísel.

Poté tyto funkce zavolej s libovolnými dvěma čísly a vypiš jejich výsledky.

## Úkol: Sudé nebo liché
Napiš funkci `je_sudé`, která přijímá jako parametr jedno číslo a vrací `True`, pokud je číslo sudé, nebo `False`, pokud je liché. Použij příkaz `return` k vrácení hodnoty. Poté funkci použij k ověření, zda je dané číslo sudé, a výsledek vypiš.

# Datové typy

## Celá čísla

```python
x = 5
y = -10
```

## Desetinná čísla

```python
a = 3.14
b = -0.5
```

## Řetězce

```python
text1 = 'Ahoj, světe!'
text2 = "Python je skvělý."
```

## Logická hodnota

```python
pravda = True
nepravda = False
```

## Seznamy

```python
cisla = [1, 2, 3, 4, 5]
jmena = ['Anna', 'Petr', 'Eva']
```

## Slovníky

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

# Co jsou `Slovníky`

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
---

## **Úloha: Překladač slov**

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

- **Vyhledávání ve slovníku:**
  - Jestli je slovo ve slovníku zjistíte takto: `if slovo in slovnik:`.

- **Přidávání nových položek do slovníku:**
  - Slovo přidáte od lsovníku tímto způsobem `slovnik[anglicke_slovo] = cesky_preklad`.

- **Opakování procesu:**
  - Použijte cyklus `while` pro opakování dotazování, dokud uživatel nezvolí ukončení programu.

---

## **Úloha: Analýza nákupního košíku**

Napište program, který bude simulovat jednoduchý nákupní košík v e-shopu. Program by měl:

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
# Interpretovane a kompilované jazyky

Jazyky rozdělujeme na interpretované a kompilované, jaký je mezi nimi rozdíl se dočtete v tomto článku: https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/

## Interpreter jazyka Brainfuck
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
# Čtení ze souborů

## **Úkol: Vypsání obsahu souboru**

Vytvoř textový soubor `basnicka.txt` a napiš do něj libovolný text. Poté vytvoř následující program:

```python
with open('basnicka.txt', 'r', encoding='utf-8') as soubor:
    content = soubor.read()
print(content)
```

Program ulož do stejného adresáře, kde je uložen soubor `basnicka.txt`. Co vypíše program po spuštění?

## Práce se soubory - vypisování

funkce `open()` vrací hodnotu, která představuje otevřený soubor. Tahle hodnota má vlastní metody. Tady používáme metodu `read()`, která najednou přečte celý obsah souboru a vrátí ho jako řetězec.

Soubory se dají přirovnat k ledničce:

> abys něco mohl/a z ledničky vzít, nebo dát dovnitř, musíš ji předtím otevřít a potom zavřít. Bez zavření to sice na první pohled funguje taky, ale pravděpodobně potom brzo něco zplesniví.

Analogicky je potřeba zavřít soubor poté, co s ním přestaneš pracovat. Existují např. limity na počet současně otevřených souborů. Na Windows navíc nemůžeš soubor, který je stále otevřený, otevřít znovu.

Příkaz `with` vezme otevřený soubor (který vrací funkce open) a přiřadí ho do proměnné `soubor`. Pak následuje práce se souborem – v tomhle případě pomocí metody `read` čteme jeho obsah jako řetězec. Na konci od odsazeného bloku se soubor automaticky zavře.

## Úkol: Počet znaků

Vytvoř podprogram, který spočítá, kolik je v souboru `basnicka.txt` znaků.

## Úkol: Počet řádků

Vytvoř podprogram, který spočítá, kolik má soubor `basnicka.txt` řádků. Doporučuji použít funkci `readlines()`.

```python
content = input_file.read()  # nacteni celeho obsahu souboru do jednoho retezce
lines = input_file.readlines()  # nacteni souboru souboru jako seznam radku
```

## Úkol: Head and Tail

Vytvořte podprogram:

1. `head`, který dostane parametr `n` a vypíš prvních `n` řádků ze souboru `basnicka.txt`
2. `tail`, který dostane parametr `n` a posledních `n` řádků souboru `basnicka.txt`

## Úkol: Frekvenční analýza písmen

Proveďte frekvenční analýzu písmen v souboru básnička. Vypište, kolikrát se v souboru vyskytují jednotlivá písmena.

Tip: pro ověření, že je daný znak písmeno, můžete použít funkci `isalpha`.

## Úkol: Triviální ChatGPT (doborovolný úkol)

Napište podprogram, který analyzuje text v [souboru](https://drive.google.com/file/d/1JQcyoNW9EKbc9jssgXmwLTSvdP6N2ubV/view?usp=sharing). Podprogram pak vygeneruje pseudo-náhodný text o `length` slovech. Text se generuje po slovech. Další generované slovo se náhodně vybírá z těch, které v původním textu po naposledy vygenerovaném slově následovaly.

# Svatá trojice
## List comprehension

List comprehension je elegantní a stručný způsob, jak vytvořit nový seznam na základě existujícího. Umožňuje aplikovat výraz na každý prvek v iterovatelné sekvenci a volitelně zahrnout podmínku pro filtrování.

**Syntaxe:**

```python
nový_seznam = [výraz for položka in sekvence if podmínka]
```

**Příklad bez podmínky:**

```python
# Vytvoření seznamu čtverců čísel od 1 do 5
čtverce = [x**2 for x in range(1, 6)]
print(čtverce)  # Vypíše: [1, 4, 9, 16, 25]
```
> `range(1,6)` je to stejné, jako kdybychom napsali `[1, 2, 3, 4, 5]` 

**Příklad s podmínkou:**

```python
# Vytvoření seznamu sudých čísel od 1 do 10
sudá_čísla = [x for x in range(1, 11) if x % 2 == 0]
print(sudá_čísla)  # Vypíše: [2, 4, 6, 8, 10]
```

## Anotace typu proměnné

I když Python je dynamicky typovaný jazyk a typy proměnných se určují při běhu programu, můžete použít anotace typu pro proměnné. To zlepšuje srozumitelnost kódu a pomáhá nástrojům pro statickou analýzu.

**Syntaxe:**

```python
název_proměnné: typ = hodnota
```

**Příklad:**

```python
# Anotace typu pro proměnné
jméno: str = "Anna"
věk: int = 25
výška: float = 1.68
student: bool = True

print(f"Jméno: {jméno}, Věk: {věk}, Výška: {výška}, Student: {student}")
# Vypíše: Jméno: Anna, Věk: 25, Výška: 1.68, Student: True
```

Anotace typu jsou zvláště užitečné v rozsáhlejších projektech, kde přispívají k lepší udržovatelnosti a čitelnosti kódu.

## Návratový typ funkce

V Pythonu můžete pomocí anotací typu specifikovat návratový typ funkce. To zlepšuje čitelnost kódu a usnadňuje detekci chyb při statické analýze kódu. Anotace se však při běhu programu nevyhodnocují.

**Syntaxe:**

```python
def název_funkce(parametry) -> návratový_typ:
    ...
    return hodnota
```

**Příklad:**

```python
def součin(a: int, b: int) -> int:
    return a * b

výsledek = součin(4, 5)
print(výsledek)  # Vypíše: 20
```

V tomto příkladu funkce `součin` přijímá dva argumenty typu `int` a vrací hodnotu typu `int`.

# Výjimky

## Úkol: Kdy selže?

Podívej se na kód níže a vymysli příklad, kdy program selže:

```python
def prevracena_hodnota():
    cislo = int(input('Zadej číslo: '))
    return cislo
```

## Úkol: Najdi funkci

Řešením problémů v předchozím úkolu by mohla být nějaká hypotetická funkce `obsahuje_jen_cislice()`. Zkuste takovou funkci najít a upravte předchozí program pomocí příkazu `if` a této funkce tak, aby se text převáděl na číslo pouze, pokud obsahuje jen číslice.

## Úkol: Jaký je výstup?

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

## Výjimky vysvětlení

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

## Úkol: Úprava kalkulačky

V programu Kalkulačka v kapitole Načítání vstupu ošetřete pomocí odchytávání výjimek dělení nulou a jestli jsou na vstupu zadaná čísla.

## Úkol: Úprava BMI

V programu BMI ošetřete pomocí odchytávání výjimek dělení nulou a jestli jsou na vstupu zadaná čísla.

## Úkol: Úprava košíku

V programu analýza nákupního košíku ošetřete pomocí odchytávání výjimek, že uživatel zadal na vstupu čísla.

## Úkol: Co nelze vypsat?

Je některé číslo, které nebude nikdy vypsáno? Připadně proč?

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

## Úkol: Obsah čtverce

Napište podprogram, který dostane jako parametr délku strany čtverce a následně vypočítá jeho obsah.

## Úkol: Ukončení programu s chybou

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

# Moduly
Vytvořte (klidně za využití konverzačního chatbota) tři programy:
- `gsd.py` - funkce `gsd` dostane jako argument dvě čísla a vrátí jejich největšího společného dělitele.
- `is_in_array.py` - funkce `is_in_array` dostane jako argument číslo a seznam čísel. Funkce vrátí `True`, jestliže se číslo nachází v seznamu. V opačném případě vrátí `False`.
- `is_prime_number.py` – funkce `is_prime_number` dostane jako argument číslo. Vrátí `True`, jestliže je číslo prvočíslo. V opačném případě vrát funkce `False`.

---

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

# Testy

Nyní si ukážeme, jak psát testy v jazyce Python pomocí knihovny `pytest`. Pytest je populární nástroj pro psaní a spouštění testů, který usnadňuje vytváření a organizaci testovacího kódu.

Zatím jsme programy testovali tak, že jsme je zkusili spustit, něco jsme zadali a podívali se, jestli jsou výsledky v pořádku. U větších programů už by to bylo náročné kontrolovat. Proto se v praxi napíše jiný program, které náš program testuje za nás. Jedná se o funkce s parametrem a použití modulů, které program spouští a ověří, že se při změně nerozbilo nic, co dříve fungovalo.

## Instalace pytest

Knihovnu `pytest` je potřeba nainstalovat následujícím příkazem:

```
pip install pytest
```

## Adresářová struktura

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

## Spuštění

Vytvořili jsme funkci `test_addition`, která testuje funkci `add` z naší kalkulačky. Příkaz `assert` vyhodnotí výraz za ním a pokud výsledek není pravdivý, vyvolá výjimku, která způsobí, že test selže.

Testy můžeme nyní spustit pomocí následujícího příkazu:

```
pytest
```

## Úkol 1

Vytvořte sadu testů pro funkci `add()`.

## Úkol 2

Rozšiřte program `calculator.py` o další funkce, aby se jednalo o dobře vychovanou kalkulačku. Pro každou funkci vytvořte sadu testů.

## Úkol 3

Vytvořte testy pro funkci `gsd()`

## Úkol 4

Vytvořte testy pro funkci `is_in_array()`

## Úkol 5

Vytvořte testy pro funkci `is_prime_number()`

# Proces vývoje softwaru

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
