# Terveyspäiväkirja

Sovellus Herokussa:
https://terveyspaivakirja.herokuapp.com/

<br>


## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on tallentaa terveyteen liittyviä tietoja, kuten urheiluun, ruokailuun ja uneen liittyviä tietoja. Sovelluksella voi myös tehdä treeniohjelmia ja tallentaa reseptejä ruokasuunnittelua varten.

<br>

Tärkeimmät ominaisuudet käyttäjän kannalta:
- Käyttäjä voi tallentaa tietoa treeneistä, unesta ja ruokavaliosta
- Käyttäjä voi hakea treenejä tai ruokia avainsanoilla
- Käyttäjä voi tallentaa treeniohjelmia ja reseptejä
- Käyttäjä voi tarkastella toisten käyttäjien julkiseksi asettamia tietoja

<br>


## Tämänhetkinen tilanne

### Sovelluksessa toteutettu

- Käyttäjä voi luoda profiilin, muokata tietojaan, vaihtaa salasanan ja poistaa profiilin.
- Käyttäjä voi luoda harjoituksia, joista tallennetaan nimi, ajankohta, kategoria ja lisätiedot sekä valitaan liikkeet valmiilta listalta
- Käyttäjä voi luoda valmiita treeniohjelmia, joista tallennetaan nimi, kategoria, ohjeet ja siihen sisältyvät liikkeet.
- Käyttäjä voi luoda harjoituksen automaattisesti olemassa olevan treeniohjelman pohjalta.
- Käyttäjä voi muokata ja poistaa harjoituksiaan ja treeniohjelmiaan.
- Käyttäjä voi hakea treeniohjelmia ja harjoituksia hakusanalla niistä talletetun kategorian perusteella.
- Käyttäjä voi lisätä tietokantaan uusia liikkeitä, joista tallennetaan nimi, kategoria ja ohjeet, mutta käyttäjä ei voi poistaa eikä muokata olemassa olevia liikkeitä.

<br>

### Puutteet
- Sovellus toimii Herokussa vaihtelevasti, enkä löydä ongelmaan ratkaisua.

<br>


## Arkkitehtuuri

### Tietokantataulut

Sovellus tallentaa tällä hetkellä tietoa seuraaviin tietokantatauluihin:
- **Käyttäjät** (nimi, käyttäjänimi, salasana, syntymäaika, paino, pituus)
- **Harjoitukset** (nimi, kategoria, ajankohta, kuvaus, käyttäjä)
- **Treeniohjelmat** (nimi, kategoria, ohjeet, käyttäjä)
- **Liikkeet** (nimi, kategoria, ohjeet)

<br>

Muita ajateltuja tietokantatauluja:
- **Ruoka-aineet** (nimi, kategoria, kalorit, hivenaineet)
- **Reseptit** (nimi, ruoka-aine, määrä, avainsanat)
- **Ateriat** (käyttäjä, kategoria, resepti, määrä, kellonaika, päivämäärä)
- **Päivälogit** (ateriat, treenit, uni)

<br>

### Sovelluksen rakenne

Kolmikerroksinen rakenne:
- Web-käyttöliittymä
- Sovelluslogiikka
- Tietokantojen käsittely

<br>


## Työaikakirjanpito

[Työaikakirjanpito](https://github.com/juliapalorinne/terveyspaivakirja/blob/master/tyoaikakirjanpito.md)

<br>
