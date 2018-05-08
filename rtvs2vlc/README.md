# rtvs2vlc
Video streamy z rtvs je pohodlné prehrávať mimo prehliadač. Našťastie nie sú nijako extra chránené, no už ma unavovalo robiť tú istú činnosť pri každom športe dookola. Tak som si napísal malý skript.

## PHP verzia
Stačí nahrať skript na php server so slovenskou IP. Kým mi to nezrušia, príklad je na následujúcej adrese. Tú stačí zadať do prehrávača:
```
http://santomet.studenthosting.sk/rtvs2vlc.php?c=1?r=true
```
  - c je číslo kanála
  - r volí, že sa má adresa presmerovať kódom 303. Ináč sa adresa na playlist len vypíše (oba spôsoby by mali fungovať vo VLC)


## Python verzia
Potrebuješ python3.
Najjednoduchšie použitie pre linux userov v prípade kanálu STV 1: 
```sh
$ vlc `./rtvs2vlc.py 1`
```
V prípade ostatných kanálov opäť vymeniť 1 za príslúšné číslo.

Po spustení samotného skriptu s inými (alebo žiadnymi) argumentmi sa spustí jenoduchý interface, použitie je jasné.


### Poznámky

  - Skripty automaticky volia FullHD stream, no stáva sa, že aj ten je niekedy odkazovaný len na HD
  - STV 2 je zdvojené na číslach 2 aj 3, takže v prípade tretieho "bonusového" kanálu označovaného ako Online je potrebné zvoliť 4
  - Výsledná adresa často nekontroluje geolokáciu. Slovenskú IP musíte mať iba počas spustenia skriptu ;)
