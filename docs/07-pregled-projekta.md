# 07 – Pregled prevzetega projekta NašBlok

## Namen in način pregleda

Pregledal sem dokumentacijo in izvorno kodo prevzetega projekta NašBlok ter aplikacijo lokalno zagnal na macOS. Za pregled sem uporabil dokumenta `docs/02-funkcionalnosti-in-obseg.md` in `docs/05-uporabniske-zgodbe.md`, arhitekturno dokumentacijo v `docs/adr/`, frontend in backend ter praktične preizkuse s testnimi računi. Lokalno okolje vključuje React/Vite frontend, FastAPI backend, PostgreSQL in Mailpit. Zaradi že zasedenega porta 5432 na računalniku je PostgreSQL lokalno izpostavljen na portu 5433. FastAPI je dostopen na `http://localhost:8000` (tudi `/docs`), frontend pa na `http://localhost:5173`.

Pri ocenah ločujem med **dejansko izvedenimi preizkusi**, **ugotovitvami iz kode** in **kriteriji, ki jih ni bilo mogoče preveriti**. Uspešno odprtje strani samo po sebi še ne pomeni, da je pripadajoča uporabniška zgodba implementirana.

## US-01: Ustvarjanje stavbe in stanovanj (MVP)

**Uporabniška vloga:** upravnik  
**Status:** Uspešno preizkušeno – osnovne funkcionalnosti delujejo.

### Izvedeni preizkusi

Aplikacijo sem lokalno zagnal in se prijavil s testnim računom upravnika. V razdelku **Stavba in stanovanja** sem izvedel naslednje preizkuse:

1. **Prikaz obstoječe stavbe:** Prikazala se je testna stavba **Prešernova 12** s seznamom **20 stanovanj**.
2. **Ustvarjanje stavbe:** Uspešno sem ustvaril novo stavbo z imenom in naslovom.
3. **Dodajanje stanovanja:** Novi stavbi sem uspešno dodal stanovanje z oznako **Stanovanje 1**.
4. **Preprečevanje podvojenih oznak:** Ob poskusu dodajanja še enega stanovanja z enako oznako je aplikacija prikazala napako in preprečila podvojitev.
5. **Urejanje in brisanje stanovanja:** Uspešno sem spremenil oznako stanovanja in izbrisal stanovanje, ki ni imelo povezanih podatkov.

### Ocena uporabniške zgodbe

Preizkušene funkcionalnosti delujejo in pokrivajo glavni potek uporabniške zgodbe US-01: upravnik lahko upravlja stavbe in stanovanja, aplikacija pa preprečuje podvojene oznake stanovanj.

**Še ni posebej preverjeno:** prepoved brisanja stanovanja, ki ima povezane stanovalce, glasove ali prijave okvar; ter omejitev, da lahko stavbo ureja samo upravnik, ki jo je ustvaril. Zato vseh kriterijev sprejemljivosti US-01 še ne morem potrditi.

**Sklep:** US-01 je za preizkušene scenarije uspešno implementirana. Za popolno potrditev zgodbe bi bilo treba izvesti še preverjanje pravic dostopa in brisanja povezanih stanovanj.

## US-02: Vabila v stavbo (MVP)

**Uporabniški vlogi:** upravnik in etažni lastnik  
**Status:** Delno implementirano – registracija z obstoječim vabilom deluje, ustvarjanje in upravljanje vabil pa ni implementirano.

### Izvedeni preizkusi

Aplikacijo sem preizkusil v lokalnem okolju s testnimi podatki, ustvarjenimi s skripto `backend/app/seed.py`.

1. **Registracija z veljavno kodo:** S testno kodo `LASTNIK-TEST` sem uspešno ustvaril nov uporabniški račun.
2. **Samodejna dodelitev podatkov:** Po registraciji sem bil prijavljen kot lastnik in povezan s stavbo **Prešernova 12** ter **Stanovanjem 10**.
3. **Enkratna uporaba kode:** Ponovna registracija z že uporabljeno kodo `LASTNIK-TEST` ni uspela. Aplikacija je prikazala sporočilo **»Vabilo ni veljavno.«**
4. **Neobstoječa koda:** Registracija z izmišljeno kodo `NEVELJAVNA-123` ni uspela. Aplikacija je prikazala sporočilo **»Vabilo ni veljavno.«**
5. **Možnost pošiljanja vabil:** Po prijavi kot upravnik sem pregledal navigacijo aplikacije. Možnosti za ustvarjanje oziroma pošiljanje vabil nisem našel. Pregled kode prav tako ni pokazal API endpointov za ustvarjanje ali upravljanje vabil.

### Ocena glede na kriterije sprejemljivosti

