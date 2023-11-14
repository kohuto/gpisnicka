import random
def o_prochazka(vzdalenost,max_pocet_kroku):
    zacatek = vzdalenost//2
    doprava_doleva = [-1,1]

    print('home ' + ('. ' * (zacatek)) + '* ' + ('. ' * (vzdalenost-zacatek-1)) + 'pub')

    pocet = 0
    pokracuj = True
    while pokracuj:
        
        smer = random.choice(doprava_doleva)
        zacatek += smer
        pocet += 1

        print('home ' + ('. ' * (zacatek)) + '* ' + ('. ' * (vzdalenost-zacatek-1)) + 'pub')

        if zacatek == 0:
            print('Ended up at home')
            pokracuj = False
        elif zacatek == vzdalenost - 1:
            print('Ended up in the pub')
            pokracuj = False
        elif pocet == max_pocet_kroku:
             print('End')
             pokracuj = False
        
        

o_prochazka(15,100)
