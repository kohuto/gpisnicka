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

- V cyklu s bojem útočí první bojovník na druhého. Poté však vždy
  útočí i druhý bojovník, nehledě na to, zda ho první nezabil.
- Druhým nedostatkem je, že bojovníci vždy bojují ve stejném pořadí,
  čili zde "Zalgoren" má vždy výhodu. Pojďme vnést další prvek náhody a pomocí kostky rozhodněme, který z bojovníků bude začínat.

## Simulace

### Úkol 1

Zadání:
Napište program, který simuluje cestu autobusem skrze několik zastávek. Autobus má omezenou kapacitu pro cestující a může přijímat a vypouštět cestující na každé zastávce. Každý cestující má určenou cílovou zastávku, na které má vystoupit.

Vytvořte třídu `Person`, která bude reprezentovat cestujícího. Tato třída by měla mít následující atributy:

- `passenger_number`: Unikátní číslo cestujícího.
- `destination_stop`: Číslo zastávky, na které má cestující vystoupit.

Vytvořte třídu `Bus`, která bude reprezentovat autobus. Tato třída by měla mít následující atributy:

- `num_stops`: Celkový počet zastávek na trase autobusu.
- `capacity`: Maximální kapacita autobusu pro cestující.
- `passengers`: Seznam obsahující instance třídy `Person`, které jsou právě uvnitř autobusu.
- `boarded_passengers`: Seznam obsahující instance třídy `Person`, které nastoupily na aktuální zastávce.

Třída `Bus` by měla mít následující metody:

- `board_passengers(self, num_passengers, stop)`: Metoda pro nástup cestujících na autobus na dané zastávce. Parametr `num_passengers` určuje počet cestujících, kteří nastoupí. Cestující by měli být vytvořeni s náhodnými cílovými zastávkami od aktuální zastávky až po poslední zastávku. Metoda by měla aktualizovat seznam `passengers` a `boarded_passengers`.
- `disembark_passengers(self, current_stop)`: Metoda pro výstup cestujících z autobusu na dané zastávce. Cestující, jejichž cílová zastávka je aktuální zastávkou, by měli být odebráni ze seznamu `passengers`.
- `report_status(self, current_stop)`: Metoda pro výpis informací o aktuálním stavu autobusu na zastávce. Zahrnuje informace o nastoupených cestujících (`boarded_passengers`) a cestujících v autobuse (`passengers`).

Nakonec napište funkci `simulate_bus_trip(num_stops, capacity)`, která simuluje cestu autobusem skrze zastávky. Parametr `num_stops` určuje celkový počet zastávek a parametr `capacity` určuje maximální kapacitu autobusu. Funkce by měla vytvořit instanci třídy `Bus` a simulovat cestu autobusem skrze jednotlivé zastávky.

**Poznámka:** Ujistěte se, že student správně implementuje všechny metody a že výstupy z funkce `simulate_bus_trip` budou podobné těm výstupům, které generuje poskytnutý kód.

### Úkol 2

Napište program, který simuluje ekosystém na malém ostrůvku. Na ostrůvku žijí různí druhy zvířat, kteří interagují mezi sebou a s prostředím. Vytvořte třídy pro různé druhy zvířat, umožněte jim hledat potravu, rozmnožovat se a interagovat s jinými zvířaty.

Zadání:

1. Vytvořte třídu `Animal`, která bude reprezentovat zvíře v ekosystému. Tato třída by měla obsahovat alespoň následující atributy:

   - `species`: Druh zvířete.
   - `age`: Věk zvířete.
   - `hunger_level`: Úroveň hladu zvířete.
   - `is_alive`: Informace o tom, zda je zvíře stále naživu.

2. Vytvořte třídy pro různé druhy zvířat, například `Lion`, `Gazelle`, `Tree`, atd. Každá třída by měla dědit z třídy `Animal` a měla by mít specifické metody, které modelují chování daného druhu v ekosystému. Například `Lion` by mohl loviti `Gazelle`, `Gazelle` by mohla hledat potravu a množit se, `Tree` by mohlo sloužit jako útočiště, atd.

