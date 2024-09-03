
import random

class Kostka:
    def __init__(self, pocet_sten = 6):
        self._pocet_sten = pocet_sten
    
    def vrat_pocet_sten(self):
        return self._pocet_sten

    def hod(self):
        return random.randint(1, self._pocet_sten)

class Bojovnik:
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._zprava = ""
    
    def je_nazivu(self):
        return self._zivot > 0
    
    def zbyvajici_zivot(self):
        return "{0} má {1}hp ".format(self._jmeno, self._zivot)
    
    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())
        if zraneni > 0:
            zprava = f"{self._jmeno} utrpěl poškození {zraneni} hp."
            self._zivot -= zraneni
            if not self.je_nazivu():
                zprava += ".. a zemřel."
        else:
            zprava = f"{self._jmeno} odrazil útok."
        self._nastav_zpravu(zprava)

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        zprava = f"{self._jmeno} útočí s úderem za {uder} hp."
        self._nastav_zpravu(zprava)
        souper.bran_se(uder)

    def _nastav_zpravu(self, zprava):
        self._zprava = zprava
    
    def vrat_zpravu(self):
        return self._zprava

class Arena:

    def __init__(self, bojovnik_1, bojovnik_2):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2

    def zapas(self):
        print("Vítejte v aréně!")
        print("Dnes se utkají {0} s {1}!".format(self._bojovnik_1, self._bojovnik_2))
        print("Zápas může začít...")
        # cyklus s bojem
        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            print(self._bojovnik_1.vrat_zpravu())
            print(self._bojovnik_2.vrat_zpravu())
            self._bojovnik_2.utoc(self._bojovnik_1)
            print(self._bojovnik_2.vrat_zpravu())
            print(self._bojovnik_1.vrat_zpravu())
            print()

class Mag(Bojovnik):
    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magicky_utok = magicky_utok

    def utoc(self, souper):
        # mana není naplněna
        if self._mana < self._max_mana:
            self._mana = self._mana + 10
            uder = self._utok + self._kostka.hod()
            zprava = f"{self._jmeno} útočí s úderem za {uder} hp."
            self._nastav_zpravu(zprava)
        #magický útok
        else:
            uder = self._magicky_utok + self._kostka.hod()
            zprava = f"{self._jmeno} použil magii za {uder} hp."
            self._nastav_zpravu(zprava)
            self._mana = 0
        souper.bran_se(uder)

# vytvoření objektů
kostka = Kostka(10)
zalgoren = Bojovnik("Zalgoren", 100, 20, 10, kostka)
gandalf = Mag("Gandalf", 60, 18, 15, kostka, 50, 50)
arena = Arena(zalgoren, gandalf)
# zápas
arena.zapas()
