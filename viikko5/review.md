# Mitä huomioita agentti teki koodistasi

Agentin ainoa huomio liittyi metodiin `won_point`. Metodissa pelaajan 2 nimeä ei ekspliittisesti tarkastettu ennen pisteiden lisäämistä. Pelaajan pisteitä kasvatettiin else-haarassa, jos annettu nimi ei vastannut pelaajan 1 nimeä.



# Olivatko ehdotetut muutokset hyviä

Mielestäni ehdotus oli hyvä, koska muuten tiedostossa `index.py` voisi vahingossa kasvattaa pelaajan 2 pisteitä antamalla nimen, joka ei vastaa kummankaan pelaajan nimeä.



# Kuinka hyödylliseksi koit agentin tekemän katselmoinnin

Agentin tekemä katselmointi oli hyödyllinen, koska se löysi hyvän parannusehdotuksen. Testeissä ei testattu väärän nimen antamista metodille.



# Huomasiko agentti jotain, minkä olisit itse jättänyt huomaamatta? Entä jäikö siltä jotain oleellista huomaamatta?

Arvelen, että olisin huomannut metodissa olevan virheen, jos olisin katselmoinut koodia tarkemmin. Mielestäni agentilta ei jäänyt mitään erityisen oleellista huomaamatta.



# Miltä agentin kommentit tuntuivat verrattuna siihen, että saman palautteen olisi antanut tiimikaveri? Mitä palautteen antamisessa kannattaa ottaa huomioon, kun katselmoijana on ihminen?

Jos saman palautteen olisi antanut tiimikaveri suhtautuisin palautteeseen vakavammin. Kun katselmoijana on ihminen, kannattaa palautetta antaessa olla kohtelias eikä hyökätä toista kohtaan. Kannattaa antaa palautetta myös hyvistä asioista. Jotkin asiat voivat olla vain makuasioita ja niistä ei välttämättä tarvitse huomauttaa. Parannusehdotukset kannattaa perustella hyvin, jotta niiden tarkoitus on selvä.
