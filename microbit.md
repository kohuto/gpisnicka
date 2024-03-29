# MICRO:BIT

## Přehled

1. [Co je Micro:bit?](#co-je-microbit)
2. [Makecode](#makecode)
3. [Úvod](#úvod)
4. [Proměnná](#proměnná)
5. [Podmínky](#podmínky)
6. [Cyklus](#cyklus)
7. [Pole](#pole)
8. [Funkce](#funkce)
9. [Projekty](#projekty)

## Co je Micro:bit

BBC micro:bit je mikropočítač zaměřený na výuku. Pro desku BBC microbit existují různá příslušenství, rozšiřující moduly, STEAM stavebnice a kreativní hračky. Microbit lze kombinovat i s LEGO. Existují dvě verze micro:bitu - micro:bit V1 a micro:bit V2.

![microbit](/images/microbit_description.png)

Pokud byste kupovali micro:bit a rozšíření, tak doporučuji obchod [HWKitchen](https://www.hwkitchen.cz/).

## Makecode

Prostředí pro psaní kódu pro micro:bit. Kód lze tvořit pomocí bloků, Pythonu a JavaScriptu. Postup pro vytvoření programu v MakeCode najdete [zde](https://scribehow.com/shared/How_to_Create_Basic_Code_in_Microsoft_MakeCode_for_microbit__m0_MMY_vTdiecdFmB0m_Zw). Celé prostředí připomíná Scratch - bloky se chovají podobně, jsou roztřízené do kategorií podle barev. V levé části dokonce vidíme simulátor microbitu, na kterém s eautomaticky spouští náš program.

## První program

Microbit připojíme kabelem k počítači. Zde je návod pro nahrání programu do microbit.

## Inspirace

Obecně u microbitu není problém vymyslet "Jak věci udělat" ale spíše "Jaké věci udělat". Dobré je začít tím, co už někdo vymyslel. Dobré stránky pro inspiraci jsou např.:
[https://www.microbiti.cz/](https://www.microbiti.cz/)
[https://bastlirna.hwkitchen.cz/category/novinky/tutorialy/microbit/](https://bastlirna.hwkitchen.cz/category/novinky/tutorialy/microbit/)

## Bloky, programy, ovládání

Níže najdete krátké tutoriály vysvětlující úplné základy:
[mazání bloků](https://scribehow.com/shared/How_to_Remove_a_Block_in_MakeCode_Microbit_Editor__UDhdI74PRC-GqaB5K9SkbQ)

## Podmínky

## Cyklus

## Pole

## Funkce

## Projekty

### Vodováha

### Zloděj vs policajt

### Multiplayer zloděj vs policajt

jeden hraje za zloděje druhý za policajta

### Multimulti player zloději a policajt

více hráču jsou zloději, policajt se náhodně hýbe, vyhrává poslední přeživší (případně jeden hraje za policajta více lidí za zloděje apod.)

### Radiomaják

### Maják pro pokročilé - dlouhý nápis

Vytvořte displej z několika microbitů ovládaný dálkově jiným microbitem

### Snake

### Blikající diody

Máš programovatelnou elektronickou desku a můžeš si s ní hrát. Na této desce jsou tři programovatelné LED diody (červená, zelená a modrá), které můžeš ovládat pomocí programu jejich zapnutím nebo vypnutím (všechny diody jsou před spuštěním programu vypnuté).

Zde je příklad takového programu: 

Opakuj stále:                                                                          
      zapni (červená)
      čekej (1s)
      vypni (červená)
      čekej (2s)

Akce prováděné tímto programem jsou následující:

   1. Zapne se červená LED dioda
   2. Program čeká a nedělá nic 1 sekundu
   3. Vypne se červená LED dioda
   4. Program čeká a nedělá nic 2 sekundy
   5. Program opakuje znovu od bodu č.1

Podle tohoto programu bude červená LED dioda stále blikat, střídavě bude svítit 1 sekundu a pak bude na 2 sekundy vypnutá.

Máme následující program:

Opakuj stále:
     zapni (modrá)
     čekej (2s)
     zapni (červená)
     zapni (zelená)
     čekej (2s)
     vypni (zelená)
     vypni (modrá)
     čekej (2s)
     zapni (zelená)
     čekej (2s)
     vypni (červená)
     vypni (zelená)     

Kolik LED diod je zapnuto 13 sekund po spuštění tohoto programu?
