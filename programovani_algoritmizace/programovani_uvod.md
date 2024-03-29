# PYTHON

## Přehled

1. [Co je Python?](#co-je-python)
2. [Instalace Pythonu](#instalace-pythonu)
3. [Změna interpreteru ve VS code](#změna-interpreteru-ve-vs-code)
4. [Instalace knihoven pomocí pip](#instalace-knihoven-pomocí-pip)
5. [VS code](#vs-code)
6. [Vypisování](#vypisování)
7. [Proměnná](#proměnná)
8. [Kreslení](#kreslení)
9. [Podprogramy](#podprogramy)
10. [Náhoda](#náhoda)
11. [Opakování](#opakování)
12. [Větvení](#větvení)
13. [Podprogramy s parametrem](#podprogramy-s-parametrem)
14. [Listy (seznamy)](#listy-seznamy)

## Co je Python?

Python je populární programovací jazyk, který vytvořil Guido van Rossum v roce 1991.

Kde se Používá?

- vývoj webových stránek (server-side)
- vývoj softwaru
- datovou analýzu a vizualizaci
- matematické výpočty
- systémové skriptování

Proč právě Python?

- multiplatformní (Windows, Mac, Linux, Raspberry Pi atd.)
- jednoduchá syntaxe
- kratší programy oproti ostatním jazykům
- lze pracovat procedurálním způsobem, objektově orientovaným způsobem nebo funkcionálním způsobem.

## Instalace Pythonu

Abychom mohli psát programy v pythonu, je potřeba nainstalovat interpreter pro python. Instalační balíček stáhněte [zde](https://www.python.org/downloads/) kliknutím na žluté tlačítko _Download python_. Pokud používáte jiný operační systém než windows, tak vyberte z dalších nabízených možností.

![download python](../images/download_python.png)

Stažený instalátor dvojklikem spusť (bude ve stažených souborech).

![python interpreter](../images/python_interpreter.png)

Na začátku instalace zaškrtni `Add python.exe to PATH`. Možnost `Use admin privileges when installing py.exe` nechte nezaškrtnutou.

![installation](../images/instalation.png)

Poté klikněte na _Install Now_. Poté, co instalace doběhne, okno zavřete.

## Změna interpreteru ve VS code

Pokud jste nainstalovali novou verzi pythonu (viz předchozí kapitola _Instalace Pythonu_) a potřebujete ve VS Code nastavit nový interpreter postupujte následovně:

 1. Pokud máte otevřené VS code, tak ho zavřete
 2. Otevřete VS code
 3. Zmáčkněte kombinaci kláves `ctrl`+`shift`+`P`
 4. Do textového pole napište `Python: Select Interpreter` a zmáčkněte `enter`
5. Vyberte verzi pythonu (`Python 3.12.1 64-bit`)
 
![installation](../images/select-interpreter.png)

![installation](../images/select-version.png)

## Instalace knihoven pomocí pip

Pokud potřebujete doinstalovat novou knihovnu pomocí pip, postupujte následovně:

1. Nainstalujte `pip`. Pokud máte nainstalovanou nejnovější verzi Pythonu, tak nemusíte `pip` instalovat.
2. Otevřete ve VS code nový terminál (v horním menu klikněte _Terminal_ a vyberte _New Terminal_).
3. Do terminálu napište `pip install ` a název knihovny, kterou chcete nainstalovat např. `pip install pygame` a zmáčkněte `enter`.

![installation](../images/new-terminal.png)

![installation](../images/pip-install.png)


## VS code

Pro psaní programu budeme používat Visual Studio Code (VS code), které nainstalujte do počítače z [oficiálních stránek](https://code.visualstudio.com/).

V momentě kdy máte nainstalované VS code, je vhodné nainstalovat ještě rozšíření ve VS code. V sekci `extension` vyhledejte `python` a vyberte první možnost (viz obrázek):

![vs code extension](../images/vscodeextension.png)

Rozšíření není nutnou podmínkou, aby programy fungovaly, ale usnadní vám psaní kódu (vs code vám díky rozšíření bude napovídat) a zároveň usnadní spouštění programů.

Všechny programy, které budeme vytvářet, budou obyčejné soubory s koncovkou `.py` (př. `mujprogram.py`). Pro přehlednost Budeme všechny soubory (programy) ukládat do jedné složky. Vytvořte si v počítači složku a libovolně ji pojmenujte. Následně otevřete VS code. V horním menu klikněte na _File_ a vyberte možnost _Open folder_. V průzkumníku najděte svou složku, jednou na ni klikněte a klikněte na tlačítko _Vybrat složku_. V levém menu nyní vidíte vaši prázdnou složku (na obrázku níže vidíte otevřenou složku _programy_).

![new file](../images/open-folder.png)

Nový soubor vytvoříte tak, že najedete myší vedle názvu složky, objeví se ikonky a kliknete na možnost _New File_. V tu chvíli se objeví textové pole, do kterého napíšete název souboru, tečku a koncovku (př. `prvni.py`).

![new file](../images/new-file.png)

Do souboru můžeme začít psát program. Program lze spustit tlačítkem `run python file` v pravém horním rohu.

## Vypisování

### Úkol 1

Zkusme napsat první program:

```python
print(1 + 2 + 3)
```

`print` je [funkce](#podprogramy) (funkcím se budeme věnovat později). To, co napíšeme do závorek se vypíše do konzole.

### Úkol 2

Python dokáže fungovat jako kalkulačka. Jaké budou výsledky následujících výrazů?

```python
print(123)
print(42 - 17)
print(3 + 4 * 5)
print((3 + 4) * 5)
print(132 / 11)
print(1 + 2 * 3 / (5 - 1))
```

> 2 \* 2 \* 2 \* 2 \* 2 \* 2 \* 2 \* 2 \* 2 \* 2 neboli umocnění 2 na 10 se v Pythonu zapisuje jako `2 ** 10`

### Úkol 3

Pozor, zápisy musí být správně, jinak se objeví chyba. Co se
stane, pokud zadáš následující příkazy?

```python
print(22 + 7 *)
print(19 - (3 4))
```

### Úkol 4

Někdy se však i po správném zápise může objevit chybové hlášení. Co se stane, pokud zadáš následující příkaz?

```python
print(10 / (6 - 2 * 3))
```

### Úkol 5

Petrovi bylo přesně před dvěma měsíci 16 let. Využij Python jako kalkulačku a spočítej:

1. Kolik je mu nyní přibližně dní?
2. Kolik je to hodin?
3. Kolik je to sekund?

Předpokládej, že rok má 365 dní a měsíc má 30 dní.

[řešení](./reseni/vypisovani/5_ukol.md)

### Úkol 6

Zjisti, co Python vypíše v případě následujících příkazů:

```python
print(1 + 2 * 3)
print("1 + 2 * 3")
print()
```

Příkaz `print` slouží na vypisování textů. Text, který se má vypsat, napíšeš mezi uvozovky.

### Úkol 7

Příkaz `print` umí vypsat víc věcí – vyzkoušej následující příkazy. Co způsobí čárka v jednotlivých příkazech?

```python
print("Mám rád", "kapustu")
print("Moje oblíbené číslo je", 42)
print("Do školy jsem šel", 2 * 10, "minut")
```

## Proměnná

V matematice je zvykem označovat hodnoty písmeny, například délka strany čtverce $a = 100$ nebo poloměr kruhu $r=4$. To samé můžeš udělat i v Pythonu.

### Úkol 1

Zkus napsat následující program:

```python
a = 100
```

Nic se nestalo (to je správně!). Python si vytvořil _proměnnou_ s _názvem_ `a` a přitom si zapamatoval, že má _hodnotu_ 100.

Lze si to představit jako krabičku. Text na krabičce je _název_ proměnné, zatímco to, co dáme dovnitř krabičky je _hodnota_ proměnné:

![variable as box](../images/variableasbox.jpg)

### Úkol 2

Zkusme nyní vypsat proměnnou `a`:

```python
a = 100
print(a)
```

Vypíše se hodnota uložená v proměnné.

### Úkol 3

Proměnných můžeme vytvořit, kolik budeme chtít a později je používat v dalších výpočtech. Vyzkoušej vytvořit a nastavit dvě proměnné `vyska` a `hmostnost`, do kterých ulož svou výšku a hmostnost. Pomocí příkazu `print` zkontroluj, jaké hodnoty se do proměnných uložily.

[řešení](./reseni/promenne/3_ukol.md)
### Úkol 4

Co se stane, když bychom chtěli vypsat proměnnou `bmi`, kterou jsme zatím nedefinovali?

```python
print(bmi)
```

### Úkol 5

Proměnné můžeš použít i v matematických zápisech a Python namísto názvu proměnné dosadí její hodnotu. Vytvoř proměnnou `bmi` a ulož do ní tvou hodnotu BMI. Pro výpočet BMI použij proměnné `vyska` a `hmotnost` ze cvičení 3.

[řešení](./reseni/promenne/5_ukol.md)
### Úkol 6

Proměnným můžeme změnit jejich obsah – vyzkoušej:

```python
hmotnost = 70
hmotnost = 73
print(hmotnost)
```

### Úkol 7

Přiřaď do proměnné `zmrzlina` cenu jedné zmrzliny (například 25 korun). Do proměnné `pocet` přiraď počet kamarádů, kterým chceš koupit po jedné zmrzlině. Za použití proměnných sestav přiřazovací příkaz, pomocí kterého se do třetí proměnné `zaplatit` přiřadí celková cena, kterou zaplatíš. Výsledek vypiš následujícím způsobem:

```
Koupil jsem 4 x zmrzlinu a zaplatil jsem 100 korun.
```
[řešení](./reseni/promenne/7_ukol.md)

### Úkol 8

V matematice značíme obsah kruhu $S$ a počítáme jej podle vzorce $\pi  r^2$. Obvod kruhu značíme $O$ a počítáme jej podle vzorce $2 \pi  r$. Vytvoř proměnné pro `poloměr`, `obsah` i `obvod` kruhu a přiřaď do nich správné výrazy. Vytvoř si proměnnou `pi` s hodnotou $3.14$. Výsledek vypiš následujícím způsobem:

```
Kruh s poloměrem 4 má obvod 25.12 a obsah 50.24
```

[řešení](./reseni/promenne/8_ukol.md)


### Úkol 9

Představ si, že bych chtěl použít program pro kruh s poloměrem 73. Změn hodnotu v proměnné `polomer` a spusť program. Zobrazí se ve výpisu správný výsledek? Jestli ne, program oprav.

### Úkol 10

Vyzkoušej, které z následujících názvu lze použít jako název proměnné:

- kuk
- Ahoj!
- 1.A
- prvni_trida
- cerno-bile
- OK
- o0o0o0o
- asdf
- věk
- počet osob
- trida(3)

## Kreslení

Doposud programy počítaly a vypisovaly textové zprávy. Nyní zkusíme kreslit obrázky. Postupuj takto:

1. Vytvoř následující program:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
input()
```

2. Program spusť – na obrazovce uvidíš nové okno.
3. Zjisti, zda se dá okno posouvat, měnit jeho velikost. Nakonec toto nové okno zavři. program vyrobil grafickou plochu `canvas`.

> `input()` na konci nemá s oknem nic společného. Jedná se o příkaz, který čeká, až mu uživatel do konzole napíše nějaký vstup. Kdyby tam příkaz nebyl, tak by program ihned skončil a okno by se ihned po otevření zavřelo. V následujících příkladech proto vždy nakonec programu napište `input()`, aby okno zůstalo otevřené.

### Úkol 1

Přidej do programu nový příkaz:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 70, 220, 150)

input()
```

příkaz vykreslí obdelník.

> Příkaz `input()` musí být pořád na konci programu

### Úkol 2

V závorkách příkazu `canvas.create_rectangle( , , , )` jsou 4 čísla. Zkus je postupně měnit. Program pokaždé spusť, abys viděl, co nakreslí:

```python
canvas.create_rectangle(0, 0, 220, 150)
canvas.create_rectangle(0, 0, 50, 50)
canvas.create_rectangle(0, 0, 250, 50)
canvas.create_rectangle(20, 10, 250, 50)
canvas.create_rectangle(20, 10, 50, 250)
```

### Jak fungují souřadnice v tkinteru

Souřadnice fungují v tkinter trochu netradičně:

![coordinates](../images/souradnice-konkretne.png)

V matematice jsme zvyklí, že střed je "uprostřed". Zde ale leží bod se souřadnicemi $[0, 0]$ v levém horním rohu. Čísla na ose $x$ se zleva doprava. zvětšují. Čísla na ose $y$ se zvětšují shora dolů (čím větší číslo, tím níže).

V příkazu `canvas.create_rectangle(x1, y1, x2, y2)` píšeme do závorek souřadnice protilehlých vrcholů obdélníku:

![rectangle](../images/souradnice-obecne.png)

### Úkol 3

Nakresli obdélník, který má souřadnice
protilehlých vrcholů $[50, 30]$ a $[300, 200]$.

[řešení](./reseni/kresleni/3_ukol.md)

### Úkol 4

Nakresli obdélník, který má levý horní vrchol na souřadnicích $[200, 100]$, jeho šířka je 60 a výška 140.

[řešení](./reseni/kresleni/4_ukol.md)

### Úkol 5

Nakresli dva čtverce se stranami délky 80. První čtverec bude mít levý horní roh na souřadnicích $[10, 20]$ a druhý na souřadnicích $[150, 120]$

[řešení](./reseni/kresleni/5_ukol.md)

### Úkol 6

Obdélník lze i vybarvit:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(30, 30, 130, 130, fill='red')
input()
```

### Úkol 7

Vytvoř program, který nakreslí 4 čtverce se stranou délky 50. Každý čtverec bude mít jinou barvu. Umístění čtverců zvol podle sebe.

[řešení](./reseni/kresleni/7_ukol.md)

### Úkol 8

V proměnných `x`, `y` jsou uložené souřadnice levého horního rohu čtverce. Dokonči kód programu tak, abys pomocí uvedených proměnných nakreslil čtverec se stranou délky
100:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 70
canvas.create_rectangle(x, y, ... , ... , fill='yellow')
input()
```

[řešení](./reseni/kresleni/8_ukol.md)

### Úkol 9

Vytvoř program, který použije čtyři proměnné `x`, `y`, `sirka`, `vyska` a na jejich základě nakreslí obdélník s levým horním rohem na souřadnicích `x`, `y`, danou šířkou a výškou. Barvu si zvol podle svého.

[řešení](./reseni/kresleni/9_ukol.md)

### Úkol 10

Vytvoř program, který nakreslí následující čtverce:

![three squares](../images/threesquares.png)

Tyto čtverce mají společný levý horní roh, jehož souřadnice jsou v proměnných `x`, `y`. Čtverce se postupně zmenšují tak, že červený má délku strany 100, modrý 70 a tmavomodrý 40.

[řešení](./reseni/kresleni/10_ukol.md)

## Podprogramy

Doposud jsme používali jen takové příkazy, které počítač znal (`print`, `create_rectangle`, `Canvas`). Nyní budeme vytvářet své vlastní příkazy – tzv. podprogramy (též funkce).

### Úkol 1

Jak vytvořit vlastní podprogram?

1. Opiš následující kód:

```python
def vypis_text():
    print('************')
    print('** Python **')
    print('************')
```

2. Program spusť – pokud se do konzole nic nevypsalo, je to v pořádku.
3. Vlož ještě příkaz `vypis_text()`:

```python
def vypis_text():
    print('************')
    print('** Python **')
    print('************')

vypis_text()
```

4. Pokud nyní program spustíš, vypíše se text.

Slovem `def` začíná definice tvého nového příkazu – podprogramu. `vypiš_text` je název podprogramu (podobně jako `print` je název pro podprogram, který vypisuje text). Tři příkazy `print` se nazývají tělo podprogramu.

Po spuštění programu se počítač naučil nový příkaz `vypis_text`. Počítač ho zatím
nevykonal, jen se ho naučil. Skupinu příkazů `print` – tedy tělo podprogramu `vypis_text` – počítač vykoná až tehdy, když narazí na příkaz `vypis_text()`. Takovýto zápis se nazývá volání podprogramu.

### Úkol 2

Přidej do programu další příkazy – pozor, tyto příkazy nesmí být odsazené (nesmí být před nimi žádná mezera, musí být hned na začátku řádku), protože už nepatří do podprogramu:

```python
def vypis_text():
    print('************')
    print('** Python **')
    print('************')

print('Vítej!')
vypis_text()
print()
vypis_text()
print('to je konec')
```

V tomto programu se nejdříve definoval podprogram `vypis_text`. Za ním následují příkazy `print` a příkazy pro volání podprogramu `vypis_text`. Python zobrazil svoji vizitku dvakrát, protože v programu jsou dvě volání podprogramu `vypis_text`. Podprogram tedy můžeme volat i vícekrát.

### Úkol 3

Změň předchozí program tak, aby počítač vypsal:

```
Vítej!
*****************
** I am Python **
*****************
Jak se máš?
*****************
** I am Python **
*****************
Mám se dobře.
*****************
** I am Python **
*****************
to je konec
```

[řešení](./reseni/podprogramy/3_ukol.md)

### Úkol 4

Vytvoř nový program, který bude obsahovat následující kód:

```python
refren()
refren()
print()
print('když já jím dám ovsa')
print('oni skáčou hopsa')
print()
refren()
refren()
def refren():
    print('já mám koně vraný koně')
    print('to jsou koně mí')
```

Když program spustíš, Python vypíše chybové hlášení. Python tím říká, že na 1. řádku programu není možné volat podprogram `refren`, protože tento podprogram ještě nebyl definován. Uprav program tak, aby se úryvek písně vypsal správně.

[řešení](./reseni/podprogramy/4_ukol.md)

### Úkol 5

Ve svém programu můžeš definovat i více podprogramů. Vytvoř nový program a definuj v něm tři podprogramy. Každý z nich zobrazí jeden z následujících obrázků:

- podprogram `noha` nakreslí takovouto nohu (dole jsou dvě podtržítka vlevo i vpravo):

```
  |
__|__
```

- podprogram `obdelnik` nakreslí takovýto obdélník:

```
#####
#   #
#####
```

- podprogram `trojuhelník` nakreslí takovýto trojúhelník:

```
  *
 ***
*****
```

Potom zkus pomocí vytvořených podprogramů zobrazit následující obrázky:

```
  *
 ***
*****
  *
 ***
*****
  |
__|__
```

```
  *
 ***
*****
#####
#   #
#####
  |
__|__
```

```
#####
#   #
#####
  |
__|__
#####
#   #
#####
```

```
toto je noha:
  |
__|__

toto je obdélník:
#####
#   #
#####

toto je trojúhelník:
  *
 ***
*****
```

[řešení](./reseni/podprogramy/5_ukol.md)

### Úkol 6

Vytvoř nový program a vyzkoušej následující kód:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def kresli():
    canvas.create_rectangle(10, 20, 30, 40, fill='red')
kresli()

input()
```

### Úkol 7

Vytvoř dva podprogramy. První pojmenuj _maly_ctverec_ a druhý pojmenuj _velky_ctverec_. První podprogram vykreslí na souřadnicicích $[10, 20]$ čtverec se stranou délky 20. Druhý podprogram vykreslí čtverec na souřadnicích $[40, 40]$ se stranou délky 80. Pomocí zavolání obou programů vykreslete do jednoho plátna oba čtverce.

[řešení](./reseni/podprogramy/7_ukol.md)

## Náhoda

### Úkol 1

Zkus spustit následující program:

```python
import random
print(random.randint(1, 6))
```

Program vypíše náhodné číslo od 1 do 6.

### Úkol 2

Náhodné číslo si můžeš zapamatovat – napiš program s následujícím kódem a spusť jej (i vícekrát):

```python
import random
n = random.randint(1, 6)
print('Na kostce padla', n)
```

### Úkol 3

Uprav program z úkolu 2 – vytvoř podprogram `hod_kostkou`. Pomocí volání tohoto podprogramu nasimuluj pět hodů za sebou.

[řešení](./reseni/nahoda/3_ukol.md)

### Úkol 4

Uprav program z úkolu 3, aby počítač simuloval dva hody na dvacetistěnné kostce.

[řešení](./reseni/nahoda/4_ukol.md)

### Úkol 5\*

Máme _sudou_ hrací kostku, která má na stěnách čísla 2, 4, 6, 8, 10, 12. Uprav program z úkolu 3, aby simuloval hod takovou kostkou.

[řešení](./reseni/nahoda/5_ukol.md)

### Úkol 6\*

Máme _lichou_ hrací kostku, která má na stěnách čísla 1, 3, 5, 7, 9, 11. Uprav předchozí program, aby simuloval hod takovou kostkou.

[řešení](./reseni/nahoda/6_ukol.md)

### Úkol 7\*

Máme _exotickou_ hrací kostku, která má na stěnách čísla 1, 4, 9, 16, 25, 36. Uprav předchozí program, aby simuloval hod takovou kostkou.

[řešení](./reseni/nahoda/7_ukol.md)

### Úkol 8

Vytvoř program, který vygeneruje náhodný PIN pro tvůj mobil. Do čtyř proměnných `a`, `b`, `c`, `d` přiřaď náhodná čísla od 0 po 9 a potom je jediným příkazem
`print` vypiš. Výpis může vypadat například takto:

```
Tvůj nový PIN je 1 3 7 3
```
[řešení](./reseni/nahoda/8_ukol.md)

### Úkol 9

Vytvoř nový program – generátor náhodných dat (pro jednoduchost nechť má každý měsíc 30 dní). Po spuštění program vypíše informaci s vygenerovaným náhodným datem, například:

```
Pokoj si uklidím 30 . 2 . 2025
```

[řešení](./reseni/nahoda/9_ukol.md)
### Úkol 10

Vytvoř podprogram _nahodny_ctverec_, který vykreslí čtverec na náhodné pozici (souřadnice jednoho rohu budou náhodně vygenerované čísla). Čtverec bude mít stranu délky 50.

[řešení](./reseni/nahoda/10_ukol.md)
### Úkol 11

Doplň do předchozího programu příkazy tak, aby program nakreslil pět náhodných čtverců.

[řešení](./reseni/nahoda/11_ukol.md)
### Úkol 12

Uprav předchozí program tak, aby se čtverce kreslily nejen na náhodných pozicích, ale také aby měl každý čtverec náhodnou velikost z intervalu od 10 do 100.

[řešení](./reseni/nahoda/12_ukol.md)
## Opakování

### Úkol 1

Vytvoř program, který pomocí příkazu `print` vypíše text _Těším se na prázdniny_ pětkrát pod sebe.

[řešení](./reseni/opakovani/1_ukol.md)

### Úkol 2

V předchozím programu jsi měl vícekrát nakopírované příkazy `print()`. Abys je nemusel opakovaně kopírovat, můžeš to zapsat jednodušeji. Uprav kód programu z úkolu 1 následovně:

```python
for i in range(5):
    print('Těším se na prázdniny')
```

Zkus místo čísla 5 dát číslo 10 a program znovu spusť. Urči, co je tímto číslem ovlivňováno.

### Úkol 3

Uprav program stejně, jako je uvedeno níže, a spusť jej:

```python
for i in range(5):
    print('Těším se na prázdniny')
    print('=====================')
```

Slovem `for` začíná příkaz cyklu. Pětka v závorce udává počet zopakování. Dva příkazy `print` tvoří tělo cyklu (tělo známe již z podprogramů). Příkazy v těle cyklu se vykonají 5x.

### Úkol 4

Je důležité odsadit od kraje příkazy, které tvoří tělo cyklu. Vyzkoušej, co vypíše takto upravený program:

```python
for i in range(5):
    print('Těším se na prázdniny')
print('=====================')
```

### Úkol 5

Vytvoř nový program a v něm podprogram `cerveny_ctverec()`. Ten nakreslí na grafickou plochu na náhodné souřadnice červený čtverec se stranou délky 10. Použij `for` cyklus na to, abys nakreslil 2000 červených čtverců.

[řešení](./reseni/opakovani/5_ukol.md)

### Úkol 6

Doplň do předchozího programu podprogram `modry_ctverec()`. Tento podprogram bude kreslit na náhodné souřadnice modrý čtverec se stranou délky 10. Zajisti, aby tělo cyklu obsahovalo volání podprogramu `cerveny_ctverec()` i podprogramu `modry_ctverec()`. Výsledek může vypadat
například jako na následujícím obrázku:

![thousand](../images/thousandsquares.png)

[řešení](./reseni/opakovani/6_ukol.md)

### Úkol 7

Vytvoř nový program, který nakreslí hvězdnou
oblohu:

![night sky](../images/nightsky.png)

Návod:

- Napiš podprogram `hvezda`, který nakreslí na náhodnou pozici malý žlutý čtvereček. Velikost jeho strany bude náhodné číslo z rozsahu od 2 do 4
- Tmavomodrou oblohu nakresli jako velký obdélník s barvou _navy_
- Potom zavolej tisíckrát podprogram `hvezda`

[řešení](./reseni/opakovani/7_ukol.md)

### Úkol 8

Napiš program, který simuluje hody dvěma kostkami. Zapiš pomocí `for` cyklu pět hodů, kdy se v těle cyklu do dvou proměnných přiřadí dvě náhodná čísla, ta se vypíšou a vypíše se i jejich součet. Výpis může vypadat například takto:

```
Na první kostce padlo číslo 4
Na druhé kostce padlo číslo 3
Součet obou čísel je 7

Na první kostce padlo číslo 2
Na druhé kostce padlo číslo 4
Součet obou čísel je 6

Na první kostce padlo číslo 5
Na druhé kostce padlo číslo 2
Součet obou čísel je 7

Na první kostce padlo číslo 3
Na druhé kostce padlo číslo 1
Součet obou čísel je 4

Na první kostce padlo číslo 1
Na druhé kostce padlo číslo 4
Součet obou čísel je 5
```

[řešení](./reseni/opakovani/8_ukol.md)

### Úkol 9\*

Vytvoř nový program, který bude představovat generátor náhodného QR kódu a který bude schopen generovat podobný QR kód jako na obrázku níže:

![qr code](../images/qrcode.png)

Obrázek se skládá z velkého počtu černých čtverečků. Každý má délku strany 10 a je nakreslený v jednom náhodně vybraném políčku mřížky, která obsahuje 21x21 políček.

[řešení](./reseni/opakovani/9_ukol.md)

### Úkol 10

Vytvoř program a pomocí následujícího kódu vypiš celá čísla od 0 do 9:

```python
for i in range(10):
    print('číslo', i)
```

Jak to funguje? `i` je proměnná, do které příkaz `for` postupně přiřazuje celá čísla od 0 do 9.

### Úkol 11

Vytvoř program, který pomocí `for` cyklu vypíše čísla a jejich druhé mocniny:

```
0 na druhou je 0
1 na druhou je 1
2 na druhou je 4
3 na druhou je 9
4 na druhou je 16
5 na druhou je 25
6 na druhou je 36
```

[řešení](./reseni/opakovani/11_ukol.md)

### Úkol 12

Urči, co je potřeba v předchozím programu změnit, aby se vypsala čísla:

1. 0, 1, ... 10 – tedy i číslo 10
2. 1, 2, ... 10
3. 2, 4, ... 20
4. 10, 20, ... 100
5. 10, 9, ... 1

[řešení](./reseni/opakovani/12_ukol.md)

### Úkol 13\*

Vytvoř program a v něm pomocí cyklu nakresli devět čtverců s délkou strany 30. Mezi čtverci bude mezera o velikosti 10. Použij proměnnou `x`, ve které bude uložena x-ová souřadnice levého horního rohu kresleného čtverce. Hodnota této proměnné bude v cyklu zvýšena pokaždé o 40.

![square row](../images/squarerow.png)

[řešení](./reseni/opakovani/13_ukol.md)

### Úkol 14

Existuje pověst o králi, který slíbil mudrcovi za odměnu tolik zrnek rýže, kolik jich bude na všech políčkách šachovnice? Král mudrcovi dovolil, aby na první políčko dal 10 zrnek, na druhé 20, na třetí 30 atd. Kolik by mudrc dostal zrnek rýže? Políček na šachovnici je 64. Druhá varianta této pověsti hovoří o tom, že král dovolil mudrci položit na každé políčko dvakrát více rýže než na předešlé políčko, kolik zrnek by dostal v tomto případě?

[řešení](./reseni/opakovani/14_ukol.md)

## Větvení

### Úkol 1

Počítač dokáže porovnávat dvě hodnoty (čísla):

```python
print(1 < 2)    # program vypíš true
print(4 < 2)    # program vypíš false

print(4 > 2 + 1)
print(1 == 1)
print(1 == 2)
print(0 != 2)
print(0 != 0)

x = 100
print(x == 10 * 10)
print(x != 10 * 10 + 1)
```

Znaménka větší/menší (`>` a `<`) známe z matematiky. Rovnost se zapisuje v pythonu jako `==` a nerovnost jako `!=`.

### Úkol 2

Vytvoříme program, který nám řekne, zda je teplo nebo zima. Do proměnné `teplota` přiřadíme číslo. Počítač pro teplotu větší než 20 stupňů vypíše, že je teplo. Jinak řekne, že je zima:

```python
teplota = 25
if teplota > 20:
    print('Dnes je teplo.')
else:
    print('Dnes je zima.')
```

`if ... else ...` je příkaz pro větvení programu. `teplota > 20` je podmínka, podle které se počítač rozhodne, kterou větev dále vykoná. `print('Dnes je teplo.')` je větev `if`. `print('Dnes je zima.')` je větev `else`.

Když počítač uvidí příkaz `if ... else ...`, nejdříve vyhodnotí podmínku. Když je podmínka splněná, vykoná se příkaz ve větvi `if`, jinak se vykoná příkaz ve větvi `else`.

Zkus měnit hodnoty v proměnné teplota tak, aby se program dostal i do větve `else`.

### Úkol 3

Uprav předchozí program tak, aby pro:

- záporné teploty vypsal _Venku je ... stupňů, vezmi si rukavice_,
- jinak vypíše _Venku je ... stupňů, rukavice nejsou potřeba_.

Ověř, že program funguje správně pro kladné i záporné hodnoty. Co tvůj program vypíše pro 0?

[řešení](./reseni/vetveni/3_ukol.md)

### Úkol 4

Vytvoř program, který určí cenu dopisu. Na začátku programu přiřaď do proměnné `hmotnost` číslo s hmotností dopisu. Použij příkaz pro větvení programu, aby pro dopis s hmotností:

- větší než 50 vypsal _Zaplatíš 55 korun_
- jinak vypíše _Zaplatíš 47 korun_

Ověř, že program počítá správně cenu dopisu pro hmotnosti: 30, 50 a 100.

[řešení](./reseni/vetveni/4_ukol.md)

### Úkol 5

Vytvoř program, ve kterém do proměnných `a`, `b` přiřaď délky stran útvaru, u nějž nevíme, zda je to obdélník nebo čtverec. Napiš kód, který určí a vypíše, zda je daný útvar obdélníkem nebo čtvercem.

[řešení](./reseni/vetveni/5_ukol.md)

### Úkol 6

Délky stran obdélníku jsou uložené v proměnných `a`, `b`. Vytvoř program, který nakreslí obdélník tak, aby vždy ležel delší stranou na zemi:

![rectangles](../images/rectangleonlongside.png)

[řešení](./reseni/vetveni/6_ukol.md)

### Úkol 7

Vytvořte program, který pomocí cyklu a příkazu větvení vypíše pro:

- čísla menší než 7 _Číslo ... je menší než 7_
- ostatní čísla (až do čísla 20) _Číslo ... je větší nebo rovno 7_

[řešení](./reseni/vetveni/7_ukol.md)

### Úkol 8

Házíme desetkrát hrací kostkou a chceme vědět, kolikrát padla šestka a kolikrát jiné číslo.
Vytvoř program, který pomocí cyklu, generování náhodných čísel a příkazu větvení simuluje deset hodů kostkou, hozená čísla vypíše a spočítá, kolikrát padla šestka a kolikrát jiné číslo. Tyto počty poté vypíše. Spuštění může například vypadat takto:

```
5
6
5
2
2
3
1
4
5
3
Padlo 1 šestek a 9 jiných čísel
```

[řešení](./reseni/vetveni/8_ukol.md)

### Úkol 9\*

Hrajeme hru, ve které házíme desetkrát kostkou a získáváme prémii vždy, když za sebou
padnou dvě stejná čísla. Vytvoř program, který simuluje deset hodů kostkou, hozená čísla vypíše a spočítá počet prémií. Tento počet prémií potom vypíše. Spuštění může například vypadat takto:

```
4
4
6
5
3
3
3
1
5
5
Počet prémií: 4
```

[řešení](./reseni/vetveni/9_ukol.md)

### Úkol 10

Systém vypisuje jestli má člověk nárok na slevu podle následjících pravidel:

- když má člověk méně než 15 let, má nárok na dětskou slevu
- když má člověk více než 65 let, má nárok na seniorskou slevu
- jinak nemá nárok na slevu

V této úloze je více podmínek. Prohlédni si následující řešení:

```python
vek = 13
if vek < 15:
    print('Dětská sleva')
else:
    if vek > 65:
        print('Seniorská sleva')
    else:
        print('Není nárok na slevu')
```

Co program vypíše pro hodnoty 5, 15, 23, 89, 65, -1?

### Úkol 11

Aby byl program přehlednější, existuje v pythonu ještě příkaz `elif`:

```python
vek = 13
if vek < 15:
    print('Dětská sleva')
elif vek > 65:
    print('Seniorská sleva')
else:
    print('Není nárok na slevu')
```

Rozšiř program, aby pro lidi od 15 do 26 let vypsal _Studentská sleva_

[řešení](./reseni/vetveni/11_ukol.md)

### Úkol 12

Chceš porovnat svůj věk s věkem kamarádky. Vytvoř program, ve kterém do proměnných `ja` a `ona` přiřadíš svůj věk a věk tvé kamarádky. Program tyto údaje porovná a podle toho vypíše: _Jsme stejně staří_, _Jsem mladší_ nebo _Ona je mladší_.

[řešení](./reseni/vetveni/12_ukol.md)

### Úkol 13

Vytvoř program, ve kterém budeš kreslit na plátno
německou vlajku. Tu budeš vytvářet tak, že pomocí cyklu vygeneruješ 10 000x náhodné
souřadnice $x$, $y$. Souřadnice $x$ bude z intervalu od 10 do 350 a souřadnice $y$ bude z intervalu od 10 do 250. Na tyto souřadnice $[x, y]$ nakreslíš barevný obdélník se stranou délky 5. Barvu obdélníku zvolíš podle $y$-ové souřadnice následovně:

- když je $y$ < 90, nakreslíš černý obdélník,
- jinak, když je $y$ < 170, nakreslíš červený obdélník,
- jinak nakreslíš žlutý obdélník.

Výsledek by měl vypadat podobně jako na obrázku níže:

![german](../images/german.png)

[řešení](./reseni/vetveni/13_ukol.md)

### Úkol 14\*

Vytvoř program, který podobnou technikou, jako byla použita v předchozí úloze, nakreslí obrázek podobný české vlajce. Výsledek může vypadat například takto:

![czech](../images/czech.png)

[řešení](./reseni/vetveni/14_ukol.md)

## Podprogramy s parametrem

### Úkol 1

Vytvoř tři podprogramy. Podprogram `velkyCtverec` vykreslí čtverec s levým horním vrcholem na souřadnicích $[50, 60]$ a délkou strany 100. Podprogram `stredniCtverec` vykreslí čtverec s levým horním vrcholem na souřadnicích $[50, 60]$ a délkou strany 70. Podprogram `malyCtverec` vykreslí čtverec s levým horním vrcholem na souřadnicích $[50, 60]$ a délkou strany 40. Podprogramy poté zavolej, aby se všechny tři čtverce vykreslily do jednoho okna.

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def velkyCtverec():
    canvas.create_rectangle(............, ............, ............, ............)
def stredniCtverec():
    canvas.create_rectangle(............, ............, ............, ............)
def malyCtverec():
    canvas.create_rectangle(............, ............, ............, ............)

input()
```

[řešení](./reseni/podprogramy_s_parametrem/1_ukol.md)

### Úkol 2

Předchozí řešení se dá zapsat pomocí jediného podprogramu:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def ctverec(strana):
    canvas.create_rectangle(50, 60, 50 + strana, 60 + strana)

ctverec(100)
ctverec(70)
ctverec(40)

input()
```

V závorce je název parametru `strana`. Ve funkci `create_rectangle` se parametr používá. Parametr funguje jako proměnná. Při volání podprogramu se do parametru `strana` přiřadí hodnota.

### Úkol 3

Dokonči následující podprogram `vypis`, který používá parametr `x` na to, aby vypsal hodnotu parametru `x` a jeho druhou mocninu:

```python
def vypis(x):
    print('Číslo', ...)
    print('Umocněné na druhou se rovná', ...)

vypis(1)
vypis(2)
vypis(3)
```

[řešení](./reseni/podprogramy_s_parametrem/3_ukol.md)

### Úkol 4

Doplň do předchozího podprogramu příkaz, kterým se vypíše i převrácená hodnota `x`. Připomeňme, že převrácená hodnota čísla $x$ je rovna $\frac{1}{x}$. Program by měl po spuštění vypsat:

```
Číslo 1
Umocněné na druhou se rovná 1
Převrácená hodnota se rovná 1.0
Číslo 2
Umocněné na druhou se rovná 4
Převrácená hodnota se rovná 0.5
Číslo 3
Umocněné na druhou se rovná 9
Převrácená hodnota se rovná 0.3333333333333333
```

[řešení](./reseni/podprogramy_s_parametrem/4_ukol.md)

### Úkol 5

Vytvoř program a v něm definuj podprogram `obliba`
s parametrem `cislo`. Podprogram podle následujících pravidel vypíše, zda má číslo v oblibě:

- když je číslo menší než 7, vypíše: _Mám rád číslo ..._
- jinak vypíše: _Číslo ... se mi nelíbí_

[řešení](./reseni/podprogramy_s_parametrem/5_ukol.md)

### Úkol 6

Uprav předchozí program tak, aby pomocí cyklu zavolal podprogram `obliba` pro čísla od 0 do 10. Výsledek by měl vypadat následovně:

```
Mám rád číslo 0
Mám rád číslo 1
...
Mám rád číslo 6
Číslo 7 se mi nelíbí
...
Číslo 10 se mi nelíbí
```

[řešení](./reseni/podprogramy_s_parametrem/6_ukol.md)

### Úkol 7

Vytvoř podprogram `nahodny_ctverec` s parametrem `a`, který nakreslí na náhodných souřadnicích červený čtverec se stranami délky `a`. Zavolej tento podprogram pro různé hodnoty parametru.

[řešení](./reseni/podprogramy_s_parametrem/7_ukol.md)

### Úkol 8

Vykresli pomocí podprogramu `nahodny_ctverec` z předchozího úkolu 10 čtverců. První bude mít délku strany 1, druhý stranu délky 2, třetí délku strany 3 atd.

[řešení](./reseni/podprogramy_s_parametrem/8_ukol.md)

### Úkol 9

Co se stane, když v podprogramu `nahodny_ctverec` z úkolu 7 nastavím hodnotu parametru na záporné číslo? Uprav program tak, aby vyreslil čtverec pouze pro kladné hodnoty parametru `a`. Pro záporné hodnoty vypíše do konzole zprávu _Nedá se_.

[řešení](./reseni/podprogramy_s_parametrem/9_ukol.md)

## Listy (seznamy)

### Úkol 1

Doposud jsme ukládali do proměnné pouze jednu hodnotu (číslo, text):

```python
cislo = 42
texticek = "muj ukazkovy texticek"
```

Co kdybychom ale chtěli například uložit všechna nejlepší čísla? Buď bychom museli vytvořit několik proměnných a uložit čísla postupně jedno po druhém:

```python
nejlepsi_cislo_1 = 42
nejlepsi_cislo_2 = 73
nejlepsi_cislo_3 = 420
nejlepsi_cislo_4 = 666
```

Nebo je můžeme uložit všechny najednou pomocí seznamu:

```python
nejlepsi_cisla = [42, 73, 420, 666]
```

Zkus proměnnou `nejlepsi_cisla` vypsat pomocí funkce `print()`

### Úkol 2

Zkus spustit postupně spustit oba programy níže. Jaký je rozdíl ve výpisu?

```python
for i in range(5):
    print('číslo', i)
```

```python
for i in [0, 1, 2, 3, 4]:
    print('číslo', i)
```

již víme, že příkaz `for` postupně přiřazuje do proměnné `i` hodnoty 0 až 5. Podobně lze dosazovat do proměnné `i` postupně všechny hodnoty ze seznamu. 


### Úkol 3

Doplň tělo podprogramu `vypis`. V rámci těla podprogramu se vypíšou všechny prvky v seznamu. 

```python
zvirata = ["pes", "kočka", "kůň", "opice", "krokodýl"]

def vypis(seznam):
    # vytvoř tělo podprogramu

vypis(zvirata)
    
```
[řešení](./reseni/listy/3_ukol.md)

### Úkol 4

Napište podprogram `zdvojnasob`, který dostane jako parametr seznam čísel. V rámci těla podprogramu se vypíše dvojnásobek každého čísla v seznamu.

[řešení](./reseni/listy/4_ukol.md)

### Úkol 5

Napište podprogram `eliminace`, který dostane jako parametr seznam čísel. V rámci těla podprogramu se vypíšou pouze ta čísla ze seznamu, která jsou větší než 7.

[řešení](./reseni/listy/5_ukol.md)

### Úkol 6

Napište podprogram `je_v`, který dostane dva parametry - seznam a prvek. Program vypíše "ano", pokud se daný prvek nachází v seznamu.

[řešení](./reseni/listy/6_ukol.md)

### Úkol 7

Napište podprogram `kolik_je_v`, který dostane jako parametr seznam, a který vypíše, kolik je v seznamu prvků.

[řešení](./reseni/listy/7_ukol.md)

### Úkol 8

Napište podprogram `soucet`, který dostane jako parametr seznam čísel a vypíše součet všech čísel v seznamu.

[řešení](./reseni/listy/8_ukol.md)

### Úkol 9

Zatím umíme projít celý seznam pomocí příkazu `for`. Co kdybych chtěl ale vypsat pouze jeden konkrétní prvek ze seznamu? Lze to udělat následovně:

```python
cisla = [44, 53, 92, 18]
print(cisla[2])
```

Každý prvek v seznamu má svůj index (pozici), který udává, kde se prvek v seznamu nachází. Zapisem `cisla[2]` říkáme, že chceme vybrat ze seznamu `cisla` prvek na indexu `2`. Pomocí funkce `print()` tento konkrétní prvek ze seznamu vypíšeme.

> Pozice v seznamu se číslují zleva od 0. První prvek je na pozici 0, druhý prvek na pozici 1, třetí prvek na pozici 2 atd.

Kdybych chtěl tedy vypsat první tři prvky, můžu to udělat takto:

```python
cisla = [44, 53, 92, 18]
print(cisla[0]) 
print(cisla[1])
print(cisla[2])
```


Co se stane, kdybych chtěl vypsat pátý prvek ze seznamu?

![first table](../images/first_table.jpg)

### Úkol 10

Podobně lze změnit prvek v seznamu na konkrétním indexu. Vyzkoušej, co vypíše následující program:

```python
cisla = [2, 6, 3, 4, 5]
print(cisla)

cisla[1] = 40
cisla[2] = 41
cisla[3] = 42
print(cisla)
```

zapisem `cisla[1] = 40` říkáme, že chceme změnit v seznamu `cisla` prvek na indexu `1` a nová hodnota tohoto prvku je `40`.

### Úkol 11
Vytvořte seznam o šesti prvcích, každý prvek bude číslo 0. Následně vytvořte proměnnou `hod`, do které uložte libovolné číslo od 1 do 6. Změňte prvek v seznamu na 1 podle toho, jaké číslo je uložené v proměnné `hod`. Pokud je v proměnné `hod` číslo 1, tak se první prvek (tzn. prvek na pozici 0) v seznamu přepíše na 1. Pokud je v proměnné `hod` číslo 2, tak se druhý prvek (tzn. prvek na pozici 1) v seznamu přepíše na 1 atd. Celý seznam následně vypište (mělo by v něm být pět 0 a jedna 1).
### Úkol 11

Upravte předchozí program tak, aby se do proměnné hod uložilo náhodné číslo od 1 do 6 (tzn. nenastavujte ho ručně, ale vygenerujte náhodné číslo).

<!--  [řešení](./reseni/listy/11_ukol.md) -->

### Úkol 12

Upravte předchozí kód tak, abychom hodnotu na daném indexu nenastavovali na 1, ale pouze zvýšili o jedna.

<!-- [řešení](./reseni/listy/12_ukol.md) -->

### Úkol 13

Upravte předchozí kód tak, abyste nesimulovali pouze jeden hod kostkou, ale 1000 hodů kostkou. Hodnoty postupně navyšujte. Budou výsledná čísla v seznamu přibližně stejná?

<!-- [řešení](./reseni/listy/13_ukol.md) -->

### Úkol 14

Upravte předchozí kód tak, abyste simulovali hod dvěma kostkami. Do seznam ukládejte součet na obou kostkách. Kolik prvků musí mít seznam? Prověďte 10000 hodů. Proč tentokrát nebudou všechny hodnoty v seznamu podobné?

<!-- [řešení](./reseni/listy/14_ukol.md) -->

### Úkol 15\*

Vytvořte podprogram `galtonova_deska`, který bude simulovat Galtonovu desku. Jak deska funguje znázorňuje toto [video](https://www.youtube.com/shorts/jstkPuhLDEw).

Dole je 13 přihrádek. Kuličky padají postupně přes 12 pater. V každém patře se můžou posunout buď o půl pozice doleva nebo o půl pozice doprava. Všechny kuličky začínají nad prostřední přihrádkou. Nakonec každá kulička spadne do jedné ze 13 přihrádek. Kuliček je 1000. Kolik bude nakonec v jednotlivých přihrádkách kuliček.

<!-- [řešení](./reseni/listy/15_ukol.md) -->

### Úkol 16\*

Opilec je na půli cesty mezi domovem a hospodou, každý krok udělá náhodně jedním směrem. Napište funkci, která bude simulovat opilcův pohyb. Jejími parametry budou vzdálenost mezi domovem a hospodou a počet kroků do opilcova usnutí (tj. maximální délka simulace). Simulace skončí buď tehdy, když opilec dojede domů nebo do hospody, případně po vyčerpání počtu kroků.

\*Rozšíření: Vyzkoušejte různé kombinace parametrů. Při jaké konfigurace dochází domů už celkem pravidelně?

Výpis by měl vypadat zhruba následovně:

```
home . . . . . * . . . . pub
home . . . . * . . . . . pub
home . . . * . . . . . . pub
home . . . . * . . . . . pub
home . . . * . . . . . . pub
home . . . . * . . . . . pub
home . . . * . . . . . . pub
home . . * . . . . . . . pub
home . * . . . . . . . . pub
home . . * . . . . . . . pub
home . . . * . . . . . . pub
home . . * . . . . . . . pub
home . . . * . . . . . . pub
home . . * . . . . . . . pub
home . . . * . . . . . . pub
home . . . . * . . . . . pub
home . . . . . * . . . . pub
home . . . . * . . . . . pub
home . . . . . * . . . . pub
home . . . . * . . . . . pub
home . . . . . * . . . . pub
home . . . . . . * . . . pub
home . . . . . * . . . . pub
home . . . . . . * . . . pub
home . . . . . . . * . . pub
home . . . . . . . . * . pub
home . . . . . . . . . * pub
home . . . . . . . . * . pub
home . . . . . . . . . * pub
home . . . . . . . . . . pub
Ended in the pub again!
```
<!-- [řešení](./reseni/listy/16_ukol.md) -->

### Úkol 17\*

Další simulace vhodné k programování naleznete [zde](https://www.fi.muni.cz/IB111/sbirka/04-nahodna_cisla.html#simulace-a-analyzy).

## Další úlohy

## Úkol 1

Dva hrací automaty spolu o dni volna hrály hru, v níž střídavě odebíraly mince z hromádky. 
Automat A vždy odebral jednu minci, automat B vždy odebral co nejvíce, maximálně však polovinu všech mincí, které právě byly na hromádce. 
Kdo odebral z hromádky poslední minci, vyhrál.

Automaty hrály tuto hru mnohokrát a při zahájení se pravidelně střídaly. Na začátku každé hry byl na hromádce náhodný počet mincí, nejméně 10, nejvíce 30 mincí.

Kdo z automatů vyhrával?

- častěji vyhrál B
- častěji vyhrál A
- oba vyhrávaly stejně často
- vždy vyhrál A

úloha byla převzata ze soutěže Bobřík informatiky

řešení:
Představme si konec hry. Na hromádce zbyla jedna mince. Je-li na tahu automat A, vezme ji a vyhraje. Automat B však smí vzít pouze polovinu všech mincí na hromádce, celou minci tedy vzít nesmí. Nevezme tedy nic a v následujícím tahu minci vezme automat A.

Automat A vždy vyhraje.

## Úkol 2

vězni v řadě, každý druhý umírá, kdo přežije