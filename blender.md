# BLENDER

## Přehled

1. [Co je Blender?](#co-je-blender)
2. []()
3. []()
4. []()
5. []()
6. []()

## Co je Blender

Blender je bezplatný program pro práci s 3D grafikou, který spravuje a aktualizuje Nadace Blender. Je oblíbený jak mezi odborníky, tak začátečníky díky své rozmanitosti nástrojů. S Blenderem můžete modelovat, animovat, simulovat, vykreslovat obrazy, komponovat scény, provádět post-produkci a stříhat videa. Software také nabízí pokročilé simulace fyziky, což umožňuje vytvářet realistické zobrazení věcí jako voda či oheň. Kromě toho má Blender velkou a aktivní komunitu, která přidává nové funkce a vylepšení. Shrnutím, Blender je komplexní, ale zároveň bezplatný nástroj pro 3D grafiku.

## Stažení

Blender stáhněte z oficiálních [stránek](https://www.blender.org/)

## Základní ovládání

Po otevření aplikace uvidíte podobnou obrazovku. Z nabídky vyberte možnost **_General_.**

![landing page](images/landing-page-blender.png)

Zobrazí se klasická 3D scéna.

> Na obrazovce jsou na začátku vidět 3 objekty - krychle, světlo a kamera. Světlo a kameru můžeme ihned smazat (viz níže).

Ovládání je následující:

- `Zmáčknuté kolečko myši` - otáčení
- `Shift` + `zmáčknuté kolečko myši` - posun
- `kolečko myši` - přiblížení
- `klik` - výběr objektu
- `Shift` + `klik` - výběr více objektů

V momentě kdy máme vybraný objekt:

- `x` - Po vybrání možnosti _Delete_ smazání objektu
- `g` - přesunutí objektu
- `r` - rotace objektu
- `s` - zvětšení objektu
- `n` - informace o objektu

## Jednotky

Vytvaříme model pro 3D tiskárnu, v takovém případě se doporučuje mít všechny jednoty v milimetrech. Z nabídky vlevo vyberte _Scene_ a rozklikněte nabídku _Units_. Nastavte _Length_ na _Millimeters_ a _Unit Scale_ nastavte na hodnotu 0.001.

![units](images/units.png)

Na první pohled to vypadá, že nám zmizela mřížka. Aby se opět správně zobrazovala, vyberte možnost _Overlays_ a opět nastavte _Scale_ na hodnotu 0.001.

![units](images/grid-scale.png)

## Módy

Pro každý objekt, který označíme, nabízí Blender dva základní módy. Aktuálně jsme v _Object mode_. V něm lze pouze objekty přesouvat, rotovat, či měnit vělikost. Druhý je _Edit mode_, který umožňuje vybraný objekt různě tvarovat.

![edit-mode](images/edit-mode.png)

## Edit mode

Vlevo nahoře máme v Edit Mode (hned vedle volby) tři možnost:

1. vertex select
2. edge select
3. face select

výběr provedeme pomocí přetažení (označení). V levé liště pak vidíme možnosti, co s daným výběrem vrcholů/hran/stěn můžeme dělat

- face select → insert faces → vytvoříme "zdi", 4 zdi označíme → extrude region (vytáhne zdi nahoru)

označíme dva body (první přepneme na vertex select) → můžeme hýbat pomocí move → deformace

zkusíme-li označit všechny body, pak po natočení zjistíme, že se to nepovedlo → vpravo nahoře TOGGLE X-RAY

Chceme na krabici přidat text → vrátíme se do Object Mode v horní noabídce (vedle Object mode) vybereme Add → přidávání objektů (v mesh - dokonce i opice), my chceme ale text → oba objekty vidíme v menu vlevo (cube, text)

změna nápisu → Edit mode, v Object mode ho můžeme přesouvat a natáčet

text je 2D (v menu vlevo vidíme rozdílné ikony u cube a u text, Cube je typ mesh, text je typ Curve) → OBJECT (vlevo nahoře) → convert → mesh

Stále bude 2D, stačí se přepnout do Edit Mode → vidíme, že to už je směs bodů a hran → označit vše lze pomocí A, pak už pomocí extrude region uděláme text 3D. Zpět do Object mode → vsuneme do zdi → chceme spojit do jednoho objektu → MODIFIERS (lišta, kde jsme nastavovali scenes, modrý klíč)
