# Řešení

## Přehled

1. [Vypisování](#vypisování)
2. [Proměnná](#proměnná)
3. [Vypisování podruhé](#vypisování-podruhé)
4. [Kreslení](#kreslení)
5. [Podprogramy](#podprogramy)
6. [Náhoda](#náhoda)
7. [Kreslení textu](#kreslení-textu)
8. [Opakování](#opakování)
9. [Větvení](#větvení)
10. [Podprogramy s parametrem](#podprogramy-s-parametrem)
11. [Pole](#pole)

## Výpisy

### Úloha 2

```
123
25
23
35
12.0
2.5
```

### Úloha 3

Objeví se chyba `invalid syntax`

### Úloha 4

Objeví se chyba `division by zero`

### Úloha 5

```python
# počet dní
print(16 * 365 + 2 * 30)
# počet hodin
print(5900 * 24)
# počet sekund
print(141600 * 60 * 60)
```

### Úloha 6

```python
print(123456789 * 111111111111111111111)
# nejčastější číslo je 9
```

### Úloha 7

```python
print(2 ** 30)
# 10 cifer
```

## Proměnná

### Úloha 3

```python
vyska = 167
print(vyska) # 167

cena = 22 + 7
print(cena) # 29
```

### Úloha 4

Objeví se chyba `NameError: name 'vek' is not defined`

### Úloha 5

```
23
97
196
```

### Úloha 7

```python
a = 100
vyska = 167 * 100
cena = 29
```

### Úloha 8

```python
zmrzlina = 25
pocet = 7
zaplatit = zmrzlina * pocet
print(zaplatit)
```

### Úloha 9

```python
polomer = 4
pi = 3.14
obvod = 2 * pi * polomer
obsah = pi * polomer ** 2
print(obvod)
print(obsah)
```

### Úloha 10

```python
kuk # ano
Ahoj! # ne - obsahuje vykřičník
1.A # ne - začíná číslem a obsahuje tečku
prvni_trida # ano
cerno-bile # ne - python to chápe jako odčítání dvou proměnných
OK # ano
o0o0o0o # ano - ale špatně čitelné
asdf # ano - ale nepoznáme význam proměnné z jejího názvu
věk # ano - ale nedporoučuje se diakritika
počet osob # ne - obsahuje mezeru
trida(3) # ne - obsahuje závorky
```

# Vypisování podruhé

### Úloha 1

```
Ahoj, já jsem počítač
```

### Úloha 2

```python
7 # spočítá výraz
1 + 2 * 3 # vypíše text v apostrofech
    # vypíše prázdný řádek
```

### Úloha 3

- Výsledný text bude na jednom řádku, mezi vypisované texty se vloží mezera
- Můžeme kombinovat texty i hodnoty (a mezi vypisované části se též vloží mezera)
- Když uvedeme výraz, ten se vyhodnotí a na obrazovku se vypíše výsledek

### Úloha 4

```
Je mi 16 let
```

### Úloha 5

```python
vek = 16
print('Je mi', vek, 'let')
print('Příští rok mi bude', vek + 1, 'let')
```

### Úloha 7

```python
penize = 100
platba = 20
print('Mám', penize, 'korun')
print('Platím', platba, 'korun')
print('Zbyde mi', penize - platba, 'korun')
```

### Úloha 8

```python
sirka = 50
delka = 80
pocet_kol = 7
print('Šířka hřiště je', sirka, 'metrů, délka je', delka,
'metrů')
print('Jedno kolo okolo hřiště je', 2 * (sirka + delka),
'metrů')
print('Po', pocet_kol, 'kolech uběhneš',
2 * (sirka + delka) * pocet_kol, 'metrů')
```

### Úloha 9

```python
puvodni_cena = 199
sleva = 20
cena_po_sleve = puvodni_cena - puvodni_cena * sleva / 100
print('Cena alba je', puvodni_cena, 'korun')
print('Sleva činí', sleva, 'procent')
print('Zaplatíš', cena_po_sleve,'korun')
```

## Kreslení

### Úloha 3

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 30, 300, 200)
input()
```

### Úloha 4

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(200, 100, 260, 240)
input()
```

### Úloha 5

```python
canvas.create_rectangle(100, 50, 100 + 80, 50 + 80)
canvas.create_rectangle(200, 50, 200 + 80, 50 + 80)
```

### Úloha 6

```python
canvas.create_rectangle(100, 50, 250, 200)
canvas.create_rectangle(100 + 25, 50 + 25, 250 - 25, 200 - 25)
```

### Úloha 7

```python
canvas.create_rectangle(100, 200, 100 + 150, 200 + 50)
canvas.create_rectangle(100 + 25, 150, 100 + 150 - 25, 150 + 50)
canvas.create_rectangle(100 + 50, 100, 100 + 150 - 50, 100 + 50)
```

### Úloha 8

```python
canvas.create_rectangle(100, 100, 200, 200)
canvas.create_rectangle(100, 100 - 50, 100 + 50, 100)
canvas.create_rectangle(200 - 50, 200, 200, 200 + 50)
canvas.create_rectangle(100 - 50, 200 - 50, 100, 200)
canvas.create_rectangle(200, 100, 200 + 50, 100 + 50)
```

### Úloha 10

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(30, 30, 130, 130, fill='red')
canvas.create_rectangle(150, 30, 250, 130, fill='green')
canvas.create_rectangle(30, 150, 130, 250, fill='blue')
canvas.create_rectangle(150, 150, 250, 250, fill='yellow')
input()
```

### Úloha 11

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 300, 100, fill='red')
canvas.create_rectangle(50, 100, 300, 150, fill='white')
canvas.create_rectangle(50, 150, 300, 200, fill='blue')
input()
```

### Úloha 12

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 150, 200, fill='green')
canvas.create_rectangle(150, 50, 250, 200, fill='white')
canvas.create_rectangle(250, 50, 350, 200, fill='orange')
input()
```

### Úloha 13

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 150, 150, fill='magenta')
canvas.create_rectangle(70, 70, 170, 170, fill='violet')
canvas.create_rectangle(90, 90, 190, 190, fill='plum')
canvas.create_rectangle(110, 110, 210, 210, fill='pink')
input()
```

### Úloha 14

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(50, 50, 300, 210, fill='white')
canvas.create_rectangle(50, 50, 110, 110, fill='red')
canvas.create_rectangle(150, 50, 300, 110, fill='red')
canvas.create_rectangle(50, 150, 110, 210, fill='red')
canvas.create_rectangle(150, 150, 300, 210, fill='red')
canvas.create_rectangle(50, 120, 300, 140, fill='navy')
canvas.create_rectangle(120, 50, 140, 210, fill='navy')
input()
```

### Úloha 15

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_rectangle(30, 90, 210, 150, fill='red')
canvas.create_rectangle(90, 30, 150, 210, fill='green')
canvas.create_rectangle(90, 90, 150, 150, fill='yellow')
input()
```

### Úloha 16

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 70
canvas.create_rectangle(x, y, x + 100, y + 100, fill='yellow')
input()
```

### Úloha 17

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 70
sirka = 200
vyska = 50
canvas.create_rectangle(x, y, x + sirka, y + vyska, fill='red')
input()
```

### Úloha 18

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 100
y = 70
canvas.create_rectangle(x, y, x + 100, y + 100, fill='red')
canvas.create_rectangle(x, y, x + 70, y + 70, fill='blue')
canvas.create_rectangle(x, y, x + 40, y + 40, fill='navy')
input()
```

### Úloha 19

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 30
y = 100
a = 100
b = 70
canvas.create_rectangle(x, y, x + a, y + b, fill='blue')
canvas.create_rectangle(x + a, y, x + 2 * a, y + b, fill='light blue')
canvas.create_rectangle(x + 2 * a, y, x + 3 * a, y + b, fill='dark blue')
input()
```

### Úloha 20

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 50
y = 200
canvas.create_rectangle(x, y - 100, x + 100, y, fill='red')
canvas.create_rectangle(x + 100, y - 80, x + 180, y, fill='yellow')
canvas.create_rectangle(x + 180, y - 60, x + 240, y, fill='green')
canvas.create_rectangle(x + 240, y - 40, x + 280, y, fill='violet')
canvas.create_rectangle(x + 280, y - 20, x + 300, y, fill='blue')
input()
```

## Podprogramy

### Úloha 3

```python
print('Hello')
vypis_text()
print('How are you?')
vypis_text()
print('I am fine.')
vypis_text()
print('The end')
```

### Úloha 4

```python
def refren():
    print('já mám koně vraný koně')
    print('to jsou koně mí')
refren()
refren()
print()
print('když já jím dám ovsa')
print('oni skáčou hopsa')
print()
refren()
refren()
```

### Úloha 5

```python
# definice podporgramů
def trojuhelnik():
    print(' *')
    print(' ***')
    print('*****')
def obdelnik():
    print('#####')
    print('# #')
    print('#####')
def noha():
    print(' |')
    print('__|__')

# obrázek 1
trojuhelnik()
trojuhelnik()
noha()

# obrázek 2
trojuhelnik()
obdelnik()
noha()

# obrázek 3
obdelnik()
noha()
obdelnik()

# obrázek 4
print('toto je noha:')
noha()
print()
print('toto je obdélník:')
obdelnik()
print()
print('toto je trojúhelník:')
trojuhelnik()
```

### Úloha 7

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def kriz():
    canvas.create_rectangle(150 - 90, 100 - 30, 150 + 90, 100 + 30, fill='red')
    canvas.create_rectangle(150 - 30, 100 - 90, 150 + 30, 100 + 90, fill='red')
kriz()
input()
```

### Úloha 8

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def hlava():
    canvas.create_rectangle(160, 40, 200, 100, fill='sky blue')
    canvas.create_rectangle(150, 10, 210, 55, fill='steel blue')
def telo():
    canvas.create_rectangle(140, 70, 220, 190, fill='royal blue')
def ruce():
    canvas.create_rectangle(80, 90, 280, 110, fill='tomato')
def nohy():
    canvas.create_rectangle(150, 160, 170, 250, fill='purple')
    canvas.create_rectangle(190, 160, 210, 250, fill='purple')
hlava()
ruce()
nohy()
telo()
input()
```

## Náhoda

### Úloha 3

```python
import random
def hod_kostkou():
    n = random.randint(1, 6)
    print('Na kostce padla', n)
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
hod_kostkou()
```

### Úloha 4

```python
def hod_kostkou():
    n = random.randint(1, 20)
    print('Na kostce padla', n)
```

### Úloha 5

```python
def hod_kostkou():
    n = random.randint(1, 6) * 2
    print('Na kostce padla', n)
```

### Úloha 6

```python
def hod_kostkou():
    n = random.randint(1, 6) * 2 - 1
    print('Na kostce padla', n)
```

### Úloha 7

```python
def hod_kostkou():
    n = random.randint(1, 6) ** 2
    print('Na kostce padla', n)
```

### Úloha 8

```python
import random
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)
print('Tvůj nový PIN je', a, b, c, d)
```

### Úloha 9

```python
import random
den = random.randint(1, 30)
mesic = random.randint(1, 12)
rok = random.randint(2018, 2099)
print('Pokoj si uklidím', den, '.', mesic, '.', rok)
```

### Úloha 11

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def nahodny_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    canvas.create_rectangle(x, y, x + 50, y + 50,fill='orange')
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
input()
```

### Úloha 12

```python
def nahodny_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    a = random.randint(10, 100)
    canvas.create_rectangle(x, y, x + a, y + a, fill='orange')
```

## Kreslení textu

### Úloha 2

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_text(180, 20, text='Horní okraj')
canvas.create_text(180, 230, text='Dolní okraj')
canvas.create_text(310, 120, text='Pravý okraj')
canvas.create_text(50, 120, text='Levý okraj')
input()
```

### Úloha 3

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def nahodne_cislo():
    x = random.randint(50, 300)
    y = random.randint(50, 200)
    n = random.randint(100000, 999999)
    canvas.create_text(x, y, text=n)
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
nahodne_cislo()
input()
```

## Opakování

### Úloha 1

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def gps():
    x = random.randint(20, 360)
    y = random.randint(20, 240)
    canvas.create_text(x, y, text='+')
    canvas.create_text(x - 10, y + 10, text=x)
    canvas.create_text(x + 10, y + 10, text=y)
gps()
gps()
gps()
gps()
gps()
gps()
gps()
gps()
gps()
gps()
input()
```

### Úloha 2

```python
print('Těším se na prázdniny')
print('Těším se na prázdniny')
print('Těším se na prázdniny')
print('Těším se na prázdniny')
print('Těším se na prázdniny')
```

### Úloha 3

číslo v závorkách u příkazu `range` označuje počet opakování od okraje odsazeného příkazu.

### Úloha 6

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def gps():
    x = random.randint(20, 360)
    y = random.randint(20, 240)
    canvas.create_text(x, y, text='+')
    canvas.create_text(x - 10, y + 10, text=x)
    canvas.create_text(x + 10, y + 10, text=y)
for i in range(10):
    gps()
input()
```

### Úloha 7

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def cerveny_ctverec():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')
for i in range(2000):
    cerveny_ctverec()
input()
```

### Úloha 8

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def cerveny_ctverec():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='red')
def modry_ctverec():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='blue')
for i in range(2000):
    cerveny_ctverec()
    modry_ctverec()
input()
```

### Úloha 9

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
def hvezdicka():
    x = random.randint(10, 360)
    y = random.randint(10, 250)
    a = random.randint(2, 4)
    canvas.create_rectangle(x, y, x + a, y + a, fill='yellow')
canvas.create_rectangle(0, 0, 380, 270, fill='navy')
for i in range(1000):
    hvezdicka()
input()
```

### Úloha 10

```python
import random
for i in range(5):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print('Na první kostce padlo číslo', a)
    print('Na druhé kostce padlo číslo', b)
    print('Součet obou čísel je', a + b)
    print()
```

### Úloha 11

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
for i in range(250):
    x = random.randint(1, 21) * 10
    y = random.randint(1, 21) * 10
    canvas.create_rectangle(x, y, x + 10, y + 10, fill='black')
input()
```

### Úloha 13

```python
# Řešení pro 0, 1, ... 10:
for i in range(11):
    print('číslo', i)

# Řešení pro 1, 2, ... 10:
for i in range(10):
    print('číslo', i + 1)

# Řešení pro 2, 4, ... 20:
for i in range(10):
    print('číslo', (i + 1) * 2)

#Řešení pro 10, 20, ... 100:
for i in range(10):
    print('číslo', (i + 1) * 10)
```

### Úloha 14

```python
for i in range(7):
    print(i, 'na druhou je', i ** 2)
```

### Úloha 15

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 10
for i in range(9):
    canvas.create_rectangle(x, 100, x + 30, 130, fill='red')
    x = x + 40
input()
```

### Úloha 16

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
x = 10
for i in range(10):
    a = random.randint(10, 40)
    canvas.create_rectangle(x, 100 - a, x + a, 100, fill='gold')
    x = x + a
input()
```

### Úloha 17

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
x = 10
for i in range(10):
    a = random.randint(10, 40)
    canvas.create_rectangle(x, 100 - a, x + a, 100, fill='gold')
    x = x + a + 5
input()
```

### Úloha 18

```python
zrnek = 0
for i in range(64):
    zrnek = zrnek + (i + 1) * 10
print('Počet zrnek na šachovnici bude:', zrnek)
```

Celkový počet zrn bude 20800, což je přibližně 832 gramů.

## Větvení

### Úloha 3

```
Je 10 stupňů.
Dnes je zima.
Správně se obleč.
```

### Úloha 4

```python
teplota = 0
print('Je', teplota, 'stupňů.')
if teplota < 0:
    print('Vezmi si rukavice.')
else:
    print('Rukavice nejsou potřeba.')
```

### Úloha 5

```python
hmotnost = 100
print('Hmotnost dopisu je', hmotnost, 'gramů')
if hmotnost > 50:
    print('Zaplatíš 55 korun')
else:
    print('Zaplatíš 47 korun')
```

### Úloha 6

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
a = 50
b = 100
if a > b:
    canvas.create_rectangle(100, 250 - b, 100 + a, 250, fill='red')
else:
    canvas.create_rectangle(100, 250 - a, 100 + b, 250, fill='red')
input()
```

### Úloha 7

```python
megabajty = 6
if megabajty < 10:
    cena = megabajty * 2
else:
    cena = 20
print('Zaplatíš', cena, 'korun.')
```

### Úloha 8

```python
a = -7
if a < 0:
    print('Absolutní hodnota', a, 'je', -a)
else:
    print('Absolutní hodnota', a, 'je', a)
```

### Úloha 10

```python
a = 10
b = 10
if a == b:
    print('Je to čtverec.')
else:
    print('Je to obdélník.')
```

### Úloha 11

```python
import random
pocet_6 = 0
pocet_jine = 0
for i in range(10):
    n = random.randint(1, 6)
    print(n)
    if n == 6:
        pocet_6 = pocet_6 + 1
    else:
        pocet_jine = pocet_jine + 1
print('Padlo', pocet_6, 'šestek a', pocet_jine, 'jiných čísel')
```

### Úloha 12

```python
import random
pocet_premii = 0
predtim = 0
for i in range(10):
    n = random.randint(1, 6)
    print(n)
    if n == predtim:
        pocet_premii = pocet_premii + 1
    else:
        predtim = n
print('Počet premií:', pocet_premii)
```

### Úloha 14

```python
ja = 10
ona = 15
if ja == ona:
    print('Jsme stejně staří.')
else:
    if ja < ona:
        print('Jsem mladší.')
    else:
        print('Ona je mladší.')
```

### Úloha 15

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='black')
    else:
        if y < 170:
            canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='red')
        else:
            canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='gold')
input()
```

### Úloha 16

```python
import tkinter
import random
canvas = tkinter.Canvas()
canvas.pack()
for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 130:
        if x < y:
            canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='blue')
        else:
            canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='white')
    else:
        if 130 - x > y - 130:
            canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='blue')
        else:
            canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill='red')
input()
```

## Podprogramy s parametrem

### Úloha 1

```python
def jemi10():
    vek = 10
    print('Je mi', vek, 'let')
def jemi20():
    vek = 20
    print('Je mi', vek, 'let')
def jemi30():
    vek = 30
    print('Je mi', vek, 'let')
```

### Úloha 3

```python
def vypis(x):
    print('Číslo', x)
    print('Umocněné na druhou se rovná', x ** 2)
vypis(1)
vypis(2)
vypis(3)
```

### Úloha 4

```python
def vypis(x):
    print('Číslo', x)
    print('Umocněné na druhou se rovná', x * x)
    print('Převrácená hodnota se rovná', 1 / x)
```

### Úloha

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def ctverec(x):
    canvas.create_rectangle(200, 150, 200 + x, 150 + x)
ctverec(10)
ctverec(100)
ctverec(50)
input()
```

### Úloha

```python

```

### Úloha

```python

```

### Úloha

```python

```
