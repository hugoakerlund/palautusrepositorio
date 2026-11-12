# Repositorio-ohjeet

- Tämä repositorio on yksinkertainen ostoskori, johon voidaan listätä tuotteita ja poistaa niitä.
- Ostoskori ohjelmoidaan Test Driven Development -tekniikalla:
    1. Kirjoitetaan testiä sen verran että testi ei mene läpi. Ei siis luoda heti kaikkia luokan tai metodin testejä, vaan edetään yksi testi kerrallaan.
    2. Kirjoitetaan koodia sen verran, että testi saadaan menemään läpi. Ei yritetäkään heti kirjoittaa “lopullista” koodia.
    3. Jos huomataan koodin rakenteen menneen huonoksi (eli havaitaan koodissa esimerkiksi toisteisuutta tai liian pitkiä metodeja) refaktoroidaan koodin rakenne paremmaksi, ja huolehditaan koko ajan, että testit menevät edelleen läpi. Refaktoroinnilla tarkoitetaan koodin sisäisen rakenteen muuttamista siten, että sen rajapinta ja toiminnallisuus säilyy muuttumattomana.
    Jatketaan askeleesta 1

- Älä muuta testikoodia, ellei sitä erikseen pyydetä.
- Testit suoritetaan komennolla `uv run pytest`.
- Tiedostoja `ostos.py` ja `tuote.py` ei saa muuttaa.
