# LATEX

## Přehled

1. [Co je LATEX?](#co-je-latex)
2. [Overleaf](#overleaf)
3. [První dokument](#první-dokument)
4. [Preambule dokumentu](#preambule-dokumentu)
5. [Komentáře](#komentáře)
6. [Tučné, kurzíva, podtržení](#tučné-kurzíva-podtržení)
7. [Obrázky](#obrázky)
8. [Popisky](#popisky)
9. [Seznamy](#seznamy)
10. [Matematika](#matematika)
11. [Abstrakt](#abstrakt)
12. [Odstavec](#odstavce)
13. [Kapitoly a sekce](#kapitoly-a-sekce)
14. [Tabulky](#tabulky)
15. [Kód a pseudokód](#kód-a-pseudokód)
16. [Obsah](#obsah)
17. [Závěr](#závěr)

## Co je LaTeX

LaTeX je nástroj pro sazbu profesionálně vypadajících textů zaměřený na vytváření technických a vědeckých dokumentů. Není to běžný “WYSIWYG” (what you see is what you get) editor. Podobně jako v HTML je struktura a obsah textu definován pomocí značek.

LaTeX je založen na TeXu, který byl vyvinut v roce 1978 Donaldem Knuthem. TeX je mocný a komplexní typografický systém, zatímco LaTeX nabízí sadu maker nad TeXem, což umožňuje snazší a intuitivnější práci.

Hlavními výhodami LaTeXu jsou:

1. **Vysoká kvalita typografie:** Dokumenty vytvořené v LaTeXu mají profesionální vzhled díky preciznímu ladění mezer, zarovnání a formátování.
2. **Strukturované psaní:** Autor se může soustředit na strukturu a obsah dokumentu bez nutnosti řešit vizuální prezentaci.
3. **Vynikající podpora pro matematiku:** Matematické vzory a rovnice jsou ve výstupu z LaTeXu precizní a čitelné.
4. **Rozšířitelnost:** Existují tisíce balíčků, které rozšiřují funkčnost LaTeXu, od složitých tabulek po grafiku a bibliografické odkazy.
5. **Přenositelnost:** LaTeXové dokumenty můžete kompilovat na různých platformách bez změny výstupu.

Princip LaTeXu spočívá v tom, že autor píše text a zároveň do něj vkládá příkazy, které označují, jak by měly jednotlivé části textu vypadat nebo jak by měly být formátovány. Tento zdrojový kód je následně "zkompilován" do výsledného dokumentu ve formátu PDF nebo jiném výstupním formátu.

## Overleaf

[Overleaf](https://www.overleaf.com/) je online platforma pro spolupráci a psaní vědeckých a technických dokumentů v LaTeXu. Je to jeden z nejoblíbenějších cloudových editorů pro LaTeX a nabízí řadu nástrojů, které zjednodušují proces vytváření a sdílení LaTeXových dokumentů.

Hlavní vlastnosti a výhody Overleafu zahrnují:

1. **Real-time spolupráce:** Umožňuje více autorům pracovat na stejném dokumentu současně, s možností vidět změny provedené ostatními v reálném čase.
2. **Online kompilace:** Nemusíte mít nainstalován LaTeX na svém počítači, protože Overleaf kompiluje dokumenty online a ukazuje vám výsledné PDF.
3. **Integrované verzování:** Overleaf automaticky sleduje revize vašeho dokumentu, takže můžete snadno vrátit změny nebo procházet historii revizí.
4. **Šablony a příklady:** Platforma nabízí širokou škálu předdefinovaných šablon pro články, prezentace, disertační práce, životopisy a další typy dokumentů.
5. **Integrované nástroje pro publikování:** Overleaf často poskytuje přímou integraci s vědeckými časopisy, což usnadňuje proces odesílání článků.
6. **Rich-Text nebo Zdrojový Režim:** Uživatelé mohou pracovat v tradičním zdrojovém režimu LaTeXu nebo v režimu rich-text, který je více podobný běžným textovým procesorům.
7. **Kompatibilita:** Overleaf je kompatibilní s mnoha balíčky a styly LaTeXu, takže je velmi pravděpodobné, že budete moci pracovat bez problémů na jakémkoli projektu.

## První dokument

Níže vidíte nejjednodušší příklad, který lze vytvořit v Overleaf:

```latex
\documentclass{article}
\begin{document}
First document. This is a simple example, with no
extra parameters or packages included.
\end{document}
```

První řádek kódu `\documentclass{article}` definuje typ dokumentu (zde `article`) nazvaný jako _třída_. Další typy dokumentů vyžadují další třídy (př. resume). Tělo dokumentu je vepsáno mezi `\begin{document}` a `\end{document}`.

V momentě, kdy provedete nějaké změny v dokumentu, stačí zmáčknout tlačítko `Recompile` a dokument se aktualizuje (případně `ctrl`+`s`).

## Preambule dokumentu

Vše, co napíšeme před příkaz `\begin{document}` nazýváme preambule. Preambule slouží jako sekce "nastavení". Nastavujeme zde třídu, jazyk, nahráváme balíčky atd. Příkladem může být třeba následující preambule:

```latex
\documentclass[12pt, letterpaper]{article}
\usepackage{graphicx}
```

- `article` již známe
- `12pt` veliksot písma v dokumentu
- `letterpaper` formát papíru (A4)
- `\usepackage{graphicx}` příkaz pro vložení balíčku.

Tento umožňuje práci s grafikou (vkládání obrázků atd.)

Můžeme přidat i název dokumentu, autora a datum.

```latex
\documentclass[12pt, letterpaper]{article}
\title{My first LaTeX document}
\author{Hubert Farnsworth\thanks{Funded by the Overleaf team.}}
\date{August 2022}
```

Pro vykrelsení stačí vložit `\maketitle` do těla dokumentu.

## Komentáře

Komentáře se v LaTeXu zapisují pomocí znaku `%`:

```latex
\begin{document}
We have now added a title, author and date to our first LaTeX document!

% This line here is a comment. It will not be typeset in the document.
\end{document}
```

## Tučné, kurzíva, podtržení

```latex
Tento text je \textbf{tučný}
Tento text je \underline{podtžený}
Tento text je \textit{kurzívou}
```

## Obrázky

Pro přidání obrázku musíme obrázek první nahrát do Overleaf projektu. Následujícím způsobem ho poté můžeme přidat do dokumentu:

```latex
\documentclass{article}
\usepackage{graphicx} %LaTeX package to import graphics
\graphicspath{{images/}} %configuring the graphicx package

\begin{document}
\includegraphics{universe}

There's a picture of a galaxy above.
\end{document}
```

Příkaz `\graphicspath{{images/}}` informuje LaTeX, že obrázky jsou uloženy ve složce _images_ v aktuálním adresáři. Příkaz `\includegraphics{universe}` zajistí samotné vložení obrázku _universe_ (bez koncovky) do dokumentu.

## Popisky

```latex
\documentclass{article}
\usepackage{graphicx}
\graphicspath{{images/}}

\begin{document}

\begin{figure}[h]
    \centering
    \includegraphics[width=0.75\textwidth]{mesh}
    \caption{A nice plot.}
    \label{fig:mesh1}
\end{figure}

As you can see in figure \ref{fig:mesh1}, the function grows near the origin. This example is on page \pageref{fig:mesh1}.

\end{document}
```

Vysvětlení kódu výše:

- `\includegraphics[width=0.75\textwidth]{mesh}`: Nastavení šířky obrázku na 75% šířky textu
- `\caption{A nice plot.}`: popisek obrázku
- `\label{fig:mesh1}`: Reference na obrázek ze zbytku dokumentu. Příkaz vygeneruje číslo obrázku a umožňuje se na něj odkázat
- `\ref{fig:mesh1}`: Příkaz je nahrazen číslem obrázku, na který je odkazováno.

## Seznamy

Nečíslovaný seznam lze vytvořit následovně:

```latex
\begin{itemize}
  \item The individual entries are indicated with a black dot, a so-called bullet.
  \item The text in the entries may be of any length.
\end{itemize}
```

Číslovaný seznam lze vytvořit následovně:

```latex
\begin{enumerate}
  \item This is the first entry in our list.
  \item The list numbers increase with each entry we add.
\end{enumerate}
```

## Matematika

Zápis matematických formulí je jednou z největších výhod LaTeXu. Lze psát dvěma způsoby - _inline_ (uvnitř textu) a _display_ (zobrazí se na samostatný řádek).

Pro _inline_ způsob zápisu lze použít jednu z následujících dvojic: `\( ... \)`, `$ ... $` nebo `\begin{math} ... \end{math}`

Pro _display_ způsob zápisu lze použít jednu z následujících dvojic: `\[ ... \]`, `\begin{displaymath} ... \end{displaymath}` nebo `\begin{equation} ... \end{equation}`.

> Často lze vidět ještě dvojici `$$ ... display math here ...$$`, která již však není doporučena používat.

Většina matematických zápisů, které kdy budete potřebovat naleznete v tomto [taháku](https://drive.google.com/file/d/1LG9sXVlvMINXu_qb6DLW3v2zLDIaaHV8/view?usp=sharing).

## Abstrakt

Abstrakt je stručné text shrnující obsah a výsledky obsahu článku. V LaTeXu ho zapíšeme následovně:

```latex
\documentclass{article}
\begin{document}
\begin{abstract}
This is a simple paragraph at the beginning of the
document. A brief introduction about the main subject.
\end{abstract}
\end{document}
```

## Odstavce

Nový odstavec vytvořit vytvoříme vložením dvou `Enter`. Pokud chceme nový řádek, ale ne nový odstavec, použijeme příkaz `\\`

## Kapitoly a sekce

Následující ukázka demonstruje členění delšího textu:

```latex
\documentclass{book}
\begin{document}

\chapter{First Chapter}

\section{Introduction}

This is the first section.

Lorem  ipsum  dolor  sit  amet,  consectetuer  adipiscing
elit. Etiam  lobortisfacilisis sem.  Nullam nec mi et
neque pharetra sollicitudin.  Praesent imperdietmi nec ante.
Donec ullamcorper, felis non sodales...

\section{Second Section}

Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Etiam lobortis facilisissem.  Nullam nec mi et neque pharetra
sollicitudin.  Praesent imperdiet mi necante...

\subsection{First Subsection}
Praesent imperdietmi nec ante. Donec ullamcorper, felis non sodales...

\section*{Unnumbered Section}
Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Etiam lobortis facilisissem...
\end{document}
```

Většina příkazu je sebevysvětlujících, poznamenáme pouze, že přííkazy `\part` a `\chapter` lze použít pouze ve třídách `report` a `book`

## Tabulky

Tvorba tabulek je v LaTeXu (dle mého názoru) natolik nepěkná, že doporučuji raději použít kterýkoliv online [generátor tabulek](https://tableconvert.com/latex-generator)

## Kód a pseudokód

## Obsah

O většinu práce se postará příkaz `\tableofcontents`

## Závěr

V případě, že je dokument připraven, stačí stisknout tlačítko pro stažení a stáhne se PDF dokument.
