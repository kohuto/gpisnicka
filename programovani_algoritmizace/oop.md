# OOP

## Přehled

1. [Úvod](#úvod)
2. [Objekt, atribut, metoda](#objekt-atribut-metoda)
3. [Třída](#třída)
4. [Instance](#instance)
5. [Konstruktor](#konstruktor)
6. [Zapouzdření](#zapouzdření)
7. [Dědičnost](#dědičnost)
8. [Polymorfismus](#polymorfismus)
9. [Projekt](#projekt)
10. [Kostka](#kostka)
11. [Bojovník](#bojovník)
12. [Aréna](#aréna)
13. [Mág](#mág)

## Úvod
Poskládání programu z komponent je výhodné především kvůli snadné rozšiřitelnosti. O komponentách se ví, že fungují, jsou otestovány a udržovány. Pokud je někde chyba, stačí ji opravit na jednom místě. V rámci OOP se snažíme simulovat realitu tak, jak jsme zvyklí ji vnímat.

OOP stojí na základních třech pilířích:
Zapouzdření, Dědičnost a Polymorfismus.

## Objekt, atribut, metoda
Základní jednotkou je objekt, který odpovídá nějakému objektu (předmětu) z reálného světa. Každý objekt má své atributy a metody. Atributy objektu jsou vlastnosti neboli data, která uchovává. Metody jsou schopnosti, které umí objekt vykonávat.

## Třída
Třída je vzor, podle kterého se objekty vytváří. Definuje jejich vlastnosti a schopnosti.

## Instance
Objekt, který se vytvoří podle třídy, se nazývá
instance. Instance se navzájem liší svými daty (atributy).

## Konstruktor
Speciální metoda, která se volá při vytváření instance. Pomocí ní můžeme například vytvořit v objektu požadované atributy a uložit do nich hodnoty. V momentě, kdy nedeklarujeme konstruktor, volá se implicitní konstruktor.

## Zapouzdření 
Koncept, který omezuje přímý přístup ke komponentám (atributům a metodám) objektu a zároveň umožňuje pracovat s těmito komponentami prostřednictvím definovaných rozhraní (metod). Jinak řečeno, udržujeme atributy třídy soukromé a manipulujeme s nimi pouze pomocí veřejných metod. 

## Dědičnost 
Princip, který umožňuje vytvářet nové třídy na základě již existujících tříd. Nově vytvořená třída dědí atributy (vlastnosti) a metody (funkce) své rodičovské třídy, což umožňuje znovupoužití kódu.

## Polymorfismus 
Koncept, podle kterého mohou objekty různých tříd být ošetřeny jako objekty jedné společné nadřazené třídy. Základním principem je, že tyto objekty mohou sdílet stejný rozhraní (metody), ale způsob, jakým tyto metody implementují funkcionalitu, se může lišit v každé třídě.

## Projekt

### Kostka

Zdroj: https://www.itnetwork.cz/python/oop/

Třídy se vytvářejí klíčovým slovem `class`. Třídu pojmenujeme `Kostka`:

```python
class Kostka:
```

Přidáme do třídy metodu `hod_sest()`:

```python
class Kostka:
    def hod_sest(self):
        return 6
```
První povinný poziční argument je `self`. Do něj se vloží "odkaz" na objekt, do kterého metoda náleží. Tento argument tam vloží sám objekt.

Nyní vytvoříme instanci třídy `Kostka`:

```python
class Kostka:
    def hod_sest(self):
        return 6

kostka = Kostka()
```

> Když vytváříme objekt (instanci třídy), představíme si ho jako
speciální box. Každý box má své vlastní atributy a metody. Když chceme, aby box něco udělal, potřebujeme způsob, jak na tento konkrétní box odkazovat. A právě `self` je způsob, kterým toho dosáhneme.

Při vytvoření instance se zavolá tzv. _konstruktor_. Závorky při vytváření instance píšeme, protože _konstruktor_ je speciální metoda, voláme tedy tuto "vytvářecí" metodu.

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
import random 

class Kostka:
    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
print(kostka.hod())
```

Pojďme nyní vytvořit atribut `pocet_sten`. K tomu nám poslouží již zmíněný _konstruktor_. Víme, že to je metoda. Pomocí této metody můžeme např. vytvořit v objektu požadované atributy a uložit do nich hodnoty.

Konstruktor se deklaruje jako metoda se jménem `__init__()`:

```python
class Kostka:
    def __init__(self):
        pass

    def hod(self):
        return random.randint(1, 6)

kostka = Kostka()
```

Atributy objektů se vytvářejí slůvkem `self`. Za `self` následuje tečka a název atributu. Vytvoříme atribut `pocet_sten`:

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
> Pokud v metodě jen tak vytvoříme nějakou proměnnou, tak ta po
ukončení metody zaniká. My ale potřebujeme vytvořit atribut `pocet_sten`, který chceme dále používat. Proto použijeme `self`.

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

Není dobré atribut pocet_sten nastavit jako veřejný, protože nechceme, aby nám někdo mohl již u vytvořené kostky počet stěn měnit. Proto atribut nastavíme na neveřejný pomocí podtržítka. Pro vypsání hodnoty atributu `pocet_sten` budeme používat veřejnou metodu `vrat_pocet_sten`. Tomuto principu se říká zapouzdření.

```python
class Kostka:
    def __init__(self, pocet_sten = 6):
        self._pocet_sten = pocet_sten

    def vrat_pocet_sten(self):
        return self._pocet_sten

    def hod(self):
        return random.randint(1, 6)
```

> Aby byl atribut skutečně read-only a zvenčí nepřístupný, je potřeba použít dvě podtržítka.

Všimněte si, že nyní nemůžeme vytvořit kostku bez parametru. Lze to však obejít pomocí uvedení výchozí hodnoty argumentu pocet_sten v definici konstruktoru.

```python
class Kostka:
    def __init__(self, pocet_sten = 6):
        self._pocet_sten = pocet_sten

    def vrat_pocet_sten(self):
        return self._pocet_sten

    def hod(self):
        return random.randint(1, 6)

desetistenna = Kostka(10)
sestistenna = Kostka()
print(desetistenna.pocet_sten)
print(sestistenna.pocet_sten)
```

Poslední věc, která zbývá upravit, je metoda `hod`, a to tak, aby nejvyšší hozené číslo odpovídalo počtu stěn:

```python
class Kostka:
    def __init__(self, pocet_sten = 6):
        self._pocet_sten = pocet_sten
    
    def vrat_pocet_sten(self):
        return self._pocet_sten

    def hod(self):
        return random.randint(1, self._pocet_sten)

kostka = Kostka(10)
print(kostka.vrat_pocet_sten())
print(kostka.hod())
```

## Bojovník

Kostka je hotová, nyní potřebujeme vytvořit bojovníka do arény a samotnou arénu.

Bojovník bude mít nějaké atributy:

- jmeno
- maximální počet životů
- aktuální počet životů
- útok
- obranu (když bojovník útočí s útokem 20hp na druhého bojovníka s obranou 10hp, ubere mu 10hp života.)

Bojovník má referenci na instanci objektu `Kostka`. Při útoku či obraně si vždy hodí kostkou a k útoku/obraně přičte padlé číslo (Všichni bojovníci sdílejí jednu instanci kostky).

Bojovníci podávají zprávy o tom, co se děje - např. "Zalgoren útočí s úderem za 25hp."

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

Případně jednodušeji:

```python
def je_nazivu(self):
    return self._zivot > 0
```

Vytvořme ještě metodu, která vypíše aktuální počet životů:

```python
def zbyvajici_zivot(self):
    return "{0} má {1}hp ".format(self._jmeno, self._zivot)
```

Nyní implemetnujeme metodu `bran_se`:

1. spočítáme skutečné zranění (od útoku odečteme naši obranu zvýšenou o číslo, které padlo na hrací kostce)
2. pokud jsme zranění celé neodrazili (`zraneni` > 0), snížíme život (Je podmínka důležitá? Co kdyby obrana byla větší než útok?)

```python
def bran_se(self, uder):
    zraneni = uder - (self._obrana + self._kostka.hod())
    if zraneni > 0:
        self._zivot = self._zivot - zraneni
```

Nyní implementujeme metodu `utoc()`. Metoda `utoc()` bere jako parametr instanci bojovníka, na kterého se útočí, abychom na něm mohli zavolat metodu `bran_se()`, která na útok zareaguje a zmenší protivníkův život.

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
    self._zprava = zprava

def vrat_zpravu(self):
    return self._zprava
```

O práci se zprávami obohatíme naše metody `utoc()` a `bran_se()`, nyní budou vypadat takto:

```python
def bran_se(self, uder):
        zraneni = uder - (self._obrana + self._kostka.hod())
        if zraneni > 0:
            zprava = f"{self._jmeno} utrpěl poškození {zraneni} hp."
            self._zivot = self._zivot - zraneni
            if not je_nazivu():
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

## Aréna

Nyní bychom chtěli simulovat souboj dvou bojovníků. Pro tyto potřeby vytvoříme novou třídu `Arena`.

```python
class Arena:

    def __init__(self, bojovnik_1, bojovnik_2):
        self._bojovnik_1 = bojovnik_1
        self._bojovnik_2 = bojovnik_2
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
arena = Arena(zalgoren, shadow)
# zápas
arena.zapas()
```

Existující nedostatky:

- V cyklu s bojem útočí první bojovník na druhého. Poté však vždy útočí i druhý bojovník, nehledě na to, zda ho první nezabil.
- Druhým nedostatkem je, že bojovníci vždy bojují ve stejném pořadí, čili zde "Zalgoren" má vždy výhodu. Pojďme vnést další prvek náhody a pomocí kostky rozhodněme, který z bojovníků bude začínat.

## Mág

Nyní do naší arény přidáme postavu mága. Mág bude fungovat stejně, jako bojovník (použijeme dědičnost). Kromě života bude mít mág i manu. Zpočátku bude mana plná. V případě plné many vykoná mág magický útok, který manu vybije na 0. Každé kolo se bude mana zvyšovat o 10 a mág bude podnikat jen běžný útok. Jakmile se mana zcela doplní, opět bude moci magický útok použít.

Vytvoříme tedy třídu Mag, zdědíme ji z Bojovnik.

```python
class Mag(Bojovnik)
```

Nemůžeme použít původní konstruktor potomka, neboť máme u mága 2 parametry navíc (mana a magický útok). Definujeme si tedy konstruktor v potomkovi, který bere parametry potřebné pro vytvoření bojovníka a několik parametrů navíc pro mága.

> U potomků není nutné vždy volat konstruktor předka. Náš potomek má ale některé parametry navíc, proto ho volat budeme. Některé parametry předáme předkovi a některé si zpracujeme sami. Konstruktor předka se vykoná před naším konstruktorem. Předání parametrů předkovi (volání konstruktoru předka) zajistí metoda `super()`.

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
        uder = self._utok + self._kostka.hod()
        zprava = f"{self._jmeno} útočí s úderem za {uder} hp."
        self._nastav_zpravu(zprava)
    # magický útok
    else:
        uder = self._magicky_utok + self._kostka.hod()
        zprava = f"{self._jmeno} použil magii za {uder} hp."
        self._nastav_zpravu(zprava)
        self._mana = 0
    souper.bran_se(uder)
```

Celý kód je k dispozici [zde](arena.md)
