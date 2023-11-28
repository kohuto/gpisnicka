# Algoritmizace
## Přehled

1. [Úvod](#úvod)

## Úvod

1. Algoritmus:
   Algoritmus je postup, který popisuje, jak řešit určitý problém. Jedná se o abstraktní sérii kroků, které mají vést k požadovanému výstupu. Algoritmy existují i mimo svět počítačů.

2. Program:
   Program je konkrétní implementace algoritmu pomocí programovacího jazyka.

Zjednodušeně řečeno, algoritmus je jako recept, který říká, co a jak udělat, zatímco program je hotové jídlo připravené podle tohoto receptu.

Přesná definice algoritmu neexistuje. Je ale dobré vnímat rozdíl mezi algoritmem a programem.

### Úkol 1

Na základě (pseudo) definice uveď příklady nějakých algoritmů, se kterými se můžeme setkat. Jakým způsobem jsou tyto algoritmy zapsané.

### Úkol 2

Na základě tohoto [videa](https://www.youtube.com/watch?v=nUHbVRSLlEs) uveď základní vlastnosti algoritmu.

U algoritmů budeme tyto vlastnosti vždy kontrolovat.

### Úkol 3

![map](../images/map.png)

Na obrázku je znázorněno město. Zelená šipka je místo, kde aktuálně stojíte vy a turista.

1. Turista nemá mapu
2. Vy nemáte mapu, ale znáte cestu
3. Turista stojící u stadionu se ptá na cestu k nemocnici (červená šipka).

### Úkol 4

Shrnutí vlastností:

- Pochopí turista popis cesty? → srozumitelnost
- Bude vědět v každém okamžiku co má dělat? → jednoznačnost
- Dojde do cíle? → ověření, správnost
- Je to jediná možná cesta? Není jiná lepší? → efektivita

Uveďte, co si myslíte, že je v tomto případě efektivní algoritmus?

### Úkol 5

Dostanete sadu kartiček s čísly:

1. Seřaďte karty (čísla) podle velikosti
2. Sepište stručný návod podle, kterého půjde karty seřadit
3. Ověřte, že se jedná o algoritmus (splňuje základní vlastnosti algoritmu?)
4. Algoritmus sepište ve skupině

### Úkol 6

1. Seřaďte karty podle instrukcí jiné skupiny
   > Třiďte karty přesně podle jejich algoritmu, nic nedohadujte ani nedomýšlejte
2. Kontrolujte, že se opravdu jedná o algoritmus
3. Najděte chybná či nepřesná místa
4. Navrhněte opravu

### Úkol 7

V momentě, kdy máme algoritmus hotový, přichází fáze testování a ladění:

1. Do balíčku karet přidáme speciální karty
2. Je-li třeba navrhněte opravu
3. Určete povolené vstupní hodnoty

### Úkol 8

Který algoritmus je nejlepší? Co znamená v tomto případě nejlepší?

- pokud chci posuzovat, musím si určit kritéria
- žádné kritérium není apriori špatné, záleží na situaci
- pokud mám Více kritérií, musím si určit jejich prioritu

### Úkol 9

Vytvoř podprogram, který určí největší společný dělitel dvou čísel

### Úkol 10

Vytvoř podprogram, který dostane dva parametry `x` a `y`, který pomocí eukleidova algoritmu najde největší společný dělitel čísel `x` a `y`.

### Úkol 11

Vytvoř podprogram, který dostane jako parametr číslo a určí, jestli je dané číslo prvočíslo, nebo ne. Pomocí tohoto programu urči pro prvních `n` přirozených čísel, jestli se jedná o prvočísla.

### Úkol 12

Vytvoř podprogram `eratosthenovo_sito`, který dostane jako parametr číslo `n` a určí pro prvních `n` čísel, jestli se jedná o prvočísla.

### Úkol 13

Vytvoř podprogram, který dostane jako parametr seznam setřízených čísel a číslo `x`. Podprogram určí, jestli se číslo v seznamu nachází.

### Úkol 14

Na řešení přechozí úlohy použijte binární vyhledávání.


### Časová složitost algoritmu

Časová složitost algoritmu je způsob, jakým vyjadřujeme, jak rychle algoritmus pracuje s _různě velkými daty_. Namísto času v sekundách měříme počet provedených _operací_, které algoritmus provádí (předpokládáme, že jedna _operace_ trvá konstantní čas).

Tato složitost se může měnit v závislosti na tom, jaká data algoritmus dostane a na základě toho rozlišujeme tři situace: _nejlepší možný scénář_, _nejhorší možný scénář_ a _průměrný případ_.

Ukažme si to na příkladu. Podprogram dostane jako parametry pole a prvek. Podprogram určí, jestli se zadaný prvek v poli nachází nebo ne. Postupně projde celý seznam prvek po prvku a když na hledaný prvek v seznamu narazí vrátí `True`:

```python
def is_element_in_array(arr, item):
   for i in arr:
      if i == item:
         return True
   return False
```

První vysvětlíme, co znamená _různě velká data_. V tomto případě se jedná o počet prvků v poli. Je asi snadno představitelné, že když bude mít pole miliardu prvků, tak program pobeží déle, než když pole bude mít deset prvků.

Nyní vysvětlíme, co jsou _operace_. Operace je něco, u čeho je potřeba něco rozhodnout/spočítat (hodně zjednodušeně řečeno). V našem případě bude operace pouze `if i == item`, jellikož je zde musíme vyhodnotit podmínku. Nyní je potřeba spočítat, kolikrát se tyto instrukce vykonají, v našem případě, kolikrát se provede příkaz `if i == item`:

- _Nejlepší případ_ - v nejlepším případě najdeme prvek hned na první pozici a program skončí. Příkaz `if i == item` se tedy vykoná pouze jednou
- _Nejhorší případ_ - v nejhorším případě najdeme prvek až na poslední pozici. Příkaz `if i == item` se tedy vykoná tolikrát, kolik prvků je v poli. Když bude v poli `n` prvků, tak říkáme, že se příkaz vykoná `n`-krát
- _Průměrný případ_ - abychom spočítali průměrný případ, museli bychom projít všechny možné scénáře. V tomto konkrétním případě by to nebylo až tak náročné. Obecně je to ale velmi složitý úkol.

> Nejlepší případ je příliš optimistický, průměrný je obecně náročné spočítat. Proto budeme vždy počítat pouze nejhorší případ.

Dobu výpočtu v nejhorším případě zapíšeme pro náš případ takto: `n`. Jedná se o počet vykonaných instrukcí pro vstupní data velikosti `n` (př. pole délky `n`) v nejhorším případě. Později ještě zavedeme tzv. asymptotickou složitost.

### Úkol 15

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (arr): # arr is array of integers
   x = 0
   for i in arr:
      x += i
   return x
```

### Úkol 16

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... ():
   for x in range(1, 11):
      for y in range(1, 11):
         print(x * y, end=" ")
      print()
```

### Úkol 17

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (n):
   for x in range(1, n + 1):
      for y in range(1, n + 1):
         print(x*y, end=" ")
      print()
```

### Úkol 18

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (number):
   try:
      int_number = int(number)
      return int_number ** 2
   except ValueError:
      print(f'{number} is not number')
```

### Úkol 19

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (arr):  # arr is an array of integers
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    return result
```

### Úkol 20

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... ():
    return 42
```
### Úkol 21

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (arr):  # arr is an array of integers
    count = 0
    for num in arr:
        if num % 2 != 0:
            count += 1
    return count
```

### Úkol 22

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (arr):  # arr is an array of integers
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in result:
                result.append(arr[i])
    return result
```

### Úkol 23

Vymyslete vhodný název pro následující podprogram. Jaká je časová složitost tohoto algoritmu?

```python
def ... (arr):  # arr is an array of integers
    count = 0
    for i in arr:
      if count < 10:
         print(i)
         count += 1
      else:
         return
```

### Úkol 24

Bubble sort 

https://visualgo.net/en/sorting?

```
seznam = [....]

opakuj, dokud bylo prohozeno:
   pro cisla od 0 do delka_seznamu udělej:
      jestliže je prvek menší než následující:
         prohoď prvky
         nastav prohozeno na True
```

### Úkol 25

V košíku jsou jablka, každé má jinou velikost. Anežka je třídí tímto způsobem:

Krok 1: Na stůl položí jedno jablko z košíku.

Krok 2: Sáhne pro další jablko do košíku a provede následující srovnání:

1. Jestliže jablko v její ruce je menší než jablko na stole, zahodí jej.

2. Jestliže jablko v její ruce je větší než jablko na stole, položí jej na stůl a jablko ze stolu zahodí.

Anežka opakuje krok 2, dokud není košík prázdný.

Které jablko nakonec zůstane na stole?

- první jablko vyzvednuté z košíku
- poslední jablko vyzvednuté z košíku
- nejmenší jablko z košíku
- největší jablko z košíku

úloha byla převzata ze soutěže Bobřík informatiky
### Úkol 22

Selection sort

```
pro všechny indexy:
   nastav index jako index aktuálně nejmenšího prvku
   pro každý prvek v nesetřízené části:
      jestliže je prvek menší, než nejmenší:
         nastav nový nejmenší
   Vyměnit nalezený minimální prvek s prvkem na indexu atuálně nejmenšího prvku
```


### Úkol 23

Spustíte-li tento program, spadne na chybu (index out of range). Pomocí debuggeru chybu/chyby najděte a opravte.

```python
def bubble_sort_with_error(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i+1):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                swapped = True

        # Pokud nebyly žádné dva prvky vyměněny vnitřní smyčkou, přeruš cyklus
        if not swapped:
            break

    return arr

# Testovací pole s funkcí
test_array = [64, 25, 12, 22, 11]
sorted_array = bubble_sort_with_error(test_array)
```

V opraveném programu zjistěte, jaké hodnoty jsou uložené v `arr[j]` a `arr[j+1]` v momentě, kdy `i = 3` a `j = 0`? Dojde v této iteraci k prohození těchto dvou hodnot?

### Úkol 23

Heap sort

### Úkol 24

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Testování funkce
test_array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quick_sort(test_array)
```

### Úkol 25

Napište program, který změří, jak rychle jednotlivé třídicí algoritmy setřídí pole náhodně vygenerovaných čísel. Otestujte pro pole délky (10, 100, 1000, 10000, 100000, 1000000, ...). Který algoritmus třídí nejrychleji? Jaká je časová složitost jednotlivých třídicích algoritmů?

### Úkol 26

Rozšifrujte tento [soubor](https://drive.google.com/file/d/13ysONFxR1HhOEoC3kUxUamGUrxAN5JPb/view?usp=sharing) pomocí frekvenční analýzy. Pro analýzu jazyka použijte libovolný soubor obsahující anglický text (zašifrovaný text je v angličtině) např. tento [soubor](https://drive.google.com/file/d/1uFDzXUQa4GJtZ7eGNg95QLSdZY-2EK4Y/view?usp=drive_link).

### Úkol 26

Každý tvor má v chromozómech sekvenci DNA, která určuje jeho geny. Sekvence je tvořena ze čtyř typů základních složek, Adeninu (A), Guaninu (G), Cytosinu (C) a Thyminu (T). DNA může mutovat a vytvořit novou sekvenci, která se od původní sekvence bude lišit. 



Vormi je živočich, jehož DNA může mutovat třemi způsoby:

1. Nahrazení: Výměna jedné základní složky za jinou základní složku.

   Příklad: AGGTC -> AGGTA (změna C na A)

2. Vymazání: Odstranění jedné ze základních složek. 

   Příklad: AGGTC -> AGTC (odstranění jednoho G)

3. Zdvojení: přidání - zopakování základní složky.

   Příklad: AGGTC -> AGGTTC (zdvojení T)

Máme původní sekvenci DNA  živočicha Vormiho "GTATCG". Která z těchto sekvencí NEmůže z původní sekvence vzniknout ani po třech genových mutacích?


Tvoje odpověď 
"GCAATG" "ATTATCCG"
"GGTAAAC" "GAATGC"
Nechci odpovídat

### Úkol 27

Obyvatelé vesnice žijí na celkem šesti ostrovech na řece Amazonce. Tyto ostrovy chtějí propojit visutými lávkami. Na obrázku níže vidíš plánek možného propojení ostrovů. Lávky se navzájem nijak nekříží a nepřekážejí si. Čísla symbolizují náklady pro zhotovení lávky.

Obyvatelé chtějí lávky postavit tak, aby bylo možné se dostat z jednoho ostrova na jakýkoliv jiný, a to buď přímo, nebo nepřímo přes jeden či více ostrovů. Zároveň chtějí postavit lávky co nejlevněji.

Označ lávky, které se mají postavit pro propojení všech ostrovů, aby to bylo co nejlevnější.

![msp](../images/minimal-spanning-tree.png)