class Polozka:
    def __init__(self,nazev, zanr):
        self.nazev = nazev
        self.zanr = zanr
    def getInfo(self):
        return f"Nazev: {self.nazev}, zanr: {self.zanr} "
class Film(Polozka):
    def __init__(self,nazev, zanr, delka):
        super().__init__(nazev, zanr)
        self.delka = delka
    def getInfo(self):
        return f"{super().getInfo()}, delka filmu je: {self.delka} min"
class Serial(Polozka):
    def __init__(self, nazev, zanr, epizodaPocet,epizodaDelka):
        super().__init__(nazev, zanr)
        self.epizodaPocet = epizodaPocet
        self.epizodaDelka = epizodaDelka
    def getInfo(self):
        return f"{super().getInfo()}, pocet epizod je: {self.epizodaPocet}, delka epizody je: {self.epizodaDelka} min"

film1 = Film("Harry Potter","fantasy",150)
serial1 = Serial("Pratele","komedie",120,20)
print(film1.getInfo())
print(serial1.getInfo())

