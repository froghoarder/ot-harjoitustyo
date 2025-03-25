class Maksukortti:
    def __init__(self, saldo):
        # saldo on senteissä
        self.saldo = saldo

    def lataa_rahaa(self, maara):
        self.saldo += maara

    def ota_rahaa(self, maara):
        if self.saldo < maara:
            return False

        self.saldo = self.saldo - maara
        return True

    def saldo_euroina(self):
        return self.saldo / 100

    def __str__(self):
        saldo_euroissa = round(self.saldo / 100, 2)

        return "Kortilla on rahaa {:0.2f} euroa".format(saldo_euroissa)
