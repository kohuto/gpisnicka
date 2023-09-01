## OOP

znovupoužitel­nost
vynálezu základních
komponent
Poskládání programu z komponent je výhodnější a levnější. Můžeme
mu věřit, je otestovaný (o komponentách se ví, že fungují, jsou
otestovány a udržovány)
Pokud je někde chyba, stačí ji opravit na
jednom místě.
snažíme se nasimulovat realitu tak, jak ji jsme
zvyklí vnímat.

Základní jednotkou je objekt, který odpovídá nějakému
Každý objekt má své atributy a metody.

Atributy objektu jsou vlastnosti neboli
data, která uchovává

Metody jsou schopnostmi, které umí objekt
vykonávat.

Třída je
vzor, podle kterého se objekty vytváří. Definuje jejich vlastnosti a schopnosti.

Objekt, který se vytvoří podle třídy, se nazývá
instance.
instance se navzájem liší svými daty (atributy)

OOP stojí na základních třech pilířích:
Zapouzdření, Dědičnost a Polymorfismus.

## a

Třídy se vytvářejí klíčovým slovem `class`. Třídu pojmenujeme `Kostka`

```python
class Kostka:
```

Přidáme do třídy metodu `hod_sest()`:

```python
class Kostka:
    def hod_sest(self):
        return 6
```

Nyní vytvoříme instanci třídy `Kostka`:

```python
class Kostka:
    def hod_sest(self):
        return 6

kostka = Kostka()
```

Při vytvoření instance se zavolá tzv. _konstruktor_.
Závorky při vytváření instance píšeme, protože _konstruktor_ je speciální metoda, voláme tedy tuto "vytvářecí" metodu.

My jsme zatím konstruktor nedeklarovali, proto se vytvořil tzv. _implicitní (prázdný) konstruktor_.

V proměnné `kostka` máme uloženou instanci třídy `Kostka`. Můžeme proto zavolat metodu `hod_sest()`:

```python
class Kostka:
    def hod_sest(self):
        return 6

kostka = Kostka()
print(kostka.hod_sest())
```

Taková kostka by byla nepraktická. Místo metody `hod_sest` vytvořte metodu `hod`, která bude vracet náhodné číslo od 1 do 6:

```python
class Kostka:
    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
print(kostka.hod())
```

Pojďme nyní vytvořit atribut `pocet_sten`. K tomu nám poslouží již zmíněný _konstruktor_. Víme, že to je metoda.
Pomocí této metody můžeme např. vytvořit v objektu požadované atributy a uložit do nich hodnoty.

Konstruktor se deklaruje jako metoda se jménem `__init__()`:

```python
class Kostka:
    def __init__(self):
        pass

    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
```

Atributy objektů se vytvářejí slůvkem `self`. Za self následuje tečka a název atributu. Vytvoříme atribut `pocet_sten`:

```python
class Kostka:
    def __init__(self):
        self.pocet_sten = 6

    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
```

Hodnotu atributu můžeme nyní vypsat:

```python
class Kostka:
    def __init__(self):
        self.pocet_sten = 6

    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
print(kostka.pocet_sten)
```

Konstruktor (jako každá metoda) může mít parametry. Díky tomu můžeme například nastavit, kolik stěn bude mít kostka:

```python
class Kostka:
    def __init__(self, pocet_sten):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
print(kostka.pocet_sten)
```

Nyní, když zavoláme konstruktor, tak se hodnota parametru `pocet_sten` dosadí do atributu `pocet_sten` (ano, je to trochu matoucí, ale pojmenovávat atribut a parametr stejně je dobrým zvykem):

```python
class Kostka:
    def __init__(self, pocet_sten):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, 6)

kostka = Kostka(10)
print(kostka.pocet_sten)
```

Všimněte si, že nyní nemůžeme vytvořit kostku bez parametru. Lze to však obejít pomocí uvedení výchozí hodnoty argumentu pocet_sten v definici konstruktoru.

