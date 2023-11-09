```python
import random
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

for i in range(10):
    x = i * 40
    canvas.create_rectangle(x, 10, x + 30, 10 + 30, fill="red")

input()
```

[zpět](../../programovani_uvod.md#úkol-13)