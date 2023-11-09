```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def maly_ctverec():
    canvas.create_rectangle(10, 20, 10 + 20, 20 + 20)

def velky_ctverec():
    canvas.create_rectangle(40, 40, 40 + 80, 40 + 80)

maly_ctverec()
velky_ctverec()

input()
```

[zpět](../../programovani_uvod.md#úkol-7-3)