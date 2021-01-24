# Arkkitehtuuri

## Tietokantataulut

Sovellus tallentaa tietoa seuraaviin tietokantatauluihin:
- **Käyttäjät** (nimi, käyttäjänimi, salasana, ikä, paino, pituus, tavoitteet)
- **Harjoitukset** (nimi, kategoria, lihasryhmä, kuvaus)
- **Treeniohjelmat** (käyttäjä, nimi, lista harjoituksista ja määristä, kuvaus)
- **Treenit** (käyttäjä, lista harjoituksista ja määristä, kellonaika, päivämäärä, arvio)
- **Ruoka-aineet** (nimi, kategoria, kalorit, hivenaineet)
- **Reseptit** (nimi, ruoka-aine, määrä, avainsanat)
- **Ateriat** (käyttäjä, kategoria, resepti, määrä, kellonaika, päivämäärä)
- **Päivälogit** (ateriat, treenit, uni)


## Sovelluksen rakenne

Kolmikerroksinen rakenne:
- Web-käyttöliittymä
- Sovelluslogiikka
- Tietokantojen käsittely