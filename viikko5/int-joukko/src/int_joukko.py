OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self._aseta_kapasiteetti(kapasiteetti)
        self._aseta_kasvastuskoko(kasvatuskoko)
        self.taulukko = self._luo_taulukko(self.kapasiteetti)
        self.koko = 0


    def _aseta_kapasiteetti(self, kapasiteetti):
        if kapasiteetti is None:
            self.kapasiteetti = OLETUSKAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti


    def _aseta_kasvastuskoko(self, kasvatuskoko):
        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko


    def _luo_taulukko(self, koko):
        return [0] * koko


    def kuuluu(self, n):
        for i in range(self.koko):
            if n == self.taulukko[i]:
                return True
        return False


    def lisaa(self, n):
        if self.koko == 0:
            self._lisaa_alkuun(n)
            return True

        if not self.kuuluu(n):
            self._lisaa_loppuun(n)
            return True

        return False


    def _lisaa_alkuun(self, n):
        self.taulukko[0] = n
        self.koko = self.koko + 1


    def _lisaa_loppuun(self, n):
        self.taulukko[self.koko] = n
        self.koko = self.koko + 1

        # Ei mahdu enempää, luodaan suurempi taulukko
        if self.koko == len(self.taulukko):
            self._kasvata_taulukkoa()


    def _kasvata_taulukkoa(self):
        vanhat_alkiot = self.taulukko
        self.taulukko = self._luo_taulukko(self.koko + self.kasvatuskoko)
        self._kopioi_alkiot(vanhat_alkiot, self.taulukko)


    def lisaa_taulukko(self, taulukko):
        for i in range(len(taulukko)):
            self.lisaa(taulukko[i])


    def poista_taulukko(self, taulukko):
        for i in range(len(taulukko)):
            self.poista(taulukko[i])


    def poista(self, n):
        kohta = self._poista_alkio(n)

        if kohta != -1:
            self._siirra_oikealle(kohta)
            return True

        return False


    def _poista_alkio(self, n):
        for i in range(self.koko):
            if n == self.taulukko[i]:
                self.taulukko[i] = 0
                return i
        return -1


    def _siirra_oikealle(self, kohta):
        for i in range(kohta, self.koko - 1):
            self.taulukko[i], self.taulukko[i + 1] = self.taulukko[i + 1], self.taulukko[i]
        self.koko = self.koko - 1


    def _kopioi_alkiot(self, a, b):
        for i in range(len(a)):
            b[i] = a[i]


    def mahtavuus(self):
        return self.koko


    def __str__(self):
        uusi_lista = self.to_int_list()
        koko = len(uusi_lista)
        if koko == 0:
            return "{}"
        else:
            tulos = ", ".join(map(str, uusi_lista))
            return "{" + tulos + "}"


    def to_int_list(self):
        uusi_taulu = self._luo_taulukko(self.koko)

        for i in range(len(uusi_taulu)):
            uusi_taulu[i] = self.taulukko[i]

        return uusi_taulu


    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        a_taulu, b_taulu = luo_listat(a, b)
        tulos.lisaa_taulukko(a_taulu)
        tulos.lisaa_taulukko(b_taulu)
        return tulos


    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()
        a_taulu, b_taulu = luo_listat(a, b)

        for a in a_taulu:
            for b in b_taulu:
                if a == b:
                    tulos.lisaa(a)

        return tulos


    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        a_taulu, b_taulu = luo_listat(a, b)

        tulos.lisaa_taulukko(a_taulu)
        tulos.poista_taulukko(b_taulu)

        return tulos


def luo_listat(a, b):
    return (a.to_int_list(), b.to_int_list())
