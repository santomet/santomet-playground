Navrhoval by som sa zamerať na následujúce témy. Samozrejme je tu obrovský priestor pre doplnenie (najmä pri EZS budú určite existovať ľudia ktorí vedia viac)


## 1. Základy o ochrane plášťa budovy, priestorov a infraštruktúry:
   - Poukázať na potenciálne slabé články ktoré budeme rozoberať (Ľudský faktor, neriešené otvory v plášti, konštrukčné a stavebné chyby, zámky, prístupové systémy...)
   - Existujúce normy a ich úrovne (dvere, okná, rámy, senzory, CCTV....)
   - Prečo sa nespoliehať na normy (bezpečnosť sa nedá štandardizovať, je to hra na mačku a myš - ukázať napr. absurditu snahy NBÚ štandardizovať odolnosť voči bumpingu)
   - Prečo sa nespoliehať na integrátorov a zámočníkov a byť pri celom procese zabezpečovania (laxný prístup, nevzdelávanie sa a následná nekompetencia, zvyk nadradzovať funkčnosť a pohodlnosť nad bezpečnosťou)


## 2. Ľudský faktor (presahy s personálnou bezpečnosťou)
   - Na vrátniciach Vás aj tak väčšinou pustia s dobrým pretextom a niekedy Vám dajú aj kľúč
   - Zbieranie informácií: pohodené kľúče, nechránené RFID, možnosť odčítania zadávania kódu do EZS, odpadky..... ako sa to dá využiť sa naučíme neskôr
   - Red-teaming & Roleplaying (opravár výťahov, technik mobilného operátora (prístup na strechu), servisák, nový zamestnanec ktorému zabudli dať prístup, Spoof mails, calls & SMS...... Spear phishing skrátka funguje aj v skutočnom svete)
   - Ako bezpečné sú domácnosti zamestnancov a čo sa tam dá v ich neprítomnosti získať? - Zraniteľnosť, ktorú legálny red-teaming nemôže odhaliť. Dá sa tomu zabrániť bezp. politikou?
   - Blackmailing, pomsta bývalých zamestnancov atď, možno dať "Walling Out the Insiders" ako odporúčanú literatúru?

## 3. Nechránené otvory a stavebné/konštrukčné/mechanické chyby, zraniteľnosti v infraštruktúre
   - Hlavne v starších budovách bude niekde núdzový výlez/východ z krytu - často nechránený alebo chránený sub-par zámkom, otvor pre šachtu na uhlie, otvor pre odpadové konvy, prístupné balkóny a pod.
   - Útoky na dvere: under/over/side door, pánty z vonkajšej strany, nesprávny alebo nesprávne nasadený zapadací plech, otáčanie vnútornou olivou zvonku, zraniteľný jednoduchý jazýček (klasika ako šetrne otvoriť zabuchnuté dvere).....
   - Útoky na pootvorené ale aj úplne zatvorené okná a balkóny (oveľa jednoduchšie ako si myslíte, ukázať najlepšie nástroje...)
   - Hrubá sila (pripomenúť úrovne v normách)
   - Všade poukazovať na dostupnosť a primitívnosť nástrojov
   - Infraštruktúra: Ako sa dostať k holým kontaktom vrámci siete (špeciálne v starších budovách ktoré sa sieťovali neskôr), ako to využiť, poukázať na absenciu sond v takýchto interných sieťach. Energie a nebezpečenstvo sabotáže! Ako skutočne poriadne zabezpečiť infraštruktúru aj pred insidermi?

## 4. EZ&PS časť prvá: Prístupové systémy
   - Pokračovanie Request-To-Exit senzory a ako ich zneužiť 
   - All-in-one prístupové systémy ktorých "rozhodovacia" elektronika je prístupná zvonku (relé, spínače a tampering senzory + ako s tým pracovať)
   - "Klasické" centralizované prístupové systémy (určite ukázať môj NetAXS Sniffer z kolejí (v tomto repo)), prejsť protokoly od Wiegand až po OSDP (Prečo sa stále používa Wiegand?!)
   - RFID: EM,HID,MIFARE... slabiny & možnosti kopírovania (čínske "magic" karty a ich generácie a ochrana pred nimi, vysokovýkonné čítačky...) Ako urobiť systém správne (nespoliehať sa na UUID, využívať možnosti tých kariet naplno)
   - Biometria Možno pripomenúť iba očividné útoky ako získanie odtlačku priamo zo senzoru? (všetko podstatné vieme od prof Matyáša :))

