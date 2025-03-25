# Tutoriál: Tvorba jednoduché GUI aplikace v Pythonu s využitím knihovny `tkinter`

## Význam GUI aplikací

GUI (Graphical User Interface) neboli grafické uživatelské rozhraní umožňuje uživateli ovládat aplikaci prostřednictvím grafických prvků – tlačítek, textových polí, výběrových seznamů apod.

Oproti **konzolovým aplikacím**, které komunikují se uživatelem přes textový vstup/výstup v příkazové řádce, jsou GUI aplikace:

- **přehlednější a uživatelsky přívětivější**
- **vhodnější pro koncové uživatele**, kteří nejsou zvyklí na terminál
- **schopné zpracovávat více vstupů a událostí najednou**

## Knihovna `tkinter`

Zdrojový kód popsaný níže naleznete v souboru [aplikace s gui](gui.py).

V Pythonu je nejpoužívanější knihovnou pro tvorbu GUI **`tkinter`**, která je součástí standardní instalace.

Importujeme ji jednoduše:
```python
import tkinter as tk
```

Dále budeme potřebovat knihovnu `threading` pro práci s vlákny:
```python
import threading
```

## Grafické prvky v aplikaci

### Hlavní okno

Každá aplikace musí mít hlavní okno:
```python
root = tk.Tk()
root.title("Fibonacci Calculator")
```

### Rámečky (`Frame`)

Rámečky slouží k logickému rozdělení GUI. Lze je vnořovat a používat pro skupiny prvků:
```python
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()
```

### Štítky (`Label`)

Zobrazují text v GUI:
```python
tk.Label(input_frame, text="Zadejte číslo n:")
result_label = tk.Label(main_frame, text="Výsledek se zobrazí zde", font=("Arial", 12))
```

### Textové pole (`Entry`)

Umožňuje uživateli zadat vstup:
```python
entry = tk.Entry(input_frame, width=10)
```

### Tlačítka (`Button`)

Slouží k vykonání akce po kliknutí:
```python
button_compute = tk.Button(button_frame, text="Spočítej Fibonacciho číslo", command=calculate_fib)
button_quit = tk.Button(button_frame, text="Ukončit", command=root.quit)
```

## Layout – rozměstění prvků

V tkinteru existují tři základní způsoby umisťování prvků:
- **`pack()`** – nejjednodušší, řadí prvky pod sebe nebo vedle sebe
- **`grid()`** – pracuje s tabulkovým rozložením (řádky a sloupce)
- **`place()`** – umožňuje přesné umístění podle souřadnic (méně často používané)

V tomto projektu používáme `grid()` i `pack()`:
```python
main_frame.pack()
input_frame.grid(row=0, column=0, columnspan=2, pady=10)
```

## Událostmi řízené programování

V GUI aplikacích neexistuje "hlavní smyčka", která by lineárně prováděla kód. Místo toho aplikace čeká na **události** (např. kliknutí myši, zadání vstupu) a na základě nich spouští funkce.

Příklad:
```python
button_compute = tk.Button(..., command=calculate_fib)
```
Po kliknutí na tlačítko se zavolá funkce `calculate_fib()`.

## Asynchronní a vícevláknové aplikace

Když napíšeme klasickou funkci v Pythonu a zavoláme ji, Python ji vykoná krok za krokem a **nepustí se do ničeho jiného, dokud ji celou nedokončí**. Takový postup ale může v grafickém rozhraní způsobit, že se okno **zasekne**, nereaguje na kliknutí nebo nelze zavřít.

### Vlákna (threads)

Aby GUI zůstalo funkční i během náročných operací (např. výpočet Fibonacciho čísla pro vysoké `n`), spustíme tento výpočet v jiném tzv. **vlákně**. 

Vlákno je jako "vedlejší cesta" běžící souběžně s hlavím programem. Pomocí knihovny `threading` lze vlákno spustit jednoduše:

```python
threading.Thread(target=nejaka_funkce).start()
```

Tato funkce se běží na pozadí, zatímco hlavní program (včetně GUI) je stále aktivní.

**Pozor:** Vlákno nesmí přímo měnit prvky GUI! Tkinter totiž není vlákno-bezpečný. 
Když potřebujeme něco zobrazit v GUI z vedlejšího vlákna, použijeme `after()`:

```python
result_label.after(0, lambda: result_label.config(text="Hotovo"))
```

### Asynchronní programování (async/await)

Asynchronní programování je jiný způsob, jak pracovat s operacemi, které trvají delší dobu (např. čtení ze souboru, čekání na odpověď serveru apod.). Místo vláken se používá klíčové slovo `async` pro definici asynchronní funkce a `await` pro čekání na její dokončení:

```python
import asyncio

async def pozdrav():
    await asyncio.sleep(1)
    print("Ahoj")

asyncio.run(pozdrav())
```

Asynchronní programy jsou čistější a efektivnější pro práci s mnoha čekajícími operacemi, ale **v tkinteru se používají méně často**. Pro jednoduchost se v GUI častěji pracuje s vlákny (`threading`), protože je jejich použití snazší a dobře integrovatelné s událostmi GUI.

Shrnuto:
- **Vlákna** jsou ideální pro spouštění dělších operací bez zablokování GUI
- **Asynchronní kód (async/await)** je vhodný pro moderní webové nebo serverové aplikace
- V tkinter projektech se častěji setkáme s knihovnami jako `threading` nebo `concurrent.futures`

## Shrnutí

Tato aplikace ukazuje:
- jak vytvořit jednoduché GUI pomocí `tkinter`
- použití základních grafických prvků (label, entry, button)
- rozměstění pomocí `grid` a `pack`
- jak reagovat na události (kliknutí)
- jak správně využít vlákna, aby se GUI nezasekávalo

Tuto strukturu lze dále rozšiřovat např. o `canvas`, `radiobutton`, `checkbutton`, `listbox` nebo `menu`.

