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

## Virtuální prostředí

https://code.visualstudio.com/docs/python/environments

projekty tvoříme ve virtuálním prostředí.

k čemu to je?

Jak vytvořit virtuální prostředí (virtual enviroment - venv)?

1. otevřete paletu příkazů (Ctrl+Shift+P)
2. vyhledejte položku `Python: Create Environment` a vyberte ji
3. objeví se dvě možnosti `Venv` or `Conda`.
4. vybereme možnost `Venv`
5. vybereme požadovaný interpretr

## Proměnná

Proměnná se používá pro ukládání hodnot. Zapisujeme vždy jako `název proměnné` = `hodnota proměnné`:

```python
cislo = 42    # proměnná číslo s hodnotou 42
text = "muj_text"    # proměnná text s hodnotou muj_text
```

Do proměnné lze dosadit i výraz. Uloží se výsledek výrazu:

```python
vysledek = 4 * 3    # proměnná výsledek s hodnotou 12
x = 5 + 5 - 2    # proměnná x s hodnotou 8
```

Do proměnné lze dosadit i jinou proměnnou:

```python
x = 3    # v proměnné x je hodnota 3
y = x    # v proměnné y je hodnota x (hodnota 3)
z = x - 1    # v proměnné z je hodnota 2
```

## Datový typ

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

## Tkinter

`tkinter` je knihovna pro tvorbu GUI.

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
```

program vyrobil grafickou plochu `canvas`.

Lze vykreslit třeba obdélník:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 70, 220, 150)
```

Souřadnice fungují v tkinter trochu netradičně:
![coordinates](images\canvas_coordinates.png)

V matematice jsme zvyklí, že střed je "uprostřed". Zde ale leží bod se souřadnicemi $[0, 0]$ v levém horním rohu. Osa $x$ jde zleva doprava. Osa $y$ jde shora dolů (čím větší číslo, tím níže).

V příkazu `canvas.create_rectangle(x1, y1, x2, y2)` píšeme do závorek souřadnice protilehlých vrcholů obdélníku:

![rectangle](images\rectangle_coord_1.png)

Tyto souřadnice vrcholů bychom mohli znázornit na souřadnicových osách následujícím způsobem:

![rectangle](images\rectangle_coord_2.png)

Obdélník může být i vybarvený:

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(30, 30, 130, 130, fill='red')
```

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
