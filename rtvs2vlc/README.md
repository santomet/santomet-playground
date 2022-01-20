# RTVS2VLC

Skripty sprístupňujú sledovanie živých kanálov a archívu RTVS v externom prehrávači podporujúcom m3u8 playlisty. Taktiež ak pre svoje requesty využijú slovenskú IP, môžu obísť geoblocking, pretože po requeste z výslednej adresy playlistu sa už lokácia neoveruje. Skript je napísaný v nenávidenom PHP, keďže nájsť slovenský freehosting nie je taký problém...

Po prvej inštancii projektu urobili tesne pred hokejovými majstrovstvami súdruhovia v RTVS malé zmeny, ktoré tento projekt znefunkčnili. Ja však mám hru na mačku a myš veľmi rád, takže aktualizovaný skript dokáže pracovať aj s touto úpravou a navyše je tam aj experimentálny režim, ktorý počíta aj s ďalšou možnou zmenou do budúcnosti.

Rovnako pred časom urobili ďalšiu nepodstatnú zmenu, a keďže sa blíži olympiáda v Pekingu, tak som to znova spojazdnil.

## PHP verzia
Stačí nahrať skript na php server so slovenskou IP.
  - c je číslo kanála. STV1 je n čísle 1. Taktiež môžeš použiť číslo relácie z archívu (posledná časť adresy)
  - r volí, že sa má adresa presmerovať kódom 303. Ináč sa adresa na playlist len vypíše (oba spôsoby by mali fungovať vo VLC)
  - b volí, že sa má stream načítať vo videojs-contrib-hls prehrávači priamo v browseri. ``` rtvs2vlc.php?c=1&b=true ``` Nezlučiteľné s argumentom r !!!
  - q volí kvalitu. ``` rtvs2vlc.php?c=1&q=auto ``` je defaultná hodnota, ktorá zobrazí adresu na pôvodný m3u8 playlist. Môžete však špecifikovať ```1080```, ```720```, ```480``` alebo ```360```. VLC s tým dokáže pracovať automaticky, avšak spolu s argumentom b sa oplatí špecifikovať kvalitu explicitne.
  - e je experimentálny režim. ``` rtvs2vlc.php?c=1&q=1080&e=true ``` V zásade prejde všetky úrovne playlistov a z posledného, pozostávajúceho priamo z .ts chunkov vybuduje vlastný playlist. V tomto režime MUSÍTE špecifikovať kvalitu explicitne. Režim som vymslel, pretože sa mi geoblocking na úrovni všetkých m3u8 playlistov javí ako ďalšia logická zmena, ktorú by mohli súdruhovia aplikovať.


### Poznámky

  - STV ŠPORT má aktuálne ID 15
  - Ak viete hľadať, príklad nájdete na https://dopi.ci