```python
class Kostka:
    def __init__(self, pocet_sten = 6):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, 6)

desetistenna = Kostka(10)
sestistenna = Kostka()
print(desetistenna.pocet_sten)
print(sestistenna.pocet_sten)
```

Poslední věc, která zbývá upravit, je metoda `hod`. Upravte ji tak, aby nejvyšší hozené číslo odpovídalo počtu stěn. Pokud nyní parametr nenastavíme, dosadí se do atributu `pocet_sten` výchozí hodnota:

```python
class Kostka:
    def __init__(self, pocet_sten = 6):
        self.pocet_sten = pocet_sten

    def hod(self):
        return random.randint(1, self.pocet_sten)

kostka = Kostka(10)
print(kostka.pocet_sten)
```

Kostka je hotová, nyní potřebujeme vytvořit bojovníka do arény a samotnou arénu.

Bojovník bude mít nějaké atributy:

- maximální počet životů
- aktuální počet životů
- útok
- obranu (když bojovník útočí s útokem 20hp na druhého bojovníka s obranou 10hp, ubere mu 10hp
  života.)

Bojovník má referenci na instanci objektu
Kostka. Při útoku či obraně si vždy hodí kostkou a k útoku/obraně přičte padlé číslo. (Všichni bojovníci sdílejí jednu instanci kostky).

Bojovníci podávají zprávy o tom, co se děje - např.
"Zalgoren útočí s úderem za 25hp."

Vytvořme kostruktor:

```python
class Bojovnik:
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        self._jmeno = jmeno
        self._zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
```

Dále se bude hodit metoda `je_nazivu`:

```python
def je_nazivu(self):
    if self._zivot > 0:
       return True
    else:
       return False
```

_Úkol: lze předchozí metodu zjednodušit?_

```python
def je_nazivu(self):
    return self.zivot > 0
```

Vytvořme ještě metodu, která vypíše aktuální počet životů:

```python
def zbyvajici_zivot(self):
    return "{0} má {1}hp ".format(self._jmeno, zivot)
```

Nyní implemetnujeme metodu `bran_se`:

1. spočítáme skutečné zranění (od útoku odečteme naši obranu zvýšenou o číslo, které padlo na hrací kostce)
2. Pokud jsme zranění celé neodrazili (`zraneni` > 0), snížíme život (úkol: je tato podmínka důležitá? Co kdyby obrana byla větší než útok?)
3. když je snížený život <0, dorovnáme ho na nulu

```python
def bran_se(self, uder):
    zraneni = uder - (self._obrana + self._kostka.hod())
    if zraneni > 0:
        self._zivot = self._zivot - zraneni
        if self._zivot < 0:
            self._zivot = 0
```

Nyní implementujeme metodu `utoc`. Metoda `utoc()` bere jako parametr instanci bojovníka, na kterého se útočí, abychom na něm mohli zavolat metodu `bran_se()`, která na útok zareaguje a zmenší protivníkův život.

```python
def utoc(self, souper):
    uder = self._utok + self._kostka.hod()
    souper.bran_se(uder)
```

Nakonec bychom chtěli umět vypisovat zprávy (aby z toho uživatel něco měl). Z praktických důvodů není hezké, aby se o to staraly metody `utoc()` a `bran_se()`. Proto vytvoříme novou proměnnou v metodě `__init__`, do které budeme text zprávy ukládat:

```python
self._zprava = ""
```

Vytvoříme také dvě nové metody `nastav_zpravu()` a `vrat_zpravu()`. První bere jako parametr text zprávy, který uloží do proměnné `zprava`. Druhá bude jednoudeš vracet obsah této proměnné. O práci se zprávami obohatíme naše metody utoc() a
bran_se(), nyní budou vypadat takto:

```python
def bran_se(self, uder):
    zraneni = uder - (self._obrana + self._kostka.hod())
    if zraneni > 0:
        zprava = "{0} utrpěl poškození {1} hp.".format(self._jmeno, zraneni)
        self._zivot = self._zivot - zraneni
        if self._zivot < 0:
            self._zivot = 0
            zprava = zprava[:-1] + " a zemřel."
    else:
        zprava = "{0} odrazil útok.".format(self._jmeno)
    self._nastav_zpravu(zprava)

def utoc(self, souper):
    uder = self._utok + self._kostka.hod()
    zprava = "{0} útočí s úderem za {1} hp.".format(self._jmeno, uder)
    self._nastav_zpravu(zprava)
    souper.bran_se(uder)
```

