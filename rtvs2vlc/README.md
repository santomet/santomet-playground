# rtvs2vlc
Video streamy z rtvs je pohodlné prehrávať mimo prehliadač. Našťastie nie sú nijako extra chránené, no už ma unavovalo robiť tú istú činnosť pri každom športe dookola. Tak som si napísal malý skript.

## Python verzia
Potrebuješ schopnejší prehrávač a python3.
Najjednoduchšie použitie pre linux userov v prípade kanálu STV 1: 
```sh
$ vlc `./rtvs2vlc.py 1`
```
V prípade ostatných kanálov vymeniť 1 za príslúšné číslo.

Po spustení samotného skriptu s inými (alebo žiadnymi) argumentmi sa spustí jenoduchý interface, použitie je jasné.


## PHP verzia
Stačí nahrať sa (slovenský) php server a do prehrávača rovno zadať adresu napr:
```
http://santomet.php5.sk/rtvs2vlc.php?c=1
```
Opäť, v tomto prípade pre kanál STV1. Php skript je na danej adrese nahraný, avšak php5.sk sa hosťuje v česku, takže geolokáciu neoklameme :(
Bohužiaľ som totiž nenašiel schopný na slovensku hosťovaný php free hosting (a už vôbec nie php). Ak by ste o niečom vedeli, dajte vedieť!

### Poznámky

  - Skripty automaticky volia FullHD stream, no stáva sa, že aj ten je niekedy odkazovaný len na HD
  - STV 2 je zdvojené na číslach 2 aj 3, takže v prípade tretieho "bonusového" kanálu označovaného ako Online je potrebné zvoliť 4
  - Výsledná adresa často nekontroluje geolokáciu. Slovenskú IP musíte mať iba počas spustenia skriptu ;)
