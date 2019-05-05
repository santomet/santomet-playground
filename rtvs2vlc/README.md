# RTVS2VLC
## UPDATE: Vyzerá to tak, že súdruovia začali geoblockovať úplne všetky requesty. Preto tento projekt a jeho inštancia na santomet.studenthosting.sk už postráda zmysel. Na získavanie samotnej adresy streamu odporúčam [streamlink](https://github.com/streamlink/streamlink)

Skripty sprístupňujú sledovanie živých kanálov a archívu RTVS v externom prehrávači podporujúcom m3u8 playlisty. Taktiež ak pre svoje requesty využijú slovenskú IP, môžu obísť geoblocking, pretože po requeste z výslednej adresy playlistu sa už lokácia neoveruje. Skript je v dvoch verziách - pôvodný python, ktorý je viac proof of concept a php, ktorý bol vytvorený špeciálne na použitie na nejakom slovenskom free hostingu, keďže nájsť použiteľný python hosting je problém celosvetovo, nieto ešte na Slovensku...

## Rýchly prístup - príklady: (skopírovať link a vložiť do prehrávača)
Na androidoch stačí kliknúť, MX Player, ale aj Blink-based prehliadače to prehrajú automaticky :) 

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
  - b volí, že sa má stream načítať vo videojs-contrib-hls prehrávači priamo v browseri. ``` http://santomet.studenthosting.sk/rtvs2vlc.php?c=1&b=true ```
  - q volí kvalitu. ```"auto"``` je defaultná hodnota, ktorá zobrazí adresu na pôvodný m3u8 playlist. Môžete však špecifikovať ```"1080"```, ```"720"```, ```"480"``` alebo ```"360"```


## Python verzia
UŽ DÁVNO NEFUNGUJE
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
