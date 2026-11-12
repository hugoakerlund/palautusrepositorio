import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from tuote import Tuote
from viitegeneraattori import Viitegeneraattori

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        self.varasto_mock = Mock()
        saldot = {1: 10, 2: 1}
        tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "Fink Bräu I", 1),
        }
        self.varasto_mock.saldo.side_effect = saldot.get
        self.varasto_mock.hae_tuote.side_effect = tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_ostettaessa_kaksi_eri_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 6)


    def test_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_ostettaessa_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 10)


    def test_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_ostettaessa_kaksi_tuotetta_joista_toinen_on_loppu(self):
        self.varasto_mock.saldo.side_effect = lambda tuote_id: 0 if tuote_id == 2 else 10
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)

    def test_metodi_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        expected = [
            unittest.mock.call("pekka", ANY, "12345", ANY, 15),
            unittest.mock.call("pekka", ANY, "12345", ANY, 5)
            ]

        self.assertEqual(self.pankki_mock.tilisiirto.call_args_list, expected)


    def test_jokaiselle_maksutapahtumalle_pyydetaan_uusi_viitenumero(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)

    def test_tuotteen_poistaminen_korista_palauttaa_sen_varastoon(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.assertEqual(self.varasto_mock.ota_varastosta.call_count, 1)

        self.kauppa.poista_korista(1)
        self.assertEqual(self.varasto_mock.palauta_varastoon.call_count, 1)
