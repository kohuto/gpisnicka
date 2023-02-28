# CSS

## Přehled

1. [CSS](#css)
2. [Propojení s HTML](#propojení-s-html)
3. [Selektory](#selektory)
4. [Příklady selektory](#příklady-na-procvičení-selektorů)
5. [Komentář](#komentář)
6. [Barvy](#barvy)
7. [Pozadí](#pozadí)
8. [Ohraničení](#ohraničení)
9. [Box model](#box-model)
10. [Odkazy](#odkazy)
11. [Seznamy](#seznamy)
12. [Display](#display)
13. [Overflow](#overflow)
14. [Float](#float)
15. [Align](#align)
16. [Navigační menu](#navbar)

### CSS

CSS je jazyk, který používáme pro stylování html dokumentů. Pomocí CSS tedy definujeme vzhled web (HTML nikdy nebylo určené k formátování webové stránky!). CSS je zkratka z Cascading Style Sheets

obecná syntaxe v CSS je následující:

```css
selector {
  property: value;
  /* tady jsou další properties */
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

#### Příklady na procvičení selektorů

Pro následující úlohy použijte tento HTML kód:

```html
<h1>Nadpis</h1>
<div class="class1">
  <div id="id1">text 1</div>
  <div>text 2</div>
  <div class="class2 class3">
    <p>text 3</p>
    <p>text 4</p>
    <div class="class5">
      <p>text 5</p>
      <p>text 6</p>
    </div>
    <a href="www.youtube.com">text 7</a>
  </div>
  <div class="class3">text 8</div>
  <div class="class2 class6">text 9</div>
  <div class="class6">text 10</div>
  <p>text 11</p>
</div>
```

1. změň barvu pozadí pro text 1
   <details>
     <summary>řešení</summary>

   ```css
   #id1 {
     background-color: red;
   }
   ```

   </details>

2. změň barvu pozadí pro všechny texty kromě nadpisu
   <details>
     <summary>řešení</summary>

   ```css
   .class1 {
     background-color: red;
   }
   ```

   </details>

3. změň barvu pozadí pro text 7
      <details>
        <summary>řešení</summary>

   ```css
   a {
     background-color: red;
   }
   ```

   </details>

4. změň barvu pozadí pro text 3, text 4, text 5, text 6, text 11
      <details>
        <summary>řešení</summary>

   ```css
   p {
     background-color: red;
   }
   ```

   </details>

5. změň barvu pozadí pro text 3, text 4, text 5, text 6 a text 7
   <details>
     <summary>řešení</summary>

   ```css
   .class2.class3 {
     background-color: red;
   }
   ```

   </details>

6. změň barvu pozadí pro text 3, text 4, text 5, text 6
   <details>
     <summary>řešení</summary>

   ```css
   .class2 p {
     background-color: red;
   }
   ```

   </details>

7. změň barvu pozadí pro text 5, text 6 a text 7
   <details>
     <summary>řešení</summary>

   ```css
   .class5,
   a {
     background-color: red;
   }
   ```

   </details>

8. změň barvu pozadí pro text 3 a text 4
   <details>
     <summary>řešení</summary>

   ```css
   .class2 > p {
     background-color: red;
   }
   ```

   </details>

9. změň barvu pozadí pro text 9 a text 10
   <details>
     <summary>řešení</summary>

   ```css
   .class6 {
     background-color: red;
   }
   ```

   </details>

10. změň barvu pozadí pro text 3, text 4, text 5, text 6, text 7, text 9, text 10,
    <details>
      <summary>řešení</summary>

    ```css
    .class2,
    .class6 {
      background-color: red;
    }
    ```

    </details>

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

```css
a:link {
  color: red;
}

/* visited link */
a:visited {
  color: green;
}

/* mouse over link */
a:hover {
  color: hotpink;
}

/* selected link */
a:active {
  color: blue;
}
```

`a:hover` MUST come after `a:link` and `a:visited` in the CSS definition in order to be effective.

`a:active` MUST come after `a:hover` in the CSS definition in order to be effective.

podtržení

```css
a:link {
  text-decoration: none;
}

a:visited {
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

a:active {
  text-decoration: underline;
}
```

pozadí

```css
a:link {
  background-color: yellow;
}

a:visited {
  background-color: cyan;
}

a:hover {
  background-color: lightgreen;
}

a:active {
  background-color: hotpink;
}
```

odkaz jako tlačítko

```css
a:link,
a:visited {
  background-color: white;
  color: black;
  border: 2px solid green;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover,
a:active {
  background-color: green;
  color: white;
}
```

### Seznamy

```css
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
```

### Display

z blokového lze udělat inline

```css
li {
  display: inline;
}
```

z inline lze udělat blokového

```css
a {
  display: block;
}
```

### Overflow

V případě, že je obsah elementu tak velký, že se do elementu nevleze, tak vlastnost `overflow` specifikuje, jak se má obsah zobrazit.

```css
div {
  background-color: coral;
  width: 200px;
  height: 100px;
  overflow: hidden;
  /* overflow: visible; */
  /* overflow: scroll; */
}
```

### Float

```html
<div class="box">
  <p>text 1</p>
</div>
<div class="box">
  <p>text 2</p>
</div>
<div class="box">
  <p>text 3</p>
</div>
```

```css
.box {
  border: solid 2px;
  float: left;
  width: 20%;
  padding: 5%;
}
```

### Align

```html
<div class="center">
  <p>This text is centered.</p>
</div>
```

```css
.center {
  text-align: center;
  border: 3px solid green;
}
```

### Navbar

vytvořte navigační menu

```html
<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>
```

```css
ul {
  list-style-type: none;
  overflow: hidden;
  background-color: #dddddd;
}

li {
  float: left;
}

li a {
  display: block;
  padding: 15px;
}
```
