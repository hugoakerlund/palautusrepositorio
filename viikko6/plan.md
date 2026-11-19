# Miltä agentin ensimmäinen suunnitelma näytti, ja mitä siihen muutettiin?

Agentin ensimmäisen suunnitelman ensimmäinen askel kattoi parse -toiminnon, joka tunnisti yksittäiset ehdot kuten `team = XXX` ja `<attribuutti> >= luku`. Askeleessa ehdot oli tarkoitus rakentaa vastaaviksi `QueryBuilder` -kutsuiksi. Toisessa askeleessa ehdot oli tarkoitus laajentaa usean ehdon `and` -ketjuille. Kolmannessa askeleessa piti lisätä `or` -yhdistelmien käsittely, niin että `and` -ehdot käsitellään ensin. Neljännessä askeleessa suunnitelmana oli testata rajatapauksia kuten tyhjä kysely ja virheelliset operaattorit. Jokaisessa suunnitelman askeleessa oli tarkoitus testata toteutettua toimintoa.

Pyysin agenttia lisäämään `not` -operaation sekä tarkentamaan minkä poikkeuksen `parse` heittää virheellisestä kyselystä. Seuraavaksi pyysin agenttia vielä lisäämään sulkeiden tuen, jolloin esimerkiksi `not` -operaattori voi kohdistua useampaan ehtoon.



# Noudattiko agentti suunnitelmaa toteutusvaiheessa?

Agentti ikään kuin toteutti useamman askeleen yhdessä askeleessa. Jo ensimmäinen muokkauspyyntö tiedostoon `parse.py` sisälsi suurimman osan pyydetystä toiminnallisuudesta kuten `_Parser` -luokan, ehtojen jäsentämisen, `and`, `or` ja `not` -operaatioiden tuen sekä sulkeiden tuen. Loput muokkauspyynnöistä olivat lähinnä testien kirjoittamista. Muuten agentti noudatti suunnitelmaa.



# Oliko agentin tuottama koodi ymmärrettävää ja rakenteeltaan selkeää?

Mielestäni agentin tuottama koodi oli enimmäkseen ymmärrettävää ja sen rakenne on selkeä. Luokan `_Parser` koheesio on hyvä ja metodit ovat sopivan pieniä. Metodit ovat nimetty selkeästi, luokassa on käytetty kapselointia ja luokan käyttäminen tapahtuu selkeästi rajapinnan `parse` kautta.



# Opitko tehtävässä jotain uutta?

Agentin tuottaman `_Parser` -luokan tutkiminen oli jossain määrin opettavaista ja agentin selitys koodin toiminnasta oli hyvä. Erityisesti `_Parser` -luokan `_parse` -alkuiset metodit olivat opettavaisia, koska niiden toteutus näyttää miten toiset operaattorit sitovat vahvemmin kuin toiset.
