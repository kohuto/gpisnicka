# DYNAMICKÉ WEBOVÉ STRÁNKY

Představ si webovou aplikaci jako dvě hlavní části, které spolu komunikují:

### Klientská strana
- **Co to je?**  
  Jedná se o vše, co se odehrává přímo v prohlížeči uživatele.  
- **Co se tam spouští?**  
  Kód, který jsi napsal v HTML, CSS a JavaScriptu.  
- **Co dělá?**  
  - Zobrazuje obsah stránky (HTML a CSS).  
  - Zpracovává uživatelské akce, jako jsou kliknutí, psaní do formulářů apod.  
  - Může komunikovat se serverem (např. pomocí AJAX nebo fetch), aby získal nebo poslal data.

### Serverová strana
- **Co to je?**  
  Jedná se o vzdálený počítač nebo cloudovou službu, kde běží tvá aplikace a data.  
- **Co se tam spouští?**  
  Serverový kód napsaný například v PHP, Node.js, Pythonu, Ruby nebo Javě.  
- **Co dělá?**  
  - Přijímá požadavky od klienta (např. při načtení stránky nebo odeslání formuláře).  
  - Zpracovává tyto požadavky, například ověřuje přihlašovací údaje nebo načítá data z databáze.  
  - Vytváří a posílá odpovědi zpět klientovi (obvykle ve formě HTML, JSON apod.).

### Jak spolupracují
- **Klient odešle požadavek:**  
  Když klikneš na tlačítko nebo načteš stránku, tvůj prohlížeč pošle požadavek na server.
- **Server požadavek zpracuje:**  
  Server provede potřebné operace (např. načte data z databáze, ověří přihlášení) a připraví odpověď.
- **Klient dostane odpověď:**  
  Prohlížeč obdrží data a podle nich aktualizuje zobrazení stránky, případně spustí další JavaScript.

### Shrnutí
- **Klientská strana:**  
  Běží v prohlížeči, vykresluje a interaktivně upravuje obsah stránky pomocí HTML, CSS a JavaScriptu.
- **Serverová strana:**  
  Běží na serveru, zpracovává požadavky, pracuje s databázemi a provádí složitější logiku, a pak posílá výsledky zpět klientovi.

Tento přístup odděluje to, co vidíš a s čím interaguješ, od těžké logiky a práce s daty, která běží „na pozadí“.

## DOM tree
### Co je to **DOM Tree**?

**DOM (Document Object Model) Tree** je **stromová struktura**, kterou prohlížeč vytváří z HTML kódu stránky. Každý HTML element (značka jako `<div>`, `<p>`, `<h1>`, `<ul>` apod.) se v této struktuře stává uzlem (node). DOM strom umožňuje JavaScriptu dynamicky měnit obsah stránky.

![dom tree](./DOM-Tree1.webp)

Obrázek výše ukazuje **převod HTML kódu do struktury DOM stromu**.

#### **1. HTML kód vlevo**
Tento kód představuje jednoduchou webovou stránku, která obsahuje:
- **Hlavičku** (`<head>`) s titulkem (`<title>`).
- **Tělo stránky** (`<body>`), ve kterém je:
  - `<div>` obsahující nadpis (`<h1>`), odstavec (`<p>`) a nečíslovaný seznam (`<ul>`), který má jeden prvek (`<li>`).

#### **2. Struktura DOM stromu vpravo**
Na pravé straně obrázku vidíme, jak je tento HTML kód převeden do **DOM stromu**:
- **Nejvyšší uzel (kořen)** je `Document`, což představuje celý HTML dokument.
- **Pod ním** je uzel `HTML`, který má dvě hlavní větve:
  - `Head` → obsahuje `Title`
  - `Body` → obsahuje `div`, který má další potomky:
    - `h1` (nadpis)
    - `p` (odstavec)
    - `ul` (seznam), který má pod sebou `li` (položku seznamu)

---

### **Jak to souvisí s JavaScriptem?**
DOM strom umožňuje **JavaScriptu přistupovat k jednotlivým prvkům stránky a měnit jejich obsah**.

Například:
```javascript
document.querySelector("h1").textContent = "Nový nadpis";
```
Tento kód vyhledá v DOM stromu element `<h1>` a změní jeho text.

## Javascript

Příklad níže je základní **dynamická webová aplikace**, která ukazuje, jak JavaScript může měnit obsah webu! Aplikace umožňuje:

1. **Změnit text na stránce** podle zadaného jména.
2. **Přidávat a odebírat úkoly** do seznamu.