- **Vabilo lastniku z izbiro stanovanja in serviserju brez stanovanja:** Ni implementirano oziroma ni na voljo v uporabniškem vmesniku. Tega postopka ni bilo mogoče preizkusiti.
- **Vabilo najemniku, ki ga pošlje lastnik samo za svoje stanovanje:** Ni implementirano oziroma ni na voljo za preizkus.
- **Enkratna uporaba kode:** Uspešno preverjeno. Uporabljene in neobstoječe kode aplikacija zavrne.
- **Sedemdnevna veljavnost vabila:** Ni preverjena. Testni vabili iz `seed.py` imata nastavljeno veljavnost **30 dni**, kar odstopa od zahteve sedmih dni; pravila za samodejno ustvarjena vabila ni bilo mogoče preveriti.
- **Pregled stanja vabil (čaka, uporabljeno, poteklo) in preklic:** Funkcionalnosti ni bilo mogoče preizkusiti, ker ustrezen vmesnik in API za upravljanje vabil nista implementirana.

### Sklep

**US-02 je delno implementirana.** Registracija s predhodno ustvarjeno kodo deluje, prav tako dodelitev stavbe, stanovanja in vloge ter preprečevanje ponovne uporabe oziroma uporabe neobstoječe kode. Glavne zahteve glede **ustvarjanja, pošiljanja, pregledovanja in preklica vabil** niso izpolnjene. Zato uporabniška zgodba **ne zadošča vsem kriterijem sprejemljivosti za MVP**.

## US-03: Prijava okvare (MVP)

**Uporabniški vlogi:** etažni lastnik in najemnik  
**Status:** Ni implementirano – v uporabniškem vmesniku je prikazan samo naslov razdelka »Okvare«.

### Izvedeni preizkusi

Aplikacijo sem lokalno zagnal in se prijavil s testnim računom **najemnika** (`najemnik@nasblok.si`). V navigacijskem meniju sem odprl razdelek **Okvare**.

1. **Dostop do razdelka Okvare:** Razdelek se je odprl in prikazal naslov **»Okvare«**.
2. **Obrazec za prijavo okvare:** Na strani ni bilo obrazca ali gumba za prijavo nove okvare.
3. **Pregled prijav:** Na strani ni bilo seznama oddanih prijav ali njihovih statusov.

### Ocena glede na kriterije sprejemljivosti

- **Naslov, kategorija, nujnost in lokacija okvare:** Ni mogoče vnesti, ker obrazec ne obstaja.
- **Predpisane kategorije in stopnje nujnosti:** Ni mogoče izbrati ali preveriti.
- **Neobvezna fotografija (JPG/PNG, manj kot 5 MB):** Dodajanje in preverjanje fotografij ni na voljo.
- **Oddaja s statusom »prijavljeno« in prikaz upravniku:** Ni mogoče preizkusiti, ker oddaja prijave ni implementirana.
- **Seznam lastnih prijav z datumom in statusom:** Ni na voljo.

Pregled izvorne kode potrjuje, da datoteka `frontend/src/pages/Okvare.jsx` vsebuje le naslov strani, v pregledanem backendu pa ni API endpointov za prijavo okvar.

### Sklep

**US-03 ni implementirana.** Uspešno se odpre le osnovna stran razdelka »Okvare«, brez obrazca, oddajanja prijav ali pregleda prijavljenih okvar. Zato uporabniška zgodba **ne izpolnjuje kriterijev sprejemljivosti za MVP**.

## US-04: Potek reševanja okvare (MVP)

**Uporabniške vloge:** prijavitelj okvare, upravnik in serviser  
**Status:** Ni implementirano – postopek reševanja okvar ni na voljo.

### Ugotovitve pri pregledu

Pri preizkusu US-03 sem ugotovil, da razdelek **Okvare** prikazuje samo naslov »Okvare«. Ni obrazca za prijavo ali seznama okvar, zato tudi ni mogoče odpreti posamezne okvare in spremljati njenega reševanja. V pregledani kodi ni API endpointov, ki bi podpirali potek reševanja okvar. Posameznih prehodov statusov zato nisem mogel praktično preizkusiti.

### Ocena glede na kriterije sprejemljivosti

- **Prehodi med statusi (prijavljeno → dodeljeno → v delu → zaključeno → potrjeno):** Niso implementirani oziroma niso dostopni prek aplikacije.
- **Pravice za spremembo statusa:** Ni mogoče preveriti, ali posamezen korak lahko izvede samo odgovorna oseba, ker spreminjanje statusov ni na voljo.
- **Serviser vidi samo dodeljene okvare:** Ni na voljo funkcionalnosti pregleda dodeljenih okvar.
- **Obvezno poročilo serviserja ob zaključku:** Ni na voljo vnosa poročila o opravljenem delu.
- **Potrditev odprave ali vrnitev okvare v reševanje z obrazložitvijo:** Ni implementirana.
- **Nespremenljiva zgodovina statusov z osebo, datumom in uro:** Beleženja in prikaza zgodovine sprememb ni mogoče uporabljati ali preveriti.

