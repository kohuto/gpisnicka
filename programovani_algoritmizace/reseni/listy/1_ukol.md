```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

cislo = random.randint(0,3)

if cislo == 0:
    canvas.create_rectangle(50, 50, 50 + 30, 50 + 30, fill="red")
elif cislo == 1:
    canvas.create_rectangle(50, 50, 50 + 30, 50 + 30, fill="green")
elif cislo == 2:
    canvas.create_rectangle(50, 50, 50 + 30, 50 + 30, fill="blue")
else:
    canvas.create_rectangle(50, 50, 50 + 30, 50 + 30, fill="yellow")

input()
```

[zpět](../../programovani_uvod.md#úkol-1-8)