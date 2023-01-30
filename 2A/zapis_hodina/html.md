# HTML

## Přehled

1. [HTML](#html)
2. [VS code](#vs-code)
3. [Tag](#tag)
4. [Komentář](#komentář)
5. [Nadpis](#nadpis)
6. [Odstavec](#odstavec)
7. [Atributy](#atributy)
8. [Obrázek](#obrázek)

### HTML

HTML je jazyk, který se používá pro tvorbu webových stránek. HTML je zkratka pro _HyperText Markup Language_. Slovo **Markup** ve zkratce znamená **Značkovací**, což vystihuje účel, kterému se HTML používá. Používá se totiž pro popis struktury webů. To znamená, že pomocí [tagu](#tag) označíme čast textu, čímž o dané části textu řekneme např. _toto je nadpis_, nebo _toto je odstavec_, nebo _toto je odkaz_. HTML soubor ukládáme s koncovkou `.html`

Kdybychom neznali `HTML` mohli bychom popsat jednotlivé části textu třeba takto.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <!-- seznam, navigace, menu -->
    <!-- první položka v seznamu -->
    1. HOME
    <!-- druhá položka v seznamu -->
    2. ABOUT ME
    <!-- třetí položka v seznamu -->
    3. MY WORK
    <!-- čtvrtá položka v seznamu -->
    4. CONTACT

    <!-- nadpis -->
    Welcome to my website!

    <!-- odstavec -->
    My name is John and I am a software developer with a passion for creating
    beautiful and functional websites. On this site, you can find information
    about my professional background and skills, as well as some of the projects
    I have worked on.

    <!-- odstavec -->
    I have always been fascinated by the power of the internet to connect people
    and share information. As a developer, I am constantly learning and seeking
    out new challenges to help me grow and improve.

    <!-- obrázek -->
    profile_photo.jpg

    <!-- odstavec -->
    In my spare time, I enjoy traveling, reading, and spending time with my
    family and friends. links to gitlab
    <!-- odkaz -->
    https://github.com/

    <!-- poděkování -->
    Thank you for visiting my website. I hope you find the information here
    useful and that we can work together in the future.
    <!-- rozloučení -->
    Best regards,

    <!-- patička -->
    John Copyright 2021 John's Website. All rights reserved. Contact:
    info@johns-website.com
  </body>
</html>
```

Později si ukážem, jak to stejné zapsat pomocí jazyka `HTML`. Zjistíme, že některé [tagy](#tag) budou existovat (např. nadpis, odkaz atd.), některé tagy, však existovat nebudou (např. poděkování, rozloučení).

### VS code

VS code je tzv. IDE (_integrated development environment_), neboli vývojové prostředí, ve kterém lze mimo jiné hezky pracovat i s `.html` soubory.

Při vyvíjení webu chceme mít vše **VŽDY** uložené v jedné složce. Proto si v počítači první vytvoříme složku (pojmenujeme ji třeba _mujPrvniWeb_). Nyní vy VS code klikneme na tlačítko `file` a vybereme možnost `open folder`. Najdeme Naši složku, klikneme na ni a vybereme možnost `vvybrat složku`. Čímž se nám složka otevře ve VS code.

Vytvoříme nyní dokument s koncovkou `.html`. Nyní zmáčkneme `!` a stiskneme `Enter`, čímž se nám vygeneruje šablona.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body></body>
</html>
```

To co je mezi [tagy](#tag) `head` zatím budeme ignorovat. Nás nyní bude zajímat tag `body`, do kterého budeme psát to, co chceme, aby bylo vidět na naší webové stránce.

### Tag

Slovo `tag` už zaznělo mnohokrát, co to tedy je? Tag určuje začátek a konec html elementu. Analogicky `element` je vše, od začínajícího (tzv. otevíracího) tagu až po ukončující (tzv. uzavírací) tag.

```html
<tagname>nějaký obsah...</tagname>
```

příkladem mohou být např. tagy určující nadpis nebo odstavec

```html
<h1>Můj první nadpis</h1>
<p>Můj první odstavec</p>
```

### Komentář

Komentáře se nezobrazují ve webovém prohlížeči.

Používáme je pro popis kódu. Pomocí komentáře můžeme například popsat, co daná část kódu dělá (např. _tato část kódu tvoří navigační menu webu_). Komentáře jsou tedy určeny pro nás webové vývojáře, ne pro běžného uživatele na webu.

Takto se zapisují komentáře v HTML:

```html
<!-- toto je komentář -->
```

### Nadpis

Máme šest úrovní nadpisů. `h` je zkratka z `heading` (česky nadpis). Číslo udává **důležitost** nadpisu (velikost nadpisu stejně budeme měnit pomocí CSS). To mimojiné vyplývá už z důvodu, proč používáme `html` (udává strukturu webu, ne vzhled).

```html
<h1>nadpis 1. úrovně</h1>
<h2>nadpis 2. úrovně</h2>
<h3>nadpis 3. úrovně</h3>
<h4>nadpis 4. úrovně</h4>
<h5>nadpis 5. úrovně</h5>
<h6>nadpis 6. úrovně</h6>
```

### Odstavec

`p` je zkratka z `paragraph` (česky odstavec). Pomocí tagu `p` označujeme opravdu celé odstavce. Toto je tedy správné použití:

```html
<p>
  Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nam libero tempore,
  cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
  maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor
  repellendus.
</p>
```

Toto je špatné použití (neoznačili jsme odstavec, ale pouze jeden řádek odstavce):

```html
<p>
  Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Nam libero tempore,
</p>
<p>
  cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod
</p>
<p>maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor</p>
<p>repellendus.</p>
```

### Atributy

atributy poskytují doplňující informace o HTML elementech. Píšeme je do otevíracího tagu. Atributy mají většinou následující syntax:

```
jméno="hodnota"
```

Konkrétní příklad uvidíme hned v další kapitole.

### Obrázek

Pro zobrazení obrázku používáme tag `img`.

```html
<img src="slozka1/slozka2/slozka3/obrazek.png" alt="muj_obrazek" />
```

Do tohoto elemetu vždy vkládáme dva atributy

- `src` - určuje místo, kde je obrázek uložen
- `alt` - určuje alternativní text, který se zobrazí v případě, že je obrázek nedostupný

#### Absolutní vs relativní cesta vs url

- url
  - "klasická" url adresa, kterou známe
  - př. https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2020%2F06%2F26%2Forange-kitten-955480082-2000.jpg
  - výhody: obrázek nemusím mít stažený a uložený - úspora paměti
  - nevýhody: někdo nám obrázek smaže
- absolutní cesta
  - cesta k souboru z kořenového adresáře k souboru
  - př. C:\Documents\Newsletters\2018\Summer2018.jpg
  - nevýhody: v nepoužitelné - nebude fungovat jinde, než na aktuálním počítači
- relativní cesta
  - cesta k souboru v podadresáři aktuálního adresáře
  - př. 2018\Summer2018.jpg
  - výhody: snadná přenositelnost

závěr - vždy budeme v atributu `src` používat realtivní cestu