3. Implementujte třídu `Ecosystem`, která bude reprezentovat celý ekosystém na ostrůvku. Tato třída by měla obsahovat seznam zvířat a prostředí na ostrůvku.

4. Napište funkci `simulate_ecosystem(num_steps)`, která bude simulovat vývoj ekosystému na ostrůvku po určitý počet kroků. V každém kroku by měly zvířata provádět různé akce, jako hledání potravy, rozmnožování a interakce s prostředím a jinými zvířaty. Funkce by měla vypisovat stav ekosystému v každém kroku.

MOŽNÁ BY STÁLO ZA TO VYTVOŘIT 2D GRID, KDY NA ZAČÁTKU BY BYLY NÁHODNĚ ROZMÍSTĚNÉ POSTAVY. V KAŽDÉM KROKU SIMULACE SE FIGURKA PŘESUNE NA VEDLEJŠÍ POLE. POKUD SE SEJDOU DVA NA JEDNOM POLI, POSTUPUJE SE NÁSLEDOVNĚ:

- POKUD SE POTKAJÍ DVA STEJNÉ DRUHY, ROZMNOŽÍ SE
- POKUD JSOU DRUHY ROZDÍLNÉ ALE BÝLOŽRAVCI, NIC SE NEDĚJE
- POKUD JSOU DRUHY ROZDÍLNÉ, JEDEN MASOŽRAVEC A DRUHÝ BÝLOŽRAVEC, TAK BÝLOŽRAVEC UMÍRÁ
  MASOŽRAVEC MUSÍ PRAVIDELNĚ ŽRÁT, JINAK PO URČITÉ DOBĚ UMŘE. BÝLOŽRAVCI ROVNĚŽ. V KAŽDÉ ITERACI VYROSTE NÁHODNĚ NÁHODNÝ POČET STROMŮ. ZABRAŇUJE TO PŘEMNOŽENÍ BÝLOŽRAVCŮ.

### Úkol 3

Napište program, který simuluje šíření lesního požáru v 2D mřížce. Každé políčko mřížky může být prázdné, obsahovat strom nebo být v plamenech. Požár se může šířit mezi stromy, a pokud je políčko s ohněm vedle stromu, ten se také zapálí.

Zadání:

1. Vytvořte třídu `Cell`, která bude reprezentovat jedno políčko v 2D mřížce. Tato třída by měla mít atributy pro stav políčka (prázdné, strom, oheň).

2. Napište funkci `simulate_fire_spread(grid_size, num_trees, num_iterations)`, která bude simulovat šíření lesního požáru v zadané 2D mřížce. Parametr `grid_size` určuje velikost mřížky, `num_trees` určuje počet stromů přidaných v každé iteraci simulace a `num_iterations` určuje počet iterací simulace. Parametr `fire_frequency` určuje, jak často vzinkne jeden požár (pokud je parametr nastaven na 5, tak vznikne jeden oheň každých 5 iterací)

Pravidla simulace:

- V každé iteraci se náhodně vybere několik políček, na kterých vyroste nový strom.
- Pokud je čas (podle parametru `fire_frequency` na založení požáru, vybere se jedno políčko, kde vyroste nový strom)
- Pokud je políčko s ohněm, šíří se oheň na sousední stromy (pokud jsou, vždy na vzdálenost max jedno políčko do stran, dopředu a dozadu a do uhlopříčky.).
- Ohněm zapálené stromy se v další iteraci stávají ohněm.
- PRvní políčko s ohněm zapálí okolní políčka a následně se stává prázdným políčkem.

### Úkol 4

**Simulace Epidemiologického Šíření:**

Napište program, který simuluje šíření infekčního onemocnění v populaci. Jednotlivé osoby budou interagovat a může dojít k přenosu infekce. Simulace bude sledovat šíření onemocnění skrze několik kroků.

Zadání:

