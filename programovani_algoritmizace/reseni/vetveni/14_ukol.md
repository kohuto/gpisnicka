```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 120:
        if x < y:
            canvas.create_rectangle(x, y, x + 5, y + 5, fill="blue")
        else:
            canvas.create_rectangle(x, y, x + 5, y + 5, fill="white")
    else:
        if x > y - 125:
            canvas.create_rectangle(x, y, x + 5, y + 5, fill="white")
        else:
            canvas.create_rectangle(x, y, x + 5, y + 5, fill="blue")

input()
```

[zpět](../../programovani_uvod.md#úkol-14-1)