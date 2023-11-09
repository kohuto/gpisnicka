```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x = 30
y = 30
canvas.create_rectangle(x, y, x + 100, y + 100, fill='red')
canvas.create_rectangle(x, y, x + 70, y + 70, fill='blue')
canvas.create_rectangle(x, y, x + 40, y + 40, fill='black')
input()
```
[zpět](../../programovani_uvod.md#úkol-10-1)