# PYTHON

## Přehled

1. [Co je Python?](#html)
2. [VS code](#vs-code)
3. [Komentář](#komentář)
4. [Řídící struktury](#nadpis)
5. [Funkce](#odstavec)
6. [Pole](#kontejner)
7. [Proměnná](#zalomení-řádku)
8. [OOP](#třídy-a-id)
9. [Dědičnost](#kontejner)
10. [Práce se soubory](#kontejner)
11. [Složitost](#kontejner)
12. [Moduly](#kontejner)
13. [Výjimky](#kontejner)
14. [Vstup/výstup](#kontejner)
15. [Třídící algoritmy](#kontejner)

## Co je Python?

Python je populární programovací jazyk, který vytvořil Guido van Rossum v roce 1991.

Kde se Používá?

- vývoj webových stránek (server-side)
- vývoj softwaru
- datovou analýzu a vizualizaci
- matematické výpočty
- systémové skriptování

Proč právě Python?

- multiplatformní (Windows, Mac, Linux, Raspberry Pi atd.)
- jednoduchá syntaxe
- kratší programy oproti ostatním jazykům
- lze pracovat procedurálním způsobem, objektově orientovaným způsobem nebo funkcionálním způsobem.

## VS code

programy budeme psát ve Visual Studiu Code (VS code)

## Pygame

https://www.pygame.org/news
ofiko stránky

```
python -m pip install -U pygame --user
```

example jestli to funguje

```
python -m pygame.examples.aliens
```

Assety: https://drive.google.com/drive/folders/1TeGCQJZbdFXXj8jcXeF1VT79brvWyOnN?usp=sharing

vytvoříme soubor `main.py`.

Vykreslíme černé okno.

```python
import pygame

WIDTH = 400
HEIGHT = 300
BACKGROUND = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        screen.fill(BACKGROUND)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
```

`WIDTH` a `HEIGHT` nastaví šířku okna. `BACKGROUND` jsou RGB hodnoty uložené jako [tuple](https://www.w3schools.com/python/python_tuples.asp). V metodě main pak iniciujeme `pygame`, vytvoříme `screen` i `clock` a spustíme herní smyčku ve while cyklu.

Všechno, co se bude ve hře dít, se bude odehrávat v herní smyčce. Hra se odehrává v reálném čase, tudíž je potřeba neustále kontrolovat, jestli nebyla zmáčknuta nějaká klávesa, jestli uživatel nezmáčkl myš apod. Toho docílíme pomocí nekonečné smyčky.

`clock.tick(60)` určuje, jak dlouho trvá jeden frame hry (tzn. určuje, jak dlouho trvá každá iterace smyčky), aby hra běžela plynule.

Hra bude mít dvě postavy:

- alien (player)
- box

Abychom se vyhnuli duplicitě kódu, vytvoříme rodičovskou třídu `Sprite`, která dědí z třídy `pygame.sprite.Sprite` (ta později poskytne metody pro detekci kolizí).

```python
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, startx, starty):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.center = [startx, starty]

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
```

Třída má tři metody:

1. `__init__` vytvoří sprite s daným obrázkem a na základě obrázku vytvoří obdélník (který bude sloužit pro pohyb a detekci kolizí). Obdélník bude zpočátku umístěn na pozici zadané pomocí `startx` a `starty`.
2. `update` budeme používat v potomcích pro zpracování událostí (stisky kláves, gravitace a kolize).
3. `draw` použijeme k vykreslení spritu.

Nyní můžeme konečně vytvořit třídy pro `Box` a `Player`, které dědí od třídy `Sprite`.

```Python
class Player(Sprite):
    def __init__(self, startx, starty):
        super().__init__("p1_front.png", startx, starty)

class Box(Sprite):
    def __init__(self, startx, starty):
        super().__init__("boxAlt.png", startx, starty)
```

Vraťme se do funkce `main` a vytvořme postavy, začneme s `player`

```python
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player(100, 200)
```

`player` bude chodit po spritech `box`, těch bude více, proto vytvoříme skupinu sprites.

```python
    player = Player(100, 200)

    boxes = pygame.sprite.Group()
```

Šířka jednoho sprite `box` je 70px a potřebujeme, aby se rozprostíraly přes šířku obrazovky (400px). Využijeme forcyklus.

```python
    boxes = pygame.sprite.Group()
    for bx in range(0,400,70):
        boxes.add(Box(bx,300))
```

V hlavní smyčce budeme zařazovat nové události do fronty událostí pomocí `pygame.event.pump()` a poté volat funkci `player.update()` aktualizující postavu hráče.

```
    while True:
        pygame.event.pump()
        player.update()
```

Potřebujeme vykreslit sprity pomocí metody `draw`.

```python
    while True:
        pygame.event.pump()
        player.update()
        screen.fill(BACKGROUND)

        player.draw(screen)
        boxes.draw(screen)

        pygame.display.flip()
        clock.tick(60)
```
