```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec():
    x = random.randint(10, 300)
    x = random.randint(10, 200)
    strana = random.randint(10, 100)
    canvas.create_rectangle(x, y, x + strana, y + strana)
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()

input()
```

[zpět](../../programovani_uvod.md#úkol-12)