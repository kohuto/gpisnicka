```python
import random

kolik_padlo_setek = 0
kolik_padlo_jinych_cisel = 0
for i in range(10):
    hod = random.randint(1, 6)
    if hod == 6:
        kolik_padlo_sestek = kolik_padlo_sestek + 1
    else:
        kolik_padlo_jinych = kolik_padlo_jinych + 1
print("Padlo", kolik_padlo_sestek, "šestek a", kolik_padlo_jinych_cisel, "jiných čísel")
```

[zpět](../../programovani_uvod.md#úkol-8-4)