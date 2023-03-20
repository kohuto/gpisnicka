# Framework

## Přehled

1. [Bootsrap](#bootstrap)
2. [Navigančí menu](#navigační-menu)
3. [Jumbotron](#jumbotron)
4. [Tlačítko](#tlačítko)
5. [Row](#row)
6. [Carousel](#carousel)
7. [Cards](#cards)
8. [Formulář](#formulář)

### Bootstrap

### Navigační menu

[dokumentace](https://getbootstrap.com/docs/4.0/components/navbar/)

Definujeme kontejner a barevné schéma navigačního menu

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a href="#">My Portfolio</a>
  <button
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span></span>
  </button>
  <div>
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

Definujeme značku firmy

```html
<!-- Navigation bar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a href="#" class="navbar-brand">My Portfolio</a>
  <button
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span></span>
  </button>
  <div>
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

Definujeme tlačítko pro malé obrazovky. Po přidání třídy si vyzkoušej zmenšit velikost okna.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a href="#" class="navbar-brand">My Portfolio</a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div>
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

Po přidání následující třídy to vypadá, že se nic nestalo. Vyzkoušej ale opět zmenšit velikost okna. Id zajistí skrytí/ukázání menu.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a href="#" class="navbar-brand">My Portfolio</a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

Nyní máme hotovu vnější část navigačního menu. Pojďme se nyní zaměřit na vnitřek.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a href="#" class="navbar-brand">My Portfolio</a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

Menu je skoro hotové, zbývá nastylovat jednotlivé prvky seznamu. Položka v menu, která je zrovna aktivní, má navíc třídu `active`.

```html
<!-- Navigation bar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a href="#" class="navbar-brand">My Portfolio</a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a href="#" class="nav-link">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#">Portfolio</a>
      </li>
      <li>
        <a href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

Stejné třídy použijte i pro zbytek prvků seznamu. Pouze první bude mít třídu `active`. Menu je hotové. Vyzkoušejte, jak vypadají položky menu, když přes ně přejedete myší. Vyzkoušejte zmenšit a zvětšit okno.

```html
<!-- Navigation bar -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">My Portfolio</a>
  <button
    class="navbar-toggler"
    type="button"
    data-toggle="collapse"
    data-target="#navbarNav"
    aria-controls="navbarNav"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">About</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Portfolio</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Contact</a>
      </li>
    </ul>
  </div>
</nav>
```

### Jumbotron

```html
<div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <p class="lead">This is my portfolio website.</p>
  <hr class="my-4" />
  <p>It is still a work in progress, but feel free to look around!</p>
  <a href="#" role="button">Learn more</a>
</div>
```

### Tlačítko

Vytvořit tlačítko pomocí Bootstrapu je velice jednoduché.

- `btn` definuje tlačítko
- `btn-primary` určí vzhled tlačítka
- `btn-lg` určuje velikost tlačítka

```html
<a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
```

### Row

### Carousel

### Cards

### Formulář
