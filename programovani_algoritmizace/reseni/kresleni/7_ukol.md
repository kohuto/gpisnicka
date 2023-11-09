```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(10, 20, 10 + 50, 20 + 50, fill="red")
canvas.create_rectangle(150, 120, 150 + 50, 120 + 50, fill="blue")
canvas.create_rectangle(30, 70, 30 + 50, 70 + 50, fill="green")
canvas.create_rectangle(200, 100, 200 + 50, 100 + 50, fill="yellow")

input()
```
[zpět](../../programovani_uvod.md#úkol-7-2)