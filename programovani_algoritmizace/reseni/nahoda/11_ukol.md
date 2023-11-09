```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec():
    x = random.randint(10, 300)
    x = random.randint(10, 200)
    canvas.create_rectangle(x, y, x + 50, y + 50)
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()
nahodny_ctverec()

input()
```

[zpět](../../programovani_uvod.md#úkol-11)