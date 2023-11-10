```python
import random

seznam = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    cislo = random.randint(1, 6)
    seznam[cislo - 1] = seznam[cislo - 1] + 1
print(seznam)
```

[zpět](../../programovani_uvod.md#úkol-11-3)