# Algoritmizace

## Přehled

1. [Čtení ze souborů](#čtení-ze-souborů)
2. [Výjimky](#výjimky)
3. [Moduly](#moduly)

## Úvod

1. Algoritmus:
   Algoritmus je postup, který popisuje, jak řešit určitý problém. Jedná se o abstraktní sérii kroků, které mají vést k požadovanému výstupu. Algoritmy existují i mimo svět počítačů.

2. Program:
   Program je konkrétní implementace algoritmu pomocí programovacího jazyka.

Zjednodušeně řečeno, algoritmus je jako recept, který říká, co a jak udělat, zatímco program je hotové jídlo připravené podle tohoto receptu.

Je toto definice? HLOUPOST!!! Jestli někdo bude tvrdit, že zná přesnou definici algoritmu, tak vám kecá.

### Úkol 1

Na základě tohoto [videa](https://www.youtube.com/watch?v=nUHbVRSLlEs) uveď základní vlastnosti algoritmu.

U algoritmů budeme tyto vlastnosti vždy kontrolovat.

### Úkol 2

![map](images/map.gif)

1. Turista nemá mapu
2. Vy nemáte mapu, ale znáte cestu
3. Turista stojící u stadionu se ptá na cestu k nemocnici.

### Úkol 3

- Pochopí turista popis cesty? → srozumitelnost
- Bude vědět v každém okamžiku co má dělat? → jednoznačnost
- Dojde do cíle? → ověření, správnost
- Je to jediná možná cesta? Není jiná lepší? → efektivita

Turista je cizinec.

- Neumíme vzájemný jazyk → kompromis pochopitelný pro oba → symboly → programovací jazyk, překladače

### Úkol 4

Dostanete sadu kartiček s čísly:

1. Seřaďte karty (čísla) podle velikosti
2. Sepište stručný návod pro řazení
3. Ověřte, že se jedná o algoritmus
4. Řešte ve skupině, diskuse je důležitá.

### Úkol 5

1. Seřaďte karty podle instrukcí jiné skupiny
   > Dodržet zápis, neodhadovat, „nedomýšlet“
2. Kontrolujte, že se opravdu jedná o algoritmus
3. Najděte chybná místa
4. Navrhněte opravu

### Úkol 6

Přichází testování a ladění:

1. Do balíčku karet přidáme speciální karty
2. Je-li třeba navrhněte opravu
3. Určete povolené vstupní hodnoty

### Úkol 7

Který algoritmus je nejlepší?

Co je to nejlepší?

- Pokud chci posuzovat, musím si určit kritéria
- Žádné kritérium není apriori špatné, záleží na situaci
- Více kritérií => priorita kritérií

### Úkol 8

Vytvoř podprogram, který dostane jako parametr číslo a určí, jestli je dané číslo prvočíslo, nebo ne.

### Úkol 9

Vytvoř podprogram `eratosthenovo_sito`, který dostane jako parametr číslo `n` a určí pro prvních `čísel`, jestli se jedná o prvočísla.

### Úkol 10

Vytvoř podprogram, který určí největší společný dělitel dvou čísel

### Úkol 11

Vytvoř podprogram, který dostane dva parametry `x` a `y`, který pomocí euklidova algoritmu najde největší společná dělitel čísel `x` a `y`.

### Úkol 12

Vytvoř podprogram, který dostane jako parametr seznam setřízených čísel a číslo `x`. Podprogram určí, jestli se číslo v seznamu nachází.

### Úkol 13

Na řešení přechozí úlohy použijte binární vyhledávání.

### Úkol 14

Bubble sort

### Úkol 15

Selection sort

### Úkol 16

Heap sort

### Úkol 17

Quick sort

### Úkol 18

Speed test třídících algoritmů.

### Úkol 19

Frekvenční analýza:

Zde je zašifrovaný text:

```
mafbo apsjdqej asdjy ycxm padpa asd asdasd asdasase asd asdass ajoi njijq naoijdqww lajqjw jqwj jaij jqlej qjwe ja iqoiwheo qj a joi joijosaj ajdsj qwasde qwdsae iojoij
```

Analyzujte následující [soubor](soubor.txt). Proveďte na něm frekvenční analýzu písmen. Následně pomocí získných informací a frekvence písmen v zašifrovaném textu rozluště zašifrovaný text.