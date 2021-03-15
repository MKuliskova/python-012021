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
    def get_celkova_delka(self):
        return self.delka
class Serial(Polozka):
    def __init__(self, nazev, zanr, epizodaPocet,epizodaDelka):
        super().__init__(nazev, zanr)
        self.epizodaPocet = epizodaPocet
        self.epizodaDelka = epizodaDelka
    def getInfo(self):
        return f"{super().getInfo()}, pocet epizod je: {self.epizodaPocet}, delka epizody je: {self.epizodaDelka} min"
    def get_celkova_delka(self):
        return self.epizodaPocet * self.epizodaDelka

film1 = Film("Harry Potter","fantasy",150)
serial1 = Serial("Pratele","komedie",120,20)
print(film1.getInfo())
print(serial1.getInfo())

class Uzivatel:
    def __init__(self,uzivatelske_jmeno):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = 0
    def pripocti_zhlednuti(self,zhlednuto):
        self.zhlednuto = zhlednuto
        self.delka_sledovani += self.zhlednuto
        return f"Uzivatel zhledl {self.zhlednuto} min."

Uzivatel1 = Uzivatel("Misa")
delkaFilmu = film1.get_celkova_delka()
delkaSerialu = serial1.get_celkova_delka()
print(Uzivatel1.pripocti_zhlednuti(delkaFilmu))
print(Uzivatel1.pripocti_zhlednuti(delkaSerialu))