1. Vytvořte třídu `Person`, která bude reprezentovat jednotlivé osoby v populaci. Tato třída by měla mít atributy pro:
   - `status`: Stav osoby (zdravá, nakažená, uzdravená).
   - `infection_time`: Čas, kdy se osoba nakazila.
   - `recovery_time`: Doba, po které se osoba uzdraví.
2. Implementujte třídu `Population`, která bude reprezentovat populaci osob. Tato třída by měla obsahovat seznam osob a metody pro:

   - Náhodný výběr osob pro nákazu.
   - Šíření infekce mezi osobami na základě pravidel.
   - Uzdravování osob po určité době.

3. Napište funkci `simulate_epidemic(population_size, infection_rate, recovery_time, num_steps)`, která bude simulovat šíření infekčního onemocnění v populaci. Parametr `population_size` určuje velikost populace, `infection_rate` určuje pravděpodobnost přenosu infekce mezi osobami, `recovery_time` určuje dobu, po které se osoba uzdraví, a `num_steps` určuje počet kroků simulace.

Pravidla simulace:

- Na začátku jsou některé osoby náhodně nakazeny.
- V každé iteraci se náhodně vybere několik osob pro přenos infekce.
- Infekce se šíří mezi nakaženými a zdravými osobami s určitou pravděpodobností.
- Osoby se uzdravují po uplynutí určité doby.

**Poznámka:** Ujistěte se, že student správně implementuje třídy pro osoby a populaci, včetně metod pro šíření infekce a uzdravování osob. Funkce `simulate_epidemic` by měla simulovat šíření onemocnění a vypisovat stav populace v každé iteraci.

### Úkol 5

**Simulace Obchodního Centra:**

Napište program, který simuluje chování zákazníků v obchodním centru. Zákazníci budou vstupovat do obchodů, nakupovat zboží a interagovat s ostatními zákazníky. Simulace bude sledovat, jak se lidé pohybují mezi obchody a jak se jednotlivé interakce odrážejí na celkovém průběhu dne.

Zadání:

1. Vytvořte třídu `Customer`, která bude reprezentovat jednotlivé zákazníky v obchodním centru. Tato třída by měla mít atributy pro:
   - `id`: Unikátní identifikátor zákazníka.
   - `shopping_list`: Seznam zboží, které zákazník chce nakoupit.
2. Implementujte třídu `Store`, která bude reprezentovat obchod v obchodním centru. Tato třída by měla obsahovat atributy pro:

   - `name`: Název obchodu.
   - `inventory`: Inventář zboží v obchodě.
   - `customers`: Seznam zákazníků ve frontě na nákup.
   - `interactions`: Metoda pro interakce mezi zákazníky a zaměstnanci obchodu.

3. Implementujte třídu `ShoppingMall`, která bude reprezentovat celé obchodní centrum. Tato třída by měla obsahovat seznam obchodů a metody pro:

   - Pohyb zákazníků mezi různými obchody.
   - Rozdělování zákazníků do front na nákup.
   - Vytváření zákazníků s nákupním seznamem.

4. Napište funkci `simulate_shopping_mall(mall_size, num_customers, num_steps)`, která bude simulovat chování zákazníků v obchodním centru. Parametr `mall_size` určuje velikost obchodního centra, `num_customers` určuje počet zákazníků a `num_steps` určuje počet kroků simulace.

Pravidla simulace:

- Zákazníci se pohybují mezi různými obchody a interagují s ostatními zákazníky.
- Zákazníci nakupují zboží podle svého nákupního seznamu.
- Obchody mají inventář zboží, který se postupně vyprazdňuje během nákupu.

**Poznámka:** Ujistěte se, že student správně implementuje třídy pro zákazníky, obchody a obchodní centrum, včetně metod pro interakce mezi zákazníky a obchody. Funkce `simulate_shopping_mall` by měla simulovat pohyb a interakce zákazníků v obchodním centru a vypisovat stav v každé iteraci.

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

Převoz písku.
