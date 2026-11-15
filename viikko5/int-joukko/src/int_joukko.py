KAPASITEETTI = 5
OLETUSKASVATUS = 5

def luo_listat(a, b):
    return (a.to_int_list(), b.to_int_list())

class IntJoukko:

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self._aseta_kapasiteetti(kapasiteetti)
        self._aseta_kasvastuskoko(kasvatuskoko)
        self.taulukko = self._luo_taulukko(self.kapasiteetti)
        self.alkioiden_lkm = 0


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
        on = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.taulukko[i]:
                on = on + 1

        if on > 0:
            return True
        else:
            return False

    def lisaa(self, n):
        ei_ole = 0

        if self.alkioiden_lkm == 0:
            self.taulukko[0] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True

        if not self.kuuluu(n):
            self.taulukko[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm % len(self.taulukko) == 0:
                taulukko_old = self.taulukko
                self.kopioi_lista(self.taulukko, taulukko_old)
                self.taulukko = self._luo_taulukko(self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_lista(taulukko_old, self.taulukko)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if n == self.taulukko[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.taulukko[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.taulukko[j]
                self.taulukko[j] = self.taulukko[j + 1]
                self.taulukko[j + 1] = apu

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_taulukko(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.taulukko[i]

        return taulu

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.taulukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.taulukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.taulukko[self.alkioiden_lkm - 1])
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