### Sklep

**US-04 ni implementirana.** Aplikacija ne omogoča celotnega postopka reševanja okvare, od dodelitve serviserju do potrditve odprave in vpogleda v zgodovino sprememb. Ker osnovna prijava okvar še ni implementirana, funkcionalnosti US-04 ni mogoče praktično preizkusiti. Uporabniška zgodba **ne izpolnjuje kriterijev sprejemljivosti za MVP**.

## US-05: Glasovanje o sklepu (MVP)

**Uporabniški vlogi:** upravnik in etažni lastnik  
**Status:** Ni implementirano – v uporabniškem vmesniku je prikazan samo naslov razdelka »Glasovanja«.

### Izvedeni preizkusi

Aplikacijo sem lokalno zagnal in v navigacijskem meniju odprl razdelek **Glasovanja**.

1. **Dostop do razdelka Glasovanja:** Stran se je odprla, vendar je prikazovala samo naslov **»Glasovanja«**.
2. **Ustvarjanje glasovanja:** Na strani ni bilo obrazca ali gumba za ustvarjanje glasovanja.
3. **Pregled in oddaja glasov:** Na strani ni bilo seznama glasovanj ali možnosti oddaje glasu.

### Ocena glede na kriterije sprejemljivosti

- **Naslov, opis, rok in prag glasovanja:** Upravnik ne more ustvariti glasovanja ali izbrati praga (več kot polovica, več kot tri četrtine ali vsa stanovanja).
- **Rok najmanj en dan po odprtju:** Pravila ni mogoče preizkusiti, ker ustvarjanje glasovanj ni na voljo.
- **Glasujejo samo lastniki, najemniki pa glasovanj ne vidijo:** Pravice za dejansko glasovanje ni mogoče preizkusiti, saj glasovanj ni. Dostop do razdelka sam po sebi še ne potrjuje vseh omejitev vlog.
- **En glas na stanovanje (za, proti, vzdržan) brez naknadnih sprememb:** Oddaja glasov ni na voljo, zato omejitve ni mogoče preizkusiti.
- **Izračun potrebnih glasov glede na vsa stanovanja:** Izračuna ni mogoče preizkusiti. Pri 20 stanovanjih bi bilo za prag več kot polovice potrebnih 11 glasov »za«.

Pregled izvorne kode potrjuje, da datoteka `frontend/src/pages/Glasovanja.jsx` vsebuje samo naslov strani, backend pa nima API endpointov za ustvarjanje glasovanj in oddajanje glasov.

### Sklep

**US-05 ni implementirana.** Na voljo je samo osnovna stran razdelka »Glasovanja«, brez ustvarjanja glasovanj, oddajanja glasov ali izračuna rezultatov. Uporabniška zgodba zato **ne izpolnjuje kriterijev sprejemljivosti za MVP**.

## US-07: Obvestila stavbe (MVP)

**Uporabniška vloga:** upravnik  
**Status:** Ni implementirano – v uporabniškem vmesniku je prikazan samo naslov razdelka »Obvestila«.

### Izvedeni preizkusi

Aplikacijo sem lokalno zagnal in v navigacijskem meniju odprl razdelek **Obvestila**.

1. **Dostop do razdelka Obvestila:** Stran se je odprla, vendar je prikazovala samo naslov **»Obvestila«**.
2. **Objava obvestila:** Na strani ni bilo obrazca ali gumba za objavo novega obvestila.
3. **Pregled in branje obvestil:** Na strani ni bilo seznama obvestil ali možnosti za njihov pregled.

### Ocena glede na kriterije sprejemljivosti

- **Objava obvestila z obveznim naslovom (največ 100 znakov) in besedilom:** Ni mogoče izvesti, ker obrazec za objavo ne obstaja.
- **Takojšnja vidnost lastnikom in najemnikom, ne pa serviserjem:** Ni mogoče praktično preveriti, ker objavljanje obvestil ni na voljo.
- **Označevanje neprebranih obvestil in beleženje prvega branja z uporabnikom in časom:** Ni na voljo.
- **Pregled števila bralcev in njihovih imen za upravnika:** Ni na voljo.

Pregled izvorne kode potrjuje, da datoteka `frontend/src/pages/Obvestila.jsx` vsebuje samo naslov strani, backend pa nima API endpointov za objavljanje in spremljanje obvestil. Posameznih pravil vidnosti in evidence branja zato ni bilo mogoče preizkusiti.

