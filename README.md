# Terveyspäiväkirja

Sovellus Herokussa:
https://terveyspaivakirja.herokuapp.com/


## Tämänhetkinen tilanne

En saa PostgreSQL-tietokantoja toimimaan koneellani enkä ole onnistunut kohtuullisessa ajassa löytämään ratkaisua ongelmaan. Sovellukseni ei siis toimi käytännössä enkä ole pystynyt juurikaan edistämään tilannetta edelliseen palautukseen verrattuna.


## Sovelluksen tarkoitus

Sovelluksen tarkoituksena on tallentaa terveyteen liittyviä tietoja, kuten urheiluun, ruokailuun ja uneen liittyviä tietoja. Sovelluksella voi myös tehdä treeniohjelmia ja tallentaa reseptejä ruokasuunnittelua varten.
<br><br/>
Tärkeimmät ominaisuudet käyttäjän kannalta:
- Käyttäjä voi tallentaa tietoa treeneistä, unesta ja ruokavaliosta
- Käyttäjä voi hakea treenejä tai ruokia avainsanoilla
- Käyttäjä voi tallentaa treeniohjelmia ja reseptejä
- Käyttäjä voi tarkastella toisten käyttäjien julkiseksi asettamia tietoja
<br><br/>

## Arkkitehtuuri

### Tietokantataulut

Sovellus tallentaa tietoa seuraaviin tietokantatauluihin:
- **Käyttäjät** (nimi, käyttäjänimi, salasana, ikä, paino, pituus, tavoitteet)
- **Harjoitukset** (nimi, kategoria, lihasryhmä, kuvaus)
- **Treeniohjelmat** (käyttäjä, nimi, lista harjoituksista ja määristä, kuvaus)
- **Treenit** (käyttäjä, lista harjoituksista ja määristä, kellonaika, päivämäärä, arvio)
- **Ruoka-aineet** (nimi, kategoria, kalorit, hivenaineet)
- **Reseptit** (nimi, ruoka-aine, määrä, avainsanat)
- **Ateriat** (käyttäjä, kategoria, resepti, määrä, kellonaika, päivämäärä)
- **Päivälogit** (ateriat, treenit, uni)
<br><br/>

### Sovelluksen rakenne

Kolmikerroksinen rakenne:
- Web-käyttöliittymä
- Sovelluslogiikka
- Tietokantojen käsittely
<br><br/>

## Työaikakirjanpito

[Työaikakirjanpito](https://github.com/juliapalorinne/terveyspaivakirja/blob/master/tyoaikakirjanpito.md)
<br><br/>
