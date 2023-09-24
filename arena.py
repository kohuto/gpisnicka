import random


class Kostka:
    def __init__(self, pocet_sten=6):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, self.pocet_sten)


class Bojovnik:
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self.jmeno = jmeno
        self.zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._zprava = ""

    def je_nazivu(self):
        return self.zivot > 0

    def zbyvajici_zivot(self):
        return f"{self.jmeno} ma {self.zivot}hp"

    def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())
        if zraneni > 0:
            self._zivot = self._zivot - zraneni
            if self._zivot < 0:
                self._zivot = 0

    def utoc(self, souper):
        uder = self._utok + self._kostka.hod()
        souper.bran_se(uder)


kostka = Kostka(10)
print(kostka.hod())
print(kostka.pocet_sten)
