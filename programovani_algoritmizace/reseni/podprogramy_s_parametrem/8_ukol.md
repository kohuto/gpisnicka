```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def nahodny_ctverec(a):
    x = random.randint(10, 300)
    y = random.randint(10, 200)
    canvas.create_rectangle(x, y, x + a, y + a, fill="red")

for i in range(10):
    nahodny_ctverec(i + 1)
```

[zpět](../../programovani_uvod.md#úkol-8-5)