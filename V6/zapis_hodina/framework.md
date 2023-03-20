# Framework

## Přehled

1. [Bootstrap](#bootstrap)
2. [Navigančí menu](#navigační-menu)
3. [Jumbotron](#jumbotron)
4. [Tlačítko](#tlačítko)
5. [Kontejner](#kontejner)
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

[dokumentace](https://getbootstrap.com/docs/4.0/components/jumbotron/)

`jumbotron` nám vytvoří stylový kontejner. `display` s číslem nám určuje styl nadpisu. `lead` použijeme pro zvýraznění textu.

```html
<div class="jumbotron">
  <h1 class="display-4">Hello, world!</h1>
  <p class="lead">This is my portfolio website.</p>
  <hr />
  <p>It is still a work in progress, but feel free to look around!</p>
  <a href="#" role="button">Learn more</a>
</div>
```

### Margin a padding

[dokumentace](https://getbootstrap.com/docs/4.0/utilities/spacing/#notation)

K nastavení mezer se používají zkratky. `mt` je zkratka z `margin-top`. Naopak `mb` je zkratka z `margin-bottom`. Číslo za pomlčkou udává velikost mezery.

```html
<hr class="mt-4 mb-4" />
```

### Tlačítko

[dokumentace](https://getbootstrap.com/docs/4.0/components/buttons/)

Vytvořit tlačítko pomocí Bootstrapu je velice jednoduché.

- `btn` definuje tlačítko
- `btn-primary` určí vzhled tlačítka
- `btn-lg` určuje velikost tlačítka

```html
<a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
```

### Kontejner

[dokumentace](https://getbootstrap.com/docs/4.0/layout/overview/#containers)

- `container` vytvoří kontejner s předem definovanou šířkou
- `row` prvky uvnitř se vyskládají do řady
- `col-md-*` kolik částí z řady zabere jeden prvek (celkem 12 částí)

```html
<div class="container">
  <div class="row">
    <div class="col-md-6">
      <h2>About Me</h2>
      <p>
        My name is John Doe and I am a web developer based in New York City. I
        have experience in HTML, CSS, JavaScript, and other web technologies.
      </p>
      <p>When I'm not coding, I enjoy hiking and playing guitar.</p>
    </div>
    <div class="col-md-6">
      <img
        src="https://via.placeholder.com/400x400"
        alt="Profile Picture"
        class="img-fluid"
      />
    </div>
  </div>
</div>
```

### Carousel

[dokumentace](https://getbootstrap.com/docs/4.0/components/carousel/)

Zde je ukázka, jak lze vytvořit Carousel

```html
<div class="container mt-5">
  <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="d-block w-100" src="grey-wall.jpg" alt="First slide" />
      </div>
      <div class="carousel-item">
        <img class="d-block w-100" src="grey-wall.jpg" alt="Second slide" />
      </div>
      <div class="carousel-item">
        <img class="d-block w-100" src="grey-wall.jpg" alt="Third slide" />
      </div>
    </div>
    <a
      class="carousel-control-prev"
      href="#carouselExampleControls"
      role="button"
      data-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="sr-only">Previous</span>
    </a>
    <a
      class="carousel-control-next"
      href="#carouselExampleControls"
      role="button"
      data-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="sr-only">Next</span>
    </a>
  </div>
</div>
```

### Cards

[dokumentace](https://getbootstrap.com/docs/4.0/components/card/)

Třídy `container`, `mt-5`, `row`, `col-md-4`, `btn` a `btn-primary` jsme již viděli. Kartu vytvoříme pomocí následujících tříd:

- `card` definuje kartu
- `card-img-top` definuje obrázek v horní části karty
- `card-body` definuje tělo (to, co je pod obrázkem)
- `card-title` definuje nadpis karty
- `card-text` definuje popisek karty

```html
<div class="container mt-5">
  <div class="row">
    <div class="col-md-4">
      <div class="card">
        <img
          src="https://via.placeholder.com/400x250"
          class="card-img-top"
          alt="..."
        />
        <div class="card-body">
          <h5 class="card-title">Project 1</h5>
          <p class="card-text">This is a description of Project 1.</p>
          <a href="#" class="btn btn-primary">Learn more</a>
        </div>
      </div>
    </div>
  </div>
</div>
```

### Formulář

[dokumentace](https://getbootstrap.com/docs/4.0/components/forms/)

Třídy `container`, `mt-5` a `mb-5` už známe. Navíc zde přibyly třídy:

- `form-group` definuje jednu skupinu, tzn. textové pole a jeho popisek
- `form-control` definuje textové pole

```html
<div class="container mt-5 mb-5">
  <form>
    <div class="form-group">
      <label for="nameInput">Name</label>
      <input
        type="text"
        class="form-control"
        id="nameInput"
        placeholder="Enter your name"
      />
    </div>
  </form>
</div>
```
