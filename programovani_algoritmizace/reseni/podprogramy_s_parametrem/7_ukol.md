```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec(a):
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    canvas.create_rectangle(x, y, x + a, y + a, fill="red")

nahodny_ctverec(10)
nahodny_ctverec(100)
nahodny_ctverec(70)
```

[zpět](../../programovani_uvod.md#úkol-7-7)