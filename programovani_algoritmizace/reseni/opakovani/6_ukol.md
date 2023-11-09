```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def cerveny_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")

def modry_ctverec():
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    canvas.create_rectangle(x, y, x + 10, y + 10, fill="blue")

for i in range(2000):
    modry_ctverec()
    cerveny_ctverec()

input()
```

[zpět](../../programovani_uvod.md#úkol-6-5)