### Sklep

**US-07 ni implementirana.** Odpre se samo osnovna stran »Obvestila«, brez objavljanja, pregledovanja in spremljanja prebranosti obvestil. Uporabniška zgodba zato **ne izpolnjuje kriterijev sprejemljivosti za MVP**.

## US-15: Avtentikacija in vloge (MVP)

**Uporabniške vloge:** vsi uporabniki  
**Status:** Glavni preverjeni scenariji delujejo; celotna varnost dostopa na ravni API-ja ni bila posebej preizkušena.

### Izvedeni preizkusi

1. **Registracija z veljavno kodo:** S kodo `LASTNIK-TEST` sem uspešno ustvaril račun. Aplikacija mi je samodejno dodelila ustrezno vlogo lastnika ter stavbo **Prešernova 12** in **Stanovanje 10**.
2. **Registracija z neveljavno oziroma že uporabljeno kodo:** Registracija z izmišljeno kodo `NEVELJAVNA-123` in ponovna uporaba kode `LASTNIK-TEST` sta bili zavrnjeni s sporočilom **»Vabilo ni veljavno.«**
3. **Prijava:** Uspešno sem se prijavil s pravilnim e-poštnim naslovom in geslom.
4. **Napačno geslo oziroma neobstoječ e-poštni naslov:** V obeh primerih je aplikacija zavrnila prijavo z enakim sporočilom **»Napačen e-poštni naslov ali geslo.«** Tako ne razkrije, kateri podatek je napačen.
5. **Prekratko geslo:** Pri registraciji z geslom `abc123` (6 znakov) je aplikacija preprečila nadaljevanje oziroma registracijo in opozorila na najmanjšo dovoljeno dolžino.
6. **Podvojen e-poštni naslov:** Registracija z že obstoječim naslovom `upravnik@nasblok.si` je bila zavrnjena.
7. **Omejitev dostopa glede na vlogo:** Prijavljen kot **najemnik** sem poskusil odpreti `/stavba`. Aplikacija je prikazala **»Ni dostopa. Ta del aplikacije ni na voljo za vašo vlogo.«**
8. **Dostop brez prijave:** Po odjavi je poskus odpiranja zaščitene strani `/stavba` povzročil preusmeritev na prijavno stran.

### Ocena glede na kriterije sprejemljivosti

- **Registracija samo z veljavnim vabilom in samodejna dodelitev vloge, stavbe ter stanovanja:** Uspešno preizkušeno na primeru lastnika.
- **Geslo z najmanj 8 znaki in enoličen e-poštni naslov:** Uspešno preizkušena zavrnitev 6-mestnega gesla in že uporabljenega e-poštnega naslova.
- **Enotno sporočilo pri napačnih prijavnih podatkih:** Uspešno preverjeno za napačno geslo in neobstoječ e-poštni naslov.
- **Dostop samo prijavljenim uporabnikom in omejitve po vlogah:** Na uporabniškem vmesniku uspešno preverjena preusmeritev neprijavljenega uporabnika ter zavrnitev najemnika pri dostopu do upravljanja stavbe. **Neposrednih nepooblaščenih API zahtev in vseh kombinacij uporabniških vlog nisem posebej testiral**, zato varnosti celotnega sistema ne morem dokončno potrditi samo na podlagi teh preizkusov.

### Sklep

**US-15 je za preizkušene scenarije uspešno implementirana.** Registracija, prijava, preverjanje gesla in e-pošte ter osnovno omejevanje dostopa delujejo pravilno. Za celovito potrditev vseh varnostnih kriterijev bi bilo treba preveriti tudi dostopne pravice neposredno na backend API-ju za vse vloge.

## Skupna ocena MVP in zaključek

| Uporabniška zgodba | Ocena |
|---|---|
| US-01 – Ustvarjanje stavbe in stanovanj | Preizkušene funkcionalnosti delujejo; nekaj kriterijev ostaja nepreverjenih. |
| US-02 – Vabila v stavbo | Delno implementirana; registracija z vabilom deluje, upravljanje vabil manjka. |
| US-03 – Prijava okvare | Ni implementirana; stran vsebuje samo naslov. |
| US-04 – Potek reševanja okvare | Ni implementirana; postopek reševanja in zgodovina sprememb nista na voljo. |
| US-05 – Glasovanje o sklepu | Ni implementirana; stran vsebuje samo naslov. |
| US-07 – Obvestila stavbe | Ni implementirana; stran vsebuje samo naslov. |
| US-15 – Avtentikacija in vloge | Preizkušeni scenariji delujejo; neposredni varnostni preizkusi API-ja niso bili opravljeni. |
