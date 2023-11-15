#adam
import random
kroky = int(input("Kroky:"))
vzdalenost = int(input("Vzdálenost:"))
pozice = int(vzdalenost/2)
dum = 0
trasa = []

for z in range(vzdalenost):
    trasa.append(".")
trasa[pozice] = "•"
print("dum",*trasa,"hospoda")

for i in range(kroky):
    trasa = []
    x = random.choice([0 , 1])
    for y in range(vzdalenost):
        trasa.append(".")
    if x == 1:
        pozice = pozice + 1
    else:
        pozice = pozice - 1
    if pozice == vzdalenost:
        print("dum",*trasa,"•hospoda")
        print("Matyáš je opět v hospodě")
        break
    elif pozice == dum:
        print("dum•",*trasa,"hospoda")
        print("Matyáš je doma")
        break
    else:
        trasa[pozice] = "•"
        print("dum",*trasa,"hospoda")

if i == (kroky - 1):
    print("Matyáš umřel po cestě")
    