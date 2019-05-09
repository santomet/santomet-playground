# RTVS2VLC

Skripty sprístupňujú sledovanie živých kanálov a archívu RTVS v externom prehrávači podporujúcom m3u8 playlisty. Taktiež ak pre svoje requesty využijú slovenskú IP, môžu obísť geoblocking, pretože po requeste z výslednej adresy playlistu sa už lokácia neoveruje. Skript je v dvoch verziách - pôvodný python, ktorý je viac proof of concept a php, ktorý bol vytvorený špeciálne na použitie na nejakom slovenskom free hostingu, keďže nájsť použiteľný python hosting je problém celosvetovo, nieto ešte na Slovensku...

Po prvej inštancii projektu urobili tesne pred hokejovými majstrovstvami súdruhovia v RTVS malé zmeny, ktoré tento projekt znefunkčnili. Ja však mám hru na mačku a myš veľmi rád, takže aktualizovaný skript dokáže pracovať aj s touto úpravou a navyše je tam aj experimentálny režim, ktorý počíta aj s ďalšou možnou zmenou do budúcnosti.


## PHP verzia
Stačí nahrať skript na php server so slovenskou IP. Kým mi to nezrušia, príklad je na následujúcej adrese. Tú stačí zadať do prehrávača:
```
http://santomet.studenthosting.sk/rtvs2vlc.php?c=1
```
  - c je číslo kanála. STV1 je n čísle 1. Taktiež môžeš použiť číslo relácie z archívu (posledná časť adresy)
  - r volí, že sa má adresa presmerovať kódom 303. Ináč sa adresa na playlist len vypíše (oba spôsoby by mali fungovať vo VLC)
  - b volí, že sa má stream načítať vo videojs-contrib-hls prehrávači priamo v browseri. ``` rtvs2vlc.php?c=1&b=true ``` Nezlučiteľné s argumentom r !!!
  - q volí kvalitu. ``` rtvs2vlc.php?c=1&q=auto ``` je defaultná hodnota, ktorá zobrazí adresu na pôvodný m3u8 playlist. Môžete však špecifikovať ```1080```, ```720```, ```480``` alebo ```360```. VLC s tým dokáže pracovať automaticky, avšak spolu s argumentom b sa oplatí špecifikovať kvalitu explicitne.
  - e je experimentálny režim. ``` rtvs2vlc.php?c=1&q=1080&e=true ``` V zásade prejde všetky úrovne playlistov a z posledného, pozostávajúceho priamo z .ts chunkov vybuduje vlastný playlist. V tomto režime MUSÍTE špecifikovať kvalitu explicitne. Režim som vymslel, pretože sa mi geoblocking na úrovni všetkých m3u8 playlistov javí ako ďalšia logická zmena, ktorú by mohli súdruhovia aplikovať.

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

  - STV 2 je zdvojené na číslach 2 aj 3, takže v prípade tretieho "bonusového" kanálu označovaného ako Online je potrebné zvoliť 4
