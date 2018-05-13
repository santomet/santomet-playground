# rtvs2vlc
Video streamy je pohodlné prehrávať mimo prehliadač. Našťastie, na RTVS nie sú nijako extra chránené. Tento skript však prácu zjednodušuje. Taktiež ak sa hosťuje na zariadení so slovenskou IP, môže obísť geoblocking.
## Rýchly prístup: (skopírovať link a vložiť do prehrávača)
[STV 1](http://santomet.studenthosting.sk/rtvs2vlc.php?c=1&r=true)

[STV 2](http://santomet.studenthosting.sk/rtvs2vlc.php?c=2&r=true)

[STV online](http://santomet.studenthosting.sk/rtvs2vlc.php?c=4&r=true)

Taktiež je možné použiť jednoducho zapamätateľné redirect linky:

```
http://stv1.dopi.ci
http://stv2.dopi.ci
http://stv3.dopi.ci
```


[Archív: Slovensko - Švajčiarsko](http://santomet.studenthosting.sk/rtvs2vlc.php?c=155614&r=true)

## PHP verzia
Stačí nahrať skript na php server so slovenskou IP. Kým mi to nezrušia, príklad je na následujúcej adrese. Tú stačí zadať do prehrávača:
```
http://santomet.studenthosting.sk/rtvs2vlc.php?c=1&r=true
```
  - c je číslo kanála. STV1 je n čísle 1. Taktiež môžeš použiť číslo relácie z archívu (posledná časť adresy)
  - r volí, že sa má adresa presmerovať kódom 303. Ináč sa adresa na playlist len vypíše (oba spôsoby by mali fungovať vo VLC)


## Python verzia
Potrebuješ python3.
Najjednoduchšie použitie pre linux userov: 
```sh
$ vlc `./rtvs2vlc.py 1`
```
V prípade ostatných kanálov vymeniť 1 za príslúšné číslo.

Po spustení samotného skriptu s inými (alebo žiadnymi) argumentmi sa spustí jenoduchý interface, použitie je jasné.


### Poznámky

  - Oba skripty automaticky volia FullHD stream, no stáva sa, že aj ten je niekedy odkazovaný len na HD
  - STV 2 je zdvojené na číslach 2 aj 3, takže v prípade tretieho "bonusového" kanálu označovaného ako Online je potrebné zvoliť 4
  - Výsledná adresa často nekontroluje geolokáciu. Slovenskú IP musíte mať iba počas spustenia skriptu ;)
