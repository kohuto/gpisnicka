# Řešení

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
import tkinter
import random
def nahodny_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    a = random.randint(10, 100)
    canvas.create_rectangle(x, y, x + a, y + a, fill='orange')
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
input()
```

## Kreslení textu

### Úloha

```python

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

### Úloha

```python

```

### Úloha

```python

```

### Úloha

```python

```
