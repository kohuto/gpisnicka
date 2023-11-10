```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec(a):
    if a > 0:
        x = random.randint(10, 300)
        y = random.randint(10, 200)
        canvas.create_rectangle(x, y, x + a, y + a, fill="red")
    else:
        print("nedá se")

nahodny_ctverec(-30)
nahodny_ctverec(0)
nahodny_ctverec(100)
```

[zpět](../../programovani_uvod.md#úkol-9-5)