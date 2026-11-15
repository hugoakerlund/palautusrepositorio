KAPASITEETTI = 5
OLETUSKASVATUS = 5

def luo_listat(a, b):
    return (a.to_int_list(), b.to_int_list())

class IntJoukko:

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self._aseta_kapasiteetti(kapasiteetti)
        self._aseta_kasvastuskoko(kasvatuskoko)
        self.taulukko = self._luo_taulukko(self.kapasiteetti)
        self.koko = 0


    def _aseta_kapasiteetti(self, kapasiteetti):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
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
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        taulu = self._luo_taulukko(self.koko)

        for i in range(0, len(taulu)):
            taulu[i] = self.taulukko[i]

        return taulu

    def __str__(self):
        if self.koko == 0:
            return "{}"
        elif self.koko == 1:
            return "{" + str(self.taulukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.koko - 1):
                tuotos = tuotos + str(self.taulukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.taulukko[self.koko - 1])
            tuotos = tuotos + "}"
            return tuotos


    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu, b_taulu = luo_listat(a, b)

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu, b_taulu = luo_listat(a, b)

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu, b_taulu = luo_listat(a, b)

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

