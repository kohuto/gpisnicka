#maxim
import random

#inputy
vzdalenost = int(input("Vzdalenost od domu: "))
doba = int(input("Doba do usnutí: "))

#obsah pole
b = "_"
x = "x"

#vytvoření list
chuze_list = []
for _ in range(2 * vzdalenost):
    chuze_list.append(b)

#dotvoření listu + tisk
chuze_list.insert(vzdalenost,x)
print("domov", chuze_list ,"hospoda")

#nahoda
move_list = (1,-1)
pohyb = random.choice(move_list)

#zjisteni kde v listu je x
r = chuze_list.index(x)



chuze_list[r], chuze_list[r + pohyb] = chuze_list[r + pohyb], chuze_list[r]         #prohození 2 elementů v listu
print("domov", chuze_list ,"hospoda")


def main(pohyb,r):
    for i in range(doba - 2):
        
        chuze_list[r], chuze_list[r + pohyb] = chuze_list[r + pohyb], chuze_list[r]         #prohození 2 elementů v listu

        if  i < doba and vzdalenost == 0:

            print("domov")
            exit()
        elif i < doba and vzdalenost == (2 * vzdalenost):
            
            print("hospoda")
            exit()
        elif i == doba:

            print("usnul")
            exit()

        print("domov", chuze_list ,"hospoda")

        pohyb = random.choice(move_list)
        r = chuze_list.index(x)                 #zjisteni kde v listu je x


main(pohyb,r)
input()