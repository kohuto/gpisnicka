```python
import random

pocet_premii = 0
predchozi_hod = 0
for i in range(10):
    hod = random.randint(1, 6)
    if hod == predchozi_hod:
        pocet_premii = pocet_premii + 1
    predchozi_hod = hod
print("Pocet prémií:", pocet_premii)
```

[zpět](../../programovani_uvod.md#úkol-9-4)