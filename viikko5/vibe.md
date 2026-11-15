# Päätyikö agentti toimivaan ja hyvään ratkaisuun

Agentin ratkaisu oli toimiva. Itse olisin toteuttanut sovelluksen hieman eri tavalla. Esimerkiksi funktiossa `create_app` agentti luo avaimen `SECRET_KEY` satunnaisesti, jos ympäristömuuttujaa `FLASK_SECRET_KEY` ei ole. Itse en olisi käyttänyt myöskään kirjastoa `functools` tai rekisteröinyt reittejä erikseen. Agentin luoma CSS-tyyli ei myöskään ollut aivan sellainen kuin halusin.


# Miten varmistit, että ratkaisu toimii?

Katselmoin koodia ja sen testejä. Suoritin testit ja tarkistin, että ne menivät läpi. Käytin sovellusta agentin luoman käyttöliittymän läpi ja varmistin, että se toimii halutulla tavalla. Varmistin, että CI meni läpi.



# Tekikö agentti testit, ja olivatko ne hyviä?

Agentti teki testit, jotka testaavat sen luomaa käyttöliittymää. Testikattavuus on hyvä ja testit ovat järkeviä, joten mielestäni agentti teki testauksen ihan hyvin.


# Oliko koodi selkeää

Koodin selkeys oli mielestäni ihan hyvä, koska ymmärsin sen toiminnan. Mielestäni itse olisin kuitenkin kirjoittanut selkeämpää koodia.



# Opitko jotain uutta agentin tekemää koodia lukiessasi

Kirjaston `functools` käyttäminen Flask-sovelluksessa ja kaikkien reittien rekisteröiminen omassa funktiossa oli minulle uutta. Yleensä reittien rekisteröimiseen käytetään `@route` -dekoraattoria. HTML:n `aria` atribuutit ja CSS:n `@media` -sääntö olivat minulle myös uusia.
