```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def hvezda():
    x = random.randint(1, 300)
    y = random.randint(11, 200)
    strana = random.randint(2, 4)
    canvas.create_rectangle(x, y, x + strana, y + strana, fill="yellow")

  
canvas.create_rectangle(0, 0, 500, 500, fill="navy")
for i in range(1000):
    hvezda()

input()
```

[zpět](../../programovani_uvod.md#úkol-7-5)