```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

cislo = random.randint(0,3)
barvy = ["red", "green", "blue", "yellow"]
barva = barvy[cislo]
canvas.create_rectangle(50, 50, 50 + 30, 50 + 30, fill=barva)
```

[zpět](../../programovani_uvod.md#úkol-13-2)