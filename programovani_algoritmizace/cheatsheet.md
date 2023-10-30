## Vypisování

```python
print(123)
print("ahoj")
```

## Proměnná

```python
a = 123
b = "ahoj"
print("text a proměnné", a, b)
```

## Tkinter

```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50, 70, 220, 150, fill="red")

input()
```

## Podprogramy

```python
def nazev(i):
    print("ahoj")
    print(i)
    print(i + 1)

nazev()
```

## Náhoda

```python
import random
x = random.randint(1,6)
print(x)
```

## Opakování

```python
for i in range(10):
    print(i)
```

## Větvení

```python
i = 3

if i > 3:
    print("vetsi")
elif i == 3:
    print("rovno")
else:
    print("mensi")
```

## Pole