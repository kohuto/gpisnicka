# OOP

## Přehled

1. [Úvod](#úvod)
2. [Třída](#třída)
3. [Metody](#metody)
4. [Atributy](#atributy)
5. [Instance](#instance)
6. [Konstruktor](#konstruktor)
7. [Simulace]()

## Úvod

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

## Třída

## Metody

## Atributy

## Instance

## Konstruktor

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

Vytvoříme také dvě nové metody `_nastav_zpravu()` a `vrat_zpravu()`. První bere jako parametr text zprávy, který uloží do proměnné `zprava`. Druhá bude jednoduše vracet obsah této proměnné.

```python
def _nastav_zpravu(self, zprava):
    self.zprava = zprava

def vrat_zpravu(self):
    return self.zprava
```

O práci se zprávami obohatíme naše metody `utoc()` a `bran_se()`, nyní budou vypadat takto:

```python
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
```

Bojovníci jsou hotoví, nyní je můžeme vyzkoušet:

```python
kostka = Kostka(10)
bojovnik = Bojovnik("Zalgoren", 100, 20, 10, kostka)
souper = Bojovnik("Shadow", 60, 18, 15, kostka)
souper.utoc(bojovnik)
print(souper.vrat_zpravu())
print(bojovnik.vrat_zpravu())
```

Nyní bychom chtěli simulovat souboj dvou bojovníků. Pro tyto potřeby vytvoříme novou třídu `Arena`.

```python
class Arena:

    def __init__(self, bojovnik_1, bojovnik_2, kostka):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
        self._kostka = kostka
```

Uvnitř arény vytvoříme jednu metodu `zapas()`. Metoda `zapas()` nebude mít žádné parametry a nebude ani nic vracet. Uvnitř bude cyklus, který bude na střídačku volat útoky bojovníků navzájem a vypisovat zprávy. Metoda by mohla vypadat takto:

```python
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

- V cyklu s bojem útočí první bojovník na druhého. Poté však vždy útočí i druhý bojovník, nehledě na to, zda ho první nezabil.
- Druhým nedostatkem je, že bojovníci vždy bojují ve stejném pořadí, čili zde "Zalgoren" má vždy výhodu. Pojďme vnést další prvek náhody a pomocí kostky rozhodněme, který z bojovníků bude začínat.

Nyní do naší arény přidáme postavu mága. Mág bude fungovat stejně, jako bojovník. Kromě života bude mít však i manu. Zpočátku bude mana plná. V případě plné many vykoná mág magický útok, který manu vybije na 0. Každé kolo se bude mana zvyšovat o 10 a mág bude podnikat jen běžný útok. Jakmile se mana zcela doplní, opět bude moci magický útok použít.

Vytvoříme tedy třídu Mag, zdědíme ji z Bojovnik.

```python
class Mag(Bojovnik)
```

Nemůžeme použít původní konstruktor potomka, neboť máme u mága 2 parametry navíc (mana a magický útok). Definujeme si tedy konstruktor v potomkovi, který bere parametry potřebné pro vytvoření bojovníka a několik parametrů navíc pro mága.

```python
def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
    super().__init__(jmeno, zivot, utok, obrana, kostka)
    self._mana = mana
    self._max_mana = mana
    self._magicky_utok = magicky_utok
```

Chceme aby `Arena` mohla pracovat s mágem stejně jako s bojovníkem (_Polymorfismus_). Aréna volá metodu `utoc()` se soupeřem v parametru nezávisle na tom, jestli bude útok vykonávat bojovník nebo mág. U mága si tedy přepíšeme metodu `utoc()` z předka tak, aby útok pracoval s manou - podle hodnoty many buď provedeme útok běžný nebo magický. Poté buď snížíme manu na 0 nebo zvýšíme o 10 (podle toho, jaký typ útok proběhl).

```python
def utoc(self, souper):
    # mana není naplněna
    if self._mana < self._max_mana:
        self._mana = self._mana + 10
        if self._mana > self._max_mana:
            self._mana = self._max_mana
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
```

Útok výše v podstatě vykonává původní metoda `utoc()`. Proto použijeme opět `super()`.

```python
def utoc(self, souper):
    # mana není naplněna
    if self._mana < self._max_mana:
        self._mana = self._mana + 10
        if self._mana > self._max_mana:
            self._mana = self._max_mana
        super().utoc(souper)
    #magický útok
    else:
        uder = self._magicky_utok + self._kostka.hod()
        zprava = "{0} použil magii za {1} hp.".format(self._jmeno, uder)
        self._nastav_zpravu(zprava)
        self._mana = 0
        souper.bran_se(uder)
```

## Simulace

### Cesta autobusem

Napište program, který simuluje cestu autobusem skrze několik zastávek. Autobus má omezenou kapacitu. Na každé zastávce může přijímat a vypouštět cestující. Na každé zastávce je vytovřen náhodný počet nastupujících lidí. Každý cestující má určenou zastávku, na které vystoupí. Na konečné stanici autobusu vystoupí všichni.

### Ekosystém

Napište program, který simuluje ekosystém. Ekosystém je reprezentován jako 2D mřížka. Každé políčko je buď prázdné, nebo je na něm strom, nebo je na něm zvíře. Na začátku je na různá místa v mřížce náhodně umístěněno několik stromů a několik zvířat. Zvířata se živí stromy, vždy, když zvíře sní strom, doplní svou energii na maximum. Pokud v dané kroku zvíře nesní strom, klesne mu energie o 1. V každém kroku se zvíře přesune na jedno ze sousedních políček. Pokud je na novém políčku strom, zvíře ho sní. V každém kroku na několika náhodných místech vyroste nový strom.

### Lesní požár

Napište program, který simuluje šíření lesního požáru v 2D mřížce. Každé políčko mřížky může být prázdné, obsahovat strom nebo být v plamenech. V každém kroku se požár rozšíří na vedlější políčko, pokud je na vedlejším políčku strom. V každém kroku na několika náhodných políčcích vyroste nový strom. Každých několik kroků se vybere náhodné políčko, kde vznikne požár.

### Epidemiologické šíření

Napište program, který simuluje šíření infekčního onemocnění v populaci. Na začátku je vytvořena populace několika osob. Některé z nich jsou na začátku nakaženy. V každém kroku se vybere několik dvojic lidí, které se spolu potkaly. Pro každou dvojici platí následující pravidla:

- pokud jsou obě osoby v dvojici zdravé, nic se neděje
- pokud jsou obě osoby v dvojici nakažené, nic se neděje
- pokud je jedna osoba ve dvojici nakažená a druhá zdravá, pak se zdravá osoba s určitou pravděpodobností nakazí

Každá osoba se po uplynutí určité doby uzdraví a získává rezistenci.

### Obchodní centrum

Napište program, který simuluje chování zákazníků v obchodním centru. V centru máme několik obchodů. Na začátku simulace se vygeneruje určitý počet zákazníků. Každý zákazník má seznam obchodů, které musí navštívit. Také má každý zákazník nastavenou trpělivost, jak dlouho dokáže stát ve frontě. Zákazník navštěvuje obchody podle toho, jak jsou napsané v seznamu. Vždy přijde do obchodu, postaví se do fronty a čeká. Pokud mu dojde trpělivost ve frontě, přechází do dalšího obchodu (později se však do daného ochodu vrátí). V každém kroku simulace se fronta zákazníků zmenší o jednoho zákazníka (v každém kroku je jeden zákazník obsloužen). Kdžy je zákazník obsloužen, přechází do dalšího obchodu ze seznamu, případně odchází z obchodního centra, když navštívil všechny obchody.

### Úkol 6

call centrum:

customers_handled

class CallCenter:
def **init**()
num_employees =
def support(self, cutomer):
random_time()
print(support finished)
customer_handled += 1

class Customer>=:
print(customer enters waiting queue at {time})
def enter_call():
print(customer enters call at {time})
def left_call(customer left call at {time})

def simulate_call_center()
call_center = CallCenter()
for time in range (sim_time):
...

number of employees
customer_interval
sim_time
simulate_call_center()

### ÚKOL 7

Napište program, který simuluje převoz písku. V místě
