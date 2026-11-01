# Kuinka hyödyllisiksi koit koodin täydennyksen ehdotukset?

Koodin täydennyksen ehdotukset olivat yleisesti ottaen ihan hyödyllisiä ja Copilot osasi generoida funktiota niiden nimien kuvausten perusteella.



# Pitikö Copilotin selitys Pylint-varoituksesta paikkansa?

Copilotin selitys Pylint-varoituksesta piti paikkansa.



# Tekikö agentti toimivan ratkaisun, ja testit?

Agentin luomat testit olivat toimivat. Ratkaisu oli pääosin toimiva, mutta siihen piti tehdä pieniä muutoksia. Agentin luoma ratkaisu ei hakenut pelaajien tiimejä aivan oikein.



# Eroaako testeissä joku siitä miten testejä tehtiin edellisellä viikolla?

Copilotin luomassa testitiedoston lopussa suoritetaan unittestin `main`-funktio:
```python
if __name__ == "__main__":
    unittest.main()
```

Lisäksi testeissä käytetään paljon seuraavaa rakennetta, jossa uusi lista luodaan funktion `assertEqual` sisällä:
```python
self.assertEqual(
    [player.name for player in result],
    ["Player Three", "Player Two", "Player One"],
)
```



# Löysikö Pylint agentin koodista virheitä?

Pylint ei löytänyt agentin koodista virheitä.



# Mitä muuta opit?

Agentin generoimaa koodia ei pidä hyväksyä sokeasti, koska vaikka se näyttää oikealta se voi sisältää vaikeasti havaittavia virheitä.
