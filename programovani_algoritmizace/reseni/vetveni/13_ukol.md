```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(10000):
    x = random.randint(10, 350)
    y = random.randint(10, 250)
    if y < 90:
        canvas.create_rectangle(x, y, x + 5, y + 5, fill="black")
    elif y < 170:
        canvas.create_rectangle(x, y, x + 5, y + 5, fill="red")
    else:
        canvas.create_rectangle(x, y, x + 5, y + 5, fill="yellow")

input()
```

[zpět](../../programovani_uvod.md#úkol-13-1)