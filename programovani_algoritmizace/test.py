import random

hod = random.randint(1, 6)
hody = [0, 0, 0, 0, 0, 0,]
hody[hod - 1] = hody[hod - 1] + 1
print(hody)

