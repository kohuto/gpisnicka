```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

a = 50
b = 100
if a < b:
    canvas.create_rectangle(10, 10, 10 + b, 10 + a, fill="red")
else:
    canvas.create_rectangle(10, 10, 10 + b, 10 + a, fill="red")
    
input()
```

[zpět](../../programovani_uvod.md#úkol-6-6)