Bojovníci jsou hotoví, nyní je můžeme vyzkoušet:

```python
kostka = Kostka(10)
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
souper = Bojovnik("Shadow", 60, 18, 15, kostka)
souper.utoc(bojovnik)
print(souper.vrat_posledni_zpravu())
print(bojovnik.vrat_posledni_zpravu())
```

Nyní bychom chtěli simulovat souboj dvou bojovníků. Pro tyto potřeby vytvoříme novou třídu `Arena`.

```python
class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka
```

Zamysleme se nad metodami. Z veřejných metod bude určitě potřeba jen ta
k simulaci zápasu. Výstup programu na konzoli uděláme trochu na úrovni a
také umožníme třídě Arena, aby přímo ke konzoli
přistupovala. Rozhodli jsme se, že výpis bude v kompetenci třídy, jelikož
se nám to zde vyplatí. Naopak kdyby výpis prováděli i bojovníci, bylo by
to na škodu. Potřebujeme tedy metodu, která vykreslí obrazovku s
aktuálními údaji o kole a životy bojovníků. Zprávy o útoku a obraně
budeme chtít vypisovat s dramatickou pauzou, aby byl výsledný efekt lepší,
uděláme si pro takový typ zprávy ještě pomocnou metodu. Začněme s
vykreslením informační obrazovky:
Zdroj: https://www.itnetwork.cz/python/oop/python-tutorial-arena-s-objektovymi-bojovniky

```python
def _vykresli(self):
    slf._vycisti_obrazovku()
    print("-------------- Aréna -------------- \n")
    print("Zdraví bojovníků: \n")
    print("{0} {1}".format(self._bojovnik_1,
                           self._bojovnik_1.graficky_zivot()))
    print("{0} {1}".format(self._bojovnik_2,
                           self._bojovnik_2.graficky_zivot()))
```

Přesuneme se již k samotnému zápasu. Metoda `zapas()` nebude
mít žádné parametry a nebude ani nic vracet. Uvnitř bude cyklus, který bude na střídačku volat útoky bojovníků navzájem a vypisovat informační obrazovku a zprávy. Metoda by mohla vypadat takto:

```python
def zapas(self):
    print("Vítejte v aréně!")
    print("Dnes se utkají {0} s {1}!".format(self._bojovnik_1, self._bojovnik_2))
    print("Zápas může začít...", end=" ")
    input()
    # cyklus s bojem
    while (self._bojovnik_1.je_nazivu() and self._bojovnik_2.je_nazivu()):
        self._bojovnik_1.utoc(self._bojovnik_2)
        self._vykresli()
        self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
        self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
        self._bojovnik_2.utoc(self._bojovnik_1)
        self._vykresli()
        self._vypis_zpravu(self._bojovnik_2.vrat_posledni_zpravu())
        self._vypis_zpravu(self._bojovnik_1.vrat_posledni_zpravu())
        print("")
```

Nyní můžeme odstartovat zápas:

```python
# vytvoření objektů
kostka = Kostka(10)
zalgoren = Bojovnik("Zalgoren", 100, 20, 10, kostka)
shadow = Bojovnik("Shadow", 60, 18, 15, kostka)
arena = Arena(zalgoren, shadow, kostka)
# zápas
arena.zapas()
```

Existující nedostatky:

- V cyklu s bojem útočí první bojovník na druhého. Poté však vždy
  útočí i druhý bojovník, nehledě na to, zda ho první nezabil.
- Druhým nedostatkem je, že bojovníci vždy bojují ve stejném pořadí,
  čili zde "Zalgoren" má vždy výhodu. Pojďme vnést další prvek náhody a pomocí kostky rozhodněme, který z bojovníků bude začínat.
