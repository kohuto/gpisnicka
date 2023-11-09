```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(30):
    x = random.randint(1, 21) * 10
    y = random.randint(1, 21) * 10
    canvas.create_rectangle(x, y, x + 10, y + 10, fill="black")

input()
```

[zpět](../../programovani_uvod.md#úkol-9-3)