## 5. EZ&PS časť druhá: Zabezpečovačky (senzory, alarmy..) + CCTV
   - Rôzne senzory narušenia (MW, PIR, kombinované, magnetické, akustické senzory rozbitia, IR brány...) ich slabiny a teoretické slabiny (ako ich netripnúť) (úrovne z noriem! Tie samotné napovedajú možné slabiny)
   - Ukázať budovu NÚKIB ako ukážkovú
   - Centrálne pulty, spôsoby pripojenia, aké sú možnosti prerušiť spojenie alebo získať PIN?? (IMSI Catchers, simulácia PSTN, odpojenie zdroja a náhradného zdroja)
   - CCTV - klasický blinding, nutkanie skoro všetkých výrobcov pridávať nezdokumentovaný backdoor interface na resetovanie hesla (ako vo firmware nájsť detaily), filmový hack od Eric Van Albert a Zack Banks (DefCon 23).

## 6. Zámky časť prvá: (Pozn.: V prípade nadviazania spolupráce s H&B by som niektoré časti z tejto prednášky vynechal)
   - Úvod - kde sa príliš spoliehame na zámky a prečo sa o zraniteľnostiach nehovorí
   - Zámočníctvo - ako funguje biznis, najväčší hráči a ako kľúčové služby svojimi požiadavkami na výrobcov vplývajú na znižovanie bezpečnosti
   - Kľúče, ich výroba a kde môže bežný smrteľník nájsť potrebné informácie o zámkových systémoch a kódovaniach
   - Ako zohnať polotovary kľúčov a ako si kľúč vyrobiť doma na kolene s pilníkom
   - Ako odčítať mechanický kód z fotografie, ako nájsť správny profil + dá sa to naučiť aj z pohľadu?
   - Ako si urobiť rýchlo silikónový negatív akéhokoľvek kľúča a následne ho kedykoľvek zduplikovať odlievaním kovu/epoxy. (lepšie ako vo filmoch)
   - Systémy generálneho kľúča a ich zraniteľnosti, špeciálne pri insideroch + spôsob akým to robí napr. GUARD
   - Key-To-Like systémy
   
## 7. Zámky časť druhá:
   - Rýchlo preletieť tvarové, dózické ale aj wafer zámky (otvorí ich každý)
   - "pin tumbler" mechanizmy - najpoužívanejšie - vysvetliť základný princíp a ukázať typy ("klasický", tubulárny, dimple...)
   - Ako sa zámky bránia (security pins, pasce...)
   - Lockpicking old-school: single-picking, raking, jiggling, bumping a do akej miery sú a môžu byť zámky odolné, čo je k tomu potrebné a ako sa dá trénovať,aký je potrebný talent?
   - PG & EPG ako low-skill útok aj na kvalitnejšie zámky + ako to nemecký Multipick dohnal do absurdnej dokonalosti ktorú zvládne skoro každý
   - Self-Impressioning (hlavne tubular a dimple zámky) - alebo ako kúsok alobalu prekoná zámok o ktorom si všetci myslia, že je bezpečnejší, rovnaký spôsob na Forever lock či Bowley...
   
## 8. Zámky časť tretia:
   - Diskové zámky ("otočné lamelové stavítka"), naznámejší zástupcovia a ich možné slabiny
   - Detto pre lever (u nás väčšinou nazývané trezorové zámky) + určite spomenúť legendány WE30C a Jamesa Clarka !!!
   - Špecializované nástroje pre tieto zámky - ako sa používajú, kde sa dajú zohnať, ako ich tajné služby vyvíjajú
   - Bonus: Autozámky a lockless odomykanie áut (aj tam môžu byť zaujímavé veci pre neskorší lateral movement)

## 9.... Praktické ukážky a cvičenia, ideálne v spolupráci s H&B, ale tí sa možno nebudú chcieť deliť o know-how. V takom prípade by bol super budget a aj nejaký priestor, nástroje a cvičné zariadenia (zámky, EZS...) vrámci FI.
