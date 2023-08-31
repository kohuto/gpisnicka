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

### Úloha

```python

```

### Úloha

```python

```
