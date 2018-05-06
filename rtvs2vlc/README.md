# rtvs2vlc
Video streamy z rtvs je pohodlné prehrávať mimo prehliadač. Našťastie nie sú nijako extra chránené, no už ma unavovalo robiť tú istú činnosť pri každom športe dookola. Tak som si napísal malý skript:

### Požiadavky
Python3 a schopnejší prehrávač

### Ako na to?
Najjednoduchšie použitie pre linux userov v prípade kanálu STV 1: 
```sh
$ vlc `./rtvs2vlc.py 1`
```
V prípade ostatných kanálov vymeniť 1 za príslúšné číslo.

Po spustení samotného skriptu s inými (alebo žiadnymi) argumentmi sa spustí jenoduchý interface, použitie je jasné.

### Poznámky

  - Skript automaticky volí FullHD stream, no stáva sa, že aj ten je niekedy odkazovaný len na HD
  - STV 2 je zdvojené na číslach 2 aj 3, takže v prípade tretieho "bonusového" kanálu označovaného ako Online je potrebné zvoliť 4
  - Výsledná adresa sa nekontroluje na lokalitu. Slovenskú IP musíte mať iba počas spustenia skriptu ;)
