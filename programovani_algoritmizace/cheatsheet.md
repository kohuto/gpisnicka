## Vypisování

```python
print(123)
print("ahoj")
print("text + proměnné: ", a, b)
```

## Proměnná

```python
a = 123
b = "ahoj"
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
def muj_podprogramek(i):
    print("hodnota parametru:", i)

muj_podprogramek(42)
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

## Seznamy

```python
seznam = [1, 4, -7, 2, 5]

for i in seznam:
    print(i)

seznam[0] = 42
print(seznam[0])
```
