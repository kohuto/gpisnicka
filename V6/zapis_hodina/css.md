# CSS

## Přehled

1. [CSS](#css)
2. [Propojení s HTML](#propojení-s-html)
3. [Selektory](#selectors)
4. [Komentář](#komentář)
5. [Barvy](#barvy)
6. [Pozadí](#pozadí)
7. [Ohraničení](#ohraničení)
8. [Box model](#box-model)
9. [Atributy](#atributy)
10. [Obrázky](#obrázek)
11. [Seznamy](#seznamy)
12. [Block & inline elementy](#block--inline-elementy)
13. [Třídy a Id](#třídy-a-id)

### CSS

CSS je jazyk, který používáme pro stylování html dokumentů. Pomocí CSS tedy definujeme vzhled web (HTML nikdy nebylo určené k formátování webové stránky!). CSS je zkratka z Cascading Style Sheets

obecná syntaxe v CSS je následující:

```css
selector {
  property: value;
}
```

konkrétní příklad:

```css
h1 {
  color: blue;
}
```

### Propojení s HTML

Existují tři způsoby jak vložit style sheet:

1. External CSS - styly máme uložené ve speciálním `.css` souboru
2. Internal CSS - styly jsou definované v elementu `<style>` v sekci `<head>`
3. Inline CSS - styly jsou definované přímo uvnitř elementu

Doporučený přístup je používat external CSS (až na výjimky).

Externí styly jsou definovány pomocí `<link>` elementu v `<head>` sekci:

```html
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="mystyle.css" />
  </head>
  <body>
    body content
  </body>
</html>
```

- `rel` - specifikuje vztah mezi nalinkovaným dokumentem a aktuálním dokumentem
- `href` - definuje umístění externího `.css` souboru

### Selektory

CSS selektory se používájí pro nalezení elementu, který chceme nastylovat.

#### Element selektory

vybereme element podle jeho jména.

```css
/* změň barvu textu na modrou ve všech <h1> elementech */
h1 {
  color: blue;
}
```

#### id selektory

vybereme element podle id atributu. Syntaxe je `#` následovaný názvem `id`

```css
/* změň barvu textu na modrou v elementu s id="mojeid" */
#mojeid {
  color: blue;
}
```

#### Class selektory

vybereme element podle class atributu. Syntaxe je `.` následovaná názvem `class`

```css
/* změň barvu textu na modrou ve všech elementech s class="mojetrida" */
.mojetrida {
  color: blue;
}
```

Můžeme vybrat pouze konkrétní element s danou třídou.

```css
/* změň barvu textu na modrou pouze v <p> elementech s class="mojetrida" */
p.mojetrida {
  color: blue;
}
```

#### Univerzální selektor

Pomocí univerzálního selektoru vybereme všechny html elementy. Snytaxe je `*`

```css
/* změň barvu textu na modrou ve všech elementech */
* {
  color: blue;
}
```

#### Seskupování selektorů

Místo tohoto:

```css
h1 {
  text-align: center;
  color: red;
}

h2 {
  text-align: center;
  color: red;
}

p {
  text-align: center;
  color: red;
}
```

budeme psát toto:

```css
h1,
h2,
p {
  text-align: center;
  color: red;
}
```

další příklady:

```css
/* změň barvu textu na modrou ve všech elementech, které mají v atributu class nastavenou hodnotu mojetrida1 i mojetrida2 */
.mojetrida1.mojetrida2 {
  color: blue;
}

/* změň barvu textu na modrou ve všech elementech <p>, které jsou uvnitř elementu <div> */
div p {
  color: blue;
}

/* změň barvu textu na modrou ve všech elementech <p>, jejichž předek je element <div> */
div > p {
  color: blue;
}
```

### Komentář

komentáře se v CSS píšou takto:

```css
/* toto je komentář */
```

Pro komentáře v CSS platí to stejné, co pro komentáře v HTML.

### Barvy

můžeme nastavit barvu pozadí:

```css
p {
  background-color: blue;
}
```

barvu textu:

```css
p {
  color: blue;
}
```

#### Hodnoty barev

barvy můžeme zapisovat pomocí názvu barvy:

```css
p {
  background-color: orange;
}
```

pomocí HEX hodnoty:

```css
p {
  background-color: #ff6347;
}
```

pomocí RGB hodnoty:

```css
p {
  background-color: rgb(255, 99, 71);
}
```

pomocí RGBA hodnoty:

```css
p {
  background-color: rgba(255, 99, 71, 0.5);
}
```

### Pozadí

Už umíme nastavit barvu pozadí. Nyní nastavme jako pozadí obrázek.

```css
div {
  background-image: url("image.png");
}
```

často chceme nastavit vlastnost `background-repeat`. Pomocí příkladu níže zajistíme, že se nám obrázek nebude opakovat.

```css
div {
  background-image: url("image.png");
  background-repeat: no-repeat;
}
```

### Ohraničení

V rámci ohraničení můžeme nastavit např. následující vlastnosti:

- `border-style`
  - `solid`
  - `dotted`
  - ...
- `border-width`
- `border-color`
- `border-radius`
  vše zapíšeme takto:

```css
div {
  border-style: solid;
  border-width: 5px;
  border-color: black;
  /* další properties */
}
```

případně lze zkrátit takto:

```css
div {
  border: 5px solid black;
}
```

### Box model

Box model je box okolo každého HTML elementu. Skládá se z `margin`, `border`, `padding` a `content`.
![Box model](./images/boxmodel.png)

#### Margin

`margin` se používá pro vytvoření prostoru okolo elementu vně ohraničení.

```css
div {
  margin-top: 100px;
  margin-bottom: 100px;
  margin-right: 150px;
  margin-left: 80px;
}

/* nebo zkráceně */
div {
  margin: 100px 100px 150px 80px;
}
```

#### Padding

`padding` se používá pro vytvoření prostoru okolo elementu uvnitř ohraničení.

```css
div {
  padding-top: 100px;
  padding-bottom: 100px;
  padding-right: 150px;
  padding-left: 80px;
}

/* nebo zkráceně */
div {
  padding: 100px 100px 150px 80px;
}
```

### Odkazy

### Seznamy

### Display

### Navbar