```html
<!DOCTYPE html>
<html lang="cs">
<head>
    <title>Dynamická stránka s JavaScriptem</title>
</head>
<body>

    <h1 id="headline">Ahoj, uživateli!</h1>
    
    <input type="text" id="nameInput" placeholder="Zadej své jméno">
    <button onclick="changeName()">Změnit jméno</button>

    <h2>Seznam úkolů</h2>
    <input type="text" id="taskInput" placeholder="Nový úkol">
    <button onclick="addTask()">Přidat úkol</button>

    <ul id="taskList"></ul>

    <script>
        function changeName() {
            let name = document.getElementById("nameInput").value;
            let headline = document.getElementById("headline");

            if (name.trim() !== "") {
                headline.textContent = "Ahoj, " + name + "!";
                document.getElementById("nameInput").value = "";
            }
        }
        function addTask() {
            let taskInput = document.getElementById("taskInput");
            let taskText = taskInput.value.trim();
            if (taskText !== "") {
                let li = document.createElement("li");
                li.textContent = taskText;

                // Přidání tlačítka pro odstranění
                let deleteBtn = document.createElement("button");
                deleteBtn.textContent = "❌";
                deleteBtn.style.marginLeft = "10px";
                deleteBtn.onclick = function() {
                    li.remove();
                };
                li.appendChild(deleteBtn);
                document.getElementById("taskList").appendChild(li);
                taskInput.value = ""; // Vymazání vstupu
            }
        }
    </script>

</body>
</html>

```

## **Vysvětlení kódu**

### 1️⃣ **Funkce `changeName()` – změna textu**
Tato funkce se spustí, když uživatel klikne na tlačítko „Změnit jméno“.

```javascript
function changeName() {
    let name = document.getElementById("nameInput").value;
    let headline = document.getElementById("headline");

    if (name.trim() !== "") {
        headline.textContent = "Ahoj, " + name + "!";
        document.getElementById("nameInput").value = "";
    }
}
```

#### **Jak to funguje?**
1. **Získání vstupního textu z prvku, které má ID "nameInput"**  
   `document.getElementById("nameInput").value` → získá hodnotu z textového pole.
2. **Najdeme prvek, který má ID "headline"**  
   `document.getElementById("headline")` → získá element `<h1>`, kde se změní text.
3. **Zkontrolujeme, zda uživatel něco zadal**  
   `name.trim() !== ""` → trim() odstraní mezery na začátku a konci, takže prázdný vstup neprojde.
4. **Změníme obsah nadpisu**  
   `headline.textContent = "Ahoj, " + name + "!";` → nadpis se změní podle jména uživatele.
5. **Vymažeme vstupní pole**  
   `document.getElementById("nameInput").value = "";` → smaže obsah vstupního pole po kliknutí.

---

### 2️⃣ **Funkce `addTask()` – přidání úkolu do seznamu**
Tato funkce se spustí, když uživatel klikne na tlačítko „Přidat úkol“.

```javascript
function addTask() {
    let taskInput = document.getElementById("taskInput");
    let taskText = taskInput.value.trim();
    if (taskText !== "") {
        let li = document.createElement("li");
        li.textContent = taskText;

        // Přidání tlačítka pro odstranění
        let deleteBtn = document.createElement("button");
        deleteBtn.textContent = "❌";
        deleteBtn.style.marginLeft = "10px";
        deleteBtn.onclick = function() {
            li.remove();
        };
        li.appendChild(deleteBtn);
        document.getElementById("taskList").appendChild(li);
        taskInput.value = ""; // Vymazání vstupu
    }
}
```

#### **Jak to funguje?**
1. **Získáme text nového úkolu**  
   `let taskText = taskInput.value.trim();`  
   → odstraníme mezery na začátku a konci, abychom předešli prázdným úkolům.
2. **Pokud není prázdný, vytvoříme `<li>` element**  
   `let li = document.createElement("li");`  
   → vytvoří nový `<li>` (položku seznamu).
3. **Nastavíme jeho text**  
   `li.textContent = taskText;`
4. **Vytvoříme tlačítko „❌“ pro smazání úkolu**  
   - `let deleteBtn = document.createElement("button");` → vytvoříme tlačítko.
   - `deleteBtn.textContent = "❌";` → nastavíme text na „❌“.
   - `deleteBtn.style.marginLeft = "10px";` → přidáme odsazení tlačítka.
   - `deleteBtn.onclick = function() { li.remove(); };` → po kliknutí se odstraní odpovídající `<li>`.
5. **Připojíme tlačítko k úkolu a úkol k seznamu**  
   - `li.appendChild(deleteBtn);` → přidáme tlačítko do `<li>`.
   - `document.getElementById("taskList").appendChild(li);` → přidáme nový úkol do seznamu `<ul>`.
6. **Vymažeme textové pole**  
   `taskInput.value = "";` → po přidání úkolu se vstupní pole vyprázdní.

