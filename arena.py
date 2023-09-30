import random


class Kostka:
    def __init__(self, pocet_sten=6):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, self.pocet_sten)


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
        return f"{self._jmeno} ma {self._zivot}hp"

    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())
        if zraneni > 0:
            zprava = f"{self._jmeno} utrpěl poškození {zraneni} hp."
            self._zivot = self._zivot - zraneni
            if self._zivot < 0:
                self._zivot = 0
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
            if self._mana > self._max_mana:
                self._mana = self._max_mana
            super().utoc(souper)
        # magický útok
        else:
            uder = self._magicky_utok + self._kostka.hod()
            zprava = f"{self._jmeno} použil magii za {uder} hp."
            self._nastav_zpravu(zprava)
            self._mana = 0
            souper.bran_se(uder)


class Arena:
    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka

    def zapas(self):
        print("Vítejte v aréně!")
        print(f"Dnes se utkají {self._bojovnik_1._jmeno} s {self._bojovnik_2._jmeno}!")
        print("Zápas může začít...")
        while self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu():
            self._bojovnik_1.utoc(self._bojovnik_2)
            print(self._bojovnik_1.vrat_zpravu())
            print(self._bojovnik_2.vrat_zpravu())
            self._bojovnik_2.utoc(self._bojovnik_1)
            print(self._bojovnik_2.vrat_zpravu())
            print(self._bojovnik_1.vrat_zpravu())
            print()


# vytvoření objektů
kostka = Kostka(10)
gandalf = Mag("Gandalf", 150, 20, 10, kostka, 30, 30)
shadow = Bojovnik("Shadow", 150, 18, 10, kostka)
arena = Arena(gandalf, shadow, kostka)
# zápas
arena.zapas()
