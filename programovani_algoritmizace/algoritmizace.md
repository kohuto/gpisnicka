# Algoritmizace
## Přehled

1. [Úvod](#úvod)

## Cíle výuky

- vysvětlím rozdíl mezi algoritmem a programem
- zhodnotím, jestli algoritmus splňuje základní vlastnosti algoritmu
- zhodnotím efektivitu daného algoritmu
- analyzuji chování algoritmu a na základě toho určím, k čemu se daný algoritmus používá
- najdu chybu v algoritmu a chybu opravím
- Graficky znázornim algoritmus

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

Který algoritmus je nejlepší? Co znamená nejlepší?

- pokud chci posuzovat, musím si určit kritéria
- žádné kritérium není apriori špatné, záleží na situaci
- pokud mám Více kritérií, musím si určit jejich prioritu

### Úkol 6

Najdi v sezamu největší číslo. Jak na to přijít? kouknu a vidím. Ok nyní si pusť video - jaké bylo největší číslo? jak jsi na to přišel?

### Úkol 10

Vytvoř podprogram, který určí největší společný dělitel dvou čísel

### Úkol 10

Vytvoř podprogram, který dostane dva parametry `x` a `y`, který pomocí eukleidova algoritmu najde největší společný dělitel čísel `x` a `y`.

### Úkol 11

Vytvoř podprogram, který dostane jako parametr číslo a určí, jestli je dané číslo prvočíslo, nebo ne. Pomocí tohoto programu urči pro prvních `n` přirozených čísel, jestli se jedná o prvočísla.

### Úkol 12

Vytvoř podprogram `eratosthenovo_sito`, který dostane jako parametr číslo `n` a určí pro prvních `n` čísel, jestli se jedná o prvočísla.
