class Czlowiek:
    def __init__(self, imie, wiek):
        self.imie = imie #self.imie to nie to samo co imie
        self.wiek = wiek

    def przedstawSie(self, powitanie = "Cześć"):
        return powitanie + " nazywam się " + self.imie + " mam " + self.wiek + " lat."


obiekt = Czlowiek("Albert", "5")
print(obiekt.imie)
print(obiekt.przedstawSie("Siema"))
obiekt2 = Czlowiek("Baltazar", "23")
print(obiekt2.przedstawSie("Witam"))
