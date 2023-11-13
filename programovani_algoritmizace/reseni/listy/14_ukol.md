```python
import random

seznam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1000):
    prvni_cislo = random.randint(1, 6)
    druhe_cislo = random.randint(1, 6)
    soucet = prvni_cislo + druhe_cislo
    seznam[soucet - 2] = seznam[soucet - 2] + 1
print(seznam)
```

[zpět](../../programovani_uvod.md#úkol-14-3)