
## Simulace

### Cesta autobusem

Napište program, který simuluje cestu autobusem skrze několik zastávek. Autobus má omezenou kapacitu. Na každé zastávce může přijímat a vypouštět cestující. Na každé zastávce je vytovřen náhodný počet nastupujících lidí. Každý cestující má určenou zastávku, na které vystoupí. Na konečné stanici autobusu vystoupí všichni.

### Ekosystém

Napište program, který simuluje ekosystém. Ekosystém je reprezentován jako 2D mřížka. Každé políčko je buď prázdné, nebo je na něm strom, nebo je na něm zvíře. Na začátku je na různá místa v mřížce náhodně umístěněno několik stromů a několik zvířat. Zvířata se živí stromy, vždy, když zvíře sní strom, doplní svou energii na maximum. Pokud v dané kroku zvíře nesní strom, klesne mu energie o 1. V každém kroku se zvíře přesune na jedno ze sousedních políček. Pokud je na novém políčku strom, zvíře ho sní. V každém kroku na několika náhodných místech vyroste nový strom.

### Lesní požár

Napište program, který simuluje šíření lesního požáru v 2D mřížce. Každé políčko mřížky může být prázdné, obsahovat strom nebo být v plamenech. V každém kroku se požár rozšíří na vedlější políčko, pokud je na vedlejším políčku strom. V každém kroku na několika náhodných políčcích vyroste nový strom. Každých několik kroků se vybere náhodné políčko, kde vznikne požár.

### Epidemiologické šíření

Napište program, který simuluje šíření infekčního onemocnění v populaci. Na začátku je vytvořena populace několika osob. Některé z nich jsou na začátku nakaženy. V každém kroku se vybere několik dvojic lidí, které se spolu potkaly. Pro každou dvojici platí následující pravidla:

- pokud jsou obě osoby v dvojici zdravé, nic se neděje
- pokud jsou obě osoby v dvojici nakažené, nic se neděje
- pokud je jedna osoba ve dvojici nakažená a druhá zdravá, pak se zdravá osoba s určitou pravděpodobností nakazí

Každá osoba se po uplynutí určité doby uzdraví a získává rezistenci.

### Obchodní centrum

Napište program, který simuluje chování zákazníků v obchodním centru. V centru máme několik obchodů. Na začátku simulace se vygeneruje určitý počet zákazníků. Každý zákazník má seznam obchodů, které musí navštívit. Také má každý zákazník nastavenou trpělivost, jak dlouho dokáže stát ve frontě. Zákazník navštěvuje obchody podle toho, jak jsou napsané v seznamu. Vždy přijde do obchodu, postaví se do fronty a čeká. Pokud mu dojde trpělivost ve frontě, přechází do dalšího obchodu (později se však do daného ochodu vrátí). V každém kroku simulace se fronta zákazníků zmenší o jednoho zákazníka (v každém kroku je jeden zákazník obsloužen). Když je zákazník obsloužen, přechází do dalšího obchodu ze seznamu, případně odchází z obchodního centra, když navštívil všechny obchody.

### Call centrum

### Převoz písku