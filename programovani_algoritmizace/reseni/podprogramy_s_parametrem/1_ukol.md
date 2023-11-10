```python
import tkinter
canvas = tkinter.Canvas()
canvas.pack()

def velkyCtverec():
    canvas.create_rectangle( 50, 60, 50 + 100, 60 + 100)
def stredniCtverec():
    canvas.create_rectangle( 50, 60, 50 + 70, 60 + 70)
def malyCtverec():
    canvas.create_rectangle( 50, 60, 50 + 40, 60 + 40)

input()
```

[zpět](../../programovani_uvod.md#úkol-1-7)