# PYTHON

## Přehled

1. [Co je Python?](#html)
2. [VS code](#vs-code)
3. [Virtuální prostředí](#virtuální-prostředí)
4. [Komentář](#komentář)
5. [Řídící struktury](#nadpis)
6. [Funkce](#odstavec)
7. [Pole](#kontejner)
8. [Proměnná](#zalomení-řádku)
9. [OOP](#třídy-a-id)
10. [Dědičnost](#kontejner)
11. [Práce se soubory](#kontejner)
12. [Složitost](#kontejner)
13. [Moduly](#kontejner)
14. [Výjimky](#kontejner)
15. [Vstup/výstup](#kontejner)
16. [Třídící algoritmy](#kontejner)

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

Abychom mohli psát programy v pythonu, je potřeba nainstalovat interpreter pro python. Instalační balíček stáhněte [zde](https://www.python.org/downloads/).

## VS code

programy budeme psát ve Visual Studiu Code (VS code). VS code je potřeba nainstalovat nainstalovat do počítače z [oficiálních stránek](https://code.visualstudio.com/).

V momentě kdy máte nainstalované VS code, je potřeba nainstalovat ještě rozšíření ve VS code. V sekci `extension` vyhledejte `python` a vyberte první možnost (viz obrázek):

![vs code extension](images/vscodeextension.png)

Program lze spustit bud pomocí `ctrl+F5` nebo tlačítkem `run python file` v pravém horním rohu.

## Virtuální prostředí

projekty tvoříme ve [virtuálním prostředí](https://code.visualstudio.com/docs/python/environments).

k čemu to je?

Jak vytvořit virtuální prostředí (virtual enviroment - venv)?

1. otevřete paletu příkazů (Ctrl+Shift+P)
2. vyhledejte položku `Python: Create Environment` a vyberte ji
3. objeví se dvě možnosti `Venv` or `Conda`.
4. vybereme možnost `Venv`
5. vybereme požadovaný interpretr

## Výpisy

### Úloha 1

Zkusme napsat první program:

```python
print(1 + 2 + 3)
```

`print` je [funkce](#podprogramy) (funkcím se budeme věnovat později). To, co napíšeme do závorek se vypíše do konzole.

### Úloha 2

Python dokáže fungovat jako kalkulačka. Jaké budou výsledky následujících výrazů?

```python
print(123)
print(42 - 17)
print(3 + 4 * 5)
print((3 + 4) * 5)
print(132 / 11)
print(1 + 2 * 3 / (5 – 1))
```

### Úloha 3

Pozor, zápisy musí být správně, jinak se objeví chyba. Co se
stane, pokud zadáš následující příkazy?

```python
print(22 + 7 *)
print(19 - (3 4))
```

### Úloha 4

Někdy se však i po správném zápise může objevit chybové hlášení. Co se stane, pokud zadáš následující příkaz?

```python
print(10 / (6 – 2 * 3))
```

### Úloha 5

Petrovi bylo přesně před dvěma měsíci 16 let. Využij Python jako kalkulačku a spočítej:

1. Kolik je mu nyní přibližně dní?
2. Kolik je to hodin?
3. Kolik je to sekund?

Předpokládej, že rok má 365 dní a měsíc má 30 dní.

### Úloha 6

Zjisti, která číslice se vyskytuje nejčastěji ve výsledku výrazu:
$123456789 * 111111111111111111111$

### Úloha 7

Výpočet $2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2 * 2$ je umocnění $2^{10}$. V Pythonu se umocnění zapisuje jako `2 ** 10`.

- Tipni si, kolik číslic bude mít $2^{30}$.
- Vypočítej pomocí pythonu a ručně spočítej počet číslic ve výsledku.

## Proměnná

V matematice je zvykem označovat hodnoty písmeny, například délka strany čtverce $a = 100$ nebo poloměr kruhu $r=4$. To samé můžeš udělat i v Pythonu.

### Úloha 1

Zkus napsat následující program:

```python
a = 100
```

Nic se nestalo (to je správně!). Python si vytvořil _proměnnou_ s _názvem_ `a` a přitom si zapamatoval, že má _hodnotu_ 100.

Lze si to představit jako krabičku. Text na krabičce je _název_ proměnné, zatímco to, co dáme dovnitř krabičky je _hodnota_ proměnné:

![variable as box](images/variableasbox.jpg)

### Úloha 2

Zkusme nyní vypsat proměnnou `a`:

```python
a = 100
print(a)
```

Vypíše se hodnota uložená v proměnné.

### Úloha 3

Vyzkoušej vytvořit a nastavit i jiné proměnné:

```python
vyska = 167
cena = 22 + 7
```

Zkontroluj, jaké hodnoty se do proměnných uložily.

Proměnných můžeme vytvořit, kolik budeme chtít a později je používat v dalších výpočtech.

### Úloha 3

Definujme tři proměnné:

```python
a = 100
vyska = 167
cena = 29
```

Co se stane, když bychom chtěli vypsat proměnnou `vek`, kterou jsme zatím nedefinovali?

```python
print(vek)
```

### Úloha 4

Proměnné můžeš použít i v matematických zápisech a Python namísto názvu proměnné dosadí její hodnotu. Mějme proměnné `a`, `vyska` a `cena` ze cvičení 3. Urči výsledek následujících příkazů:

```python
print(190 - vyska)
print(3 * cena + 10)
print(cena + vyska)
```

### Úloha 5

Proměnným můžeme změnit jejich obsah – vyzkoušej:

```python
cena = 29
cena = 6 * 7
print(cena)
```

### Úloha 5

Změň hodnotu proměnné vyska tak, aby v ní byla tvoje výška v centimetrech.

### Úloha 5

Přiřaď do proměnné `zmrzlina` cenu jedné zmrzliny (například 25 korun). Do proměnné `pocet` přiraď počet kamarádů, kterým chceš koupit po jedné zmrzlině. Za
použití proměnných sestav přiřazovací příkaz, pomocí kterého se do třetí proměnné `zaplatit` přiřadí celková cena, kterou zaplatíš.

### Úloha 6

V matematice značíme obsah kruhu $S$ a počítáme jej podle vzorce $\pi  r^2$. Obvod kruhu značíme $O$ a počítáme jej podle vzorce $2 \pi  r$. Vytvoř proměnné pro `poloměr`, `obsah` i `obvod` kruhu a přiřaď do nich správné výrazy. Vytvoř si proměnnou `pi` s hodnotou $3.14$.

### Úloha 7

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

## Vypisování

### Úloha 1

Příkaz `print` již známe. Vyzkoušej, co vypíše následující program:

```python
print('Ahoj, já jsem počítač')
```

Příkaz `print` slouží na vypisování textů. Text, který se má vypsat, napíšeš mezi apostrofy.

### Úloha 2

Zjisti, co Python vypíše v případě následujících příkazů:

```python
print(1 + 2 * 3)
print('1 + 2 * 3')
print()
```

### Úloha 3

Příkaz `print` umí vypsat víc věcí – vyzkoušej následující příkazy. Co způsobí čárka v jednotlivých příkazech?

```python
print('Mám rád', 'kapustu')
print('Moje oblíbené číslo je', 42)
print('Do školy jsem šel', 2 * 10, 'minut')
```

### Úloha 4

V příkazu `print` lze kombinovat i proměnné. Zkus, co vypíše následující program:

```python
vek = 16
print('Je mi', vek, 'let')
```

### Úloha 5

Rozšiř program z úlohy 4 tak, aby navíc vypsal zprávu: _Příští rok mi bude 17 let_.

### Úloha 6

Představ si, že program z úlohy 5 spustí tvůj otec. Vyzkoušej program za něj – dosaď do proměnné věk jeho skutečný věk. Zobrazí se správný výsledek i na druhém řádku svého výstupu? Jestli ne, program oprav.

### Úloha 7

Vytvoř nový program. Na začátku přiřaď do proměnně `penize`, kolik korun máš. Do proměnné `platba` přiřaď cenu nákupu. Použij proměnné a vypiš pomocí nich:

```
Mám ... korun
Platím ... korun
Zbyde mi ... korun
```

### Úloha 8

Hřiště má šířku 50 metrů a délku 80 metrů. Budeš běhat po obvodě. Vytvoř program, který vypíše, kolik metrů uběhneš po
7 kolech. Do proměnné `sirka` přiřaď hodnotu 50, do proměnné
`delka` hodnotu 80 a do proměnné `pocet_kol` hodnotu 7. Vypiš text:

```
Šířka hřiště je 50 metrů, délka je 80 metrů
Jedno kolo okolo hřiště je 260 metrů
Po 7 kolech uběhneš 1820 metrů
```

Předpokládejme nyní, že šířka je 45 metrů a délka 70 metrů. Přepiš hodnoty v proměnných. Zobrazí program správné
hodnoty na druhém a na třetím řádku výstupu? Jestli ne, program oprav.

### Úloha 9

Obchod nabízí 20% slevu. Původní cena výrobku byla 199 korun. Napiš program, který vypočítá, kolik zaplatíš. V programu
použij proměnné `puvodni_cena`, `sleva`, `cena_po_sleve` a pomocí nich vypiš:

```
Cena alba je 199 korun
Sleva činí 20 procent
Zaplatíš 159.2 korun
```

Jakou výslednou cenu program vypíše pro výrobek, jehož původní cena byla 399 korun, jestliže sleva činí 30 %?

## Kreslení

Doposud programy počítaly a vypisovaly textové zprávy. Nyní zkusíme kreslit obrázky. Postupuj takto:

1. Vytvoř následující program:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
```

2. Program spusť – na obrazovce uvidíš nové okno.
3. Zjisti, zda se dá okno posouvat, měnit jeho velikost. Nakonec toto nové okno zavři.
   program vyrobil grafickou plochu `canvas`.

### Úkol 1

Přidej do programu nový příkaz:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 70, 220, 150)
```

příkaz vykreslí obdelník.

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

![coordinates](images\canvas_coordinates.png)

V matematice jsme zvyklí, že střed je "uprostřed". Zde ale leží bod se souřadnicemi $[0, 0]$ v levém horním rohu. Osa $x$ jde zleva doprava. Osa $y$ jde shora dolů (čím větší číslo, tím níže).

V příkazu `canvas.create_rectangle(x1, y1, x2, y2)` píšeme do závorek souřadnice protilehlých vrcholů obdélníku:

![rectangle](images\rectangle_coord_1.png)

Tyto souřadnice vrcholů bychom mohli znázornit na souřadnicových osách následujícím způsobem:

![rectangle](images\rectangle_coord_2.png)

### Úkol 3

Nakresli obdélník, který má souřadnice
protilehlých vrcholů $[50, 30]$ a $[300, 200]$.

### Úkol 4

Nakresli obdélník, který má jeden vrchol na souřadnicích $[200, 100]$, jeho šířka je 60 a výška 140.

### Úkol 5

Nakresli dva čtverce se stranami délky 80 (pozici čtverců zvol podle uvážení):

![two squares](images/twosquares.png)

### Úkol 6

Nakresli dva velké čtverce – jeden se stranou
délky 100 a druhý 150. Čtverce budou mít společný střed jako na následujícím obrázku:

![inside squares](images/inside%20squares.png)

### Úkol 7

Nakresli ze tří obdélníků o rozměrech 150x50, 100x50
a 50x50 následující pyramidu:

![pyramid](images/pyramid.png)

### Úkol 8\*

Vytvoř z pěti čtverců následující ornament.
Rozměry čtverců zvol podle svého uvážení (všechny menší čtverce budou stejně velké):

![ornament](images/ornament.png)

### Úkol 9

Obdélník lze i vybarvit:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(30, 30, 130, 130, fill='red')
```

### Úkol 10

Přidej do programu z úkolu 9 další 3 příkazy na kreslení obdélníků, abys dostal následující obrázek:

![four squares](images/foursquares.png)

Další barvy získáš, když místo slova `red` napíšeš `green`, `blue` nebo `yellow`.

### Úkol 11

Vytvoř program, který nakreslí nizozemskou vlajku:

![nizozemi](images/nizozemi.png)

### Úkol 12

Vytvoř program, který nakreslí irskou vlajku s barvou `orange`:

![irsko](images/irsko.png)

### Úkol 13

Následující obrázek vznikl ze čtyř čtverců. První z nich má souřadnice levého horního vrcholu $[50, 50]$. Napiš program, který nakreslí následující obrázek (zvol libovolné barvy):

![overlay squares](images/overlaysquares.png)

### Úkol 14\*

Vytvoř program, který vykreslí norskou vlajku:

![norsko](images/norsko.png)

### Úkol 15\*

Vytvoř nový program, ve kterém uprav následující kód tak, aby
nakreslil stejný obrázek, ale aby program obsahoval jen 3 příkazy pro kreslení obdélníků:

```python
canvas.create_rectangle(90, 90, 150, 150, fill='yellow')
canvas.create_rectangle(150, 90, 210, 150, fill='red')
canvas.create_rectangle(90, 150, 150, 210, fill='green')
canvas.create_rectangle(30, 90, 90, 150, fill='red')
canvas.create_rectangle(90, 30, 150, 90, fill='green')
```

## Podprogramy

Doposud jsme psali jen takové příkazy, které počítač znal (`print`, `int`, `str`). Nyní budeme vytvářet své vlastní příkazy – tzv. podprogramy (též funkce).

```python
def vypis_text():
    print('************')
    print('** Python **')
    print('************')
```

Slovem `def` začíná definice tvého nového příkazu – podprogramu. `vypiš_text` je název podprogramu (podobně jako `print` je název pro podprogram, který vypisuje text). Tři příkazy `print` se nazvývají tělo programu.

Když bychom tento program spustili, nic se nestane. Tímto způsobem jsme pouze počítač naučili nový příkaz `vypiš_text`. Nyní ho musíme ještě zavolat:

```python
def vypis_text():
    print('************')
    print('** Python **')
    print('************')

vypiš_text()    # volání podprogramu
```

_poznámka: závorky za `vypiš_text` jsou velice důležité_

Podprogram můžeme volat, kolikrát budeme chtít:

```python
def vypis_text():
    print('************')
    print('** Python **')
    print('************')

vypiš_text()    # 1. volání podprogramu
vypiš_text()    # 2. volání podprogramu
vypiš_text()    # 3. volání podprogramu
```

Pozor! Podprogram musí být první definovaný a až poté ho můžeme volat. Následující kód nebude fungovat, protože první se snažíme podprogram volat a až poté ho definujeme:

```python
vypiš_text()    # volání podprogramu

def vypis_text():
    print('************')
    print('** Python **')
    print('************')
```

## Náhoda

V pythonu můžeme generovat náhodná čísla následujícím způsobem:

```python
import random
print(random.randint(1, 6))
```

Program vypíše náhodné číslo od 1 do 6. Hodnoty lze samozřejmě ukládat do proměnné:

```python
import random
n = random.randint(1, 6)
print('Na kostce padla', n)
```

## Opakování

Když budeme chtít pomocí příkazu `print` vypsat
text _Těším se na prázdniny_ pětkrát pod sebe, můžeme to udělat takto:

```python
print("Těším se na prázdniny")
print("Těším se na prázdniny")
print("Těším se na prázdniny")
print("Těším se na prázdniny")
print("Těším se na prázdniny")
```

Raději ale použijeme opakování (tzv. cyklus):

```python
for i in range(5):
    print('Těším se na prázdniny')
```

Slovem for začíná příkaz cyklu. Pětka v závorce udává počet zopakování. `print` je tělo cyklu (tělo známe již z podprogramů). `i` je proměnná, do které příkaz `for` postupně dosazuje celá čísla od 0 do 4:

```python
for i in range(5):
    print('opakování:', i)

# program vypíše:
# opakování: 0
# opakování: 1
# opakování: 2
# opakování: 3
# opakování: 4
```

## Větvení

Počítač dokáže porovnávat dvě hodnoty (čísla):

```python
print(1 < 2)    # program vypíš true
print(4 < 2)    # program vypíš false
print(4 < 2 + 1)    # program vypíš false
print(4 - 7 < 2 + 1)    # program vypíš true
```

Vytvoříme program, který nám řekne, zda je teplo nebo
zima. Do proměnné teplota přiřadíme číslo. Počítač pro teplotu větší než 20 stupňů vypíše, že je teplo. Jinak řekne, že je zima:

```python
teplota = 25
if teplota > 20:
    print('Dnes je teplo.')
else:
    print('Dnes je zima.')
```

`if ... else ...` je příkaz pro větvení programu. `teplota > 20` je podmínka, podle které se počítač rozhodne, kterou větev dále vykoná. `print('Dnes je teplo.')` je větev `if`. ` print('Dnes je zima.')` je větev `else`.

Když počítač uvidí příkaz `if ... else ...`, nejdříve vyhodnotí podmínku. Když je podmínka splněná, vykoná se příkaz ve větvi `if`, jinak se vykoná příkaz ve větvi `else`.

## Pygame

https://www.pygame.org/news
ofiko stránky

```
python -m pip install -U pygame --user
```

example jestli to funguje

```
python -m pygame.examples.aliens
```

Assety: https://drive.google.com/drive/folders/1TeGCQJZbdFXXj8jcXeF1VT79brvWyOnN?usp=sharing

vytvoříme soubor `main.py`.

Vykreslíme černé okno.

```python
import pygame

WIDTH = 400
HEIGHT = 300
BACKGROUND = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

`WIDTH` a `HEIGHT` nastaví šířku okna. `BACKGROUND` jsou RGB hodnoty uložené jako [tuple](https://www.w3schools.com/python/python_tuples.asp). V metodě main pak iniciujeme `pygame`, vytvoříme `screen` i `clock` a spustíme herní smyčku ve while cyklu.

Všechno, co se bude ve hře dít, se bude odehrávat v herní smyčce. Hra se odehrává v reálném čase, tudíž je potřeba neustále kontrolovat, jestli nebyla zmáčknuta nějaká klávesa, jestli uživatel nezmáčkl myš apod. Toho docílíme pomocí nekonečné smyčky.

`clock.tick(60)` určuje, jak dlouho trvá jeden frame hry (tzn. určuje, jak dlouho trvá každá iterace smyčky), aby hra běžela plynule.

Hra bude mít dvě postavy:

- alien (player)
- box

Abychom se vyhnuli duplicitě kódu, vytvoříme rodičovskou třídu `Sprite`, která dědí z třídy `pygame.sprite.Sprite` (ta později poskytne metody pro detekci kolizí).

```python
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
```

Třída má tři metody:

1. `__init__` vytvoří sprite s daným obrázkem a na základě obrázku vytvoří obdélník (který bude sloužit pro pohyb a detekci kolizí). Obdélník bude zpočátku umístěn na pozici zadané pomocí `startx` a `starty`.
2. `update` budeme používat v potomcích pro zpracování událostí (stisky kláves, gravitace a kolize).
3. `draw` použijeme k vykreslení spritu.

Nyní můžeme konečně vytvořit třídy pro `Box` a `Player`, které dědí od třídy `Sprite`.

```Python
class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("p1_front.png", startx, starty)

class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("boxAlt.png", startx, starty)
```

Vraťme se do funkce `main` a vytvořme postavy, začneme s `player`

```python
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(100, 200)
```

`player` bude chodit po spritech `box`, těch bude více, proto vytvoříme skupinu sprites.

```python
    player = Player(100, 200)

    boxes = pygame.sprite.Group()
```

Šířka jednoho sprite `box` je 70px a potřebujeme, aby se rozprostíraly přes šířku obrazovky (400px). Využijeme forcyklus.

```python
    boxes = pygame.sprite.Group()
    for bx in range(0,400,70):
        boxes.add(Box(bx,300))
```

V hlavní smyčce budeme zařazovat nové události do fronty událostí pomocí `pygame.event.pump()` a poté volat funkci `player.update()` aktualizující postavu hráče.

```
    while True:
        pygame.event.pump()
        player.update()
```

Potřebujeme vykreslit sprity pomocí metody `draw`.

```python
    while True:
        pygame.event.pump()
        player.update()
        screen.fill(BACKGROUND)

        player.draw(screen)
        boxes.draw(screen)

        pygame.display.flip()
        clock.tick(60)
```

Nyní, když máme způsob pohybu hráče, je čas přidat metodu aktualizace, aby tento pohyb mohl být vyvolán stisknutím klávesy. Nyní přidejte prázdnou metodu update:

```python
class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("p1_front.png", startx, starty)

    def update(self):
        pass

    def move(self, x, y):
        self.rect.move_ip([x,y])
```

PyGame nabízí několik různých způsobů, jak zkontrolovat stav klávesnice. Ve výchozím nastavení shromažďuje fronta událostí KEY_DOWN a KEY_UP, když jsou stisknuty a uvolněny určité klávesy. Použití události KEY_DOWN k pohybu hráče se zdá být logické, ale protože se událost spouští pouze ve stejné aktualizační smyčce, ve které je klávesa poprvé stisknuta, nutilo by nás to rychle klepnout na klávesu se šipkou, abychom se mohli pohybovat stále jedním směrem.

Potřebujeme způsob, jak pohybovat hráčem vždy, když je klávesa se šipkou stisknutá, ne jen po jejím stisknutí. Proto se místo spoléhání na události budeme dotazovat na aktuální stav všech kláves pomocí pygame.key.get_pressed():

Tato metoda vrací tuple 0 a 1, které ukazují stav stisknutí každé klávesy na klávesnici. Můžeme tedy zjistit, zda je právě stisknuta klávesa se šipkou vlevo nebo vpravo, a to tak, že tuple indexujeme pomocí konstant klávesnice PyGame:

```python
def update(self):
    # check keys
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        self.move(-1,0)
    elif key[pygame.K_RIGHT]:
        self.move(1,0)
```

Spusťte hru. Nyní byste měli být schopni pohybovat hráčem doleva a doprava, i když velmi pomalu. Zrychlíme práci a zároveň snížíme závislost našeho kódu na magických číslech tím, že hráči přidělíme proměnnou rychlost.

```python
class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("p1_front.png", startx, starty)

        self.speed = 4

    def update(self):
        # check keys
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move(-self.speed,0)
        elif key[pygame.K_RIGHT]:
            self.move(self.speed,0)
```

```python

```

```python

```

```python

```

```python

```
