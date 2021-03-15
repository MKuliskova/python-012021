from datetime import datetime, timedelta

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datetime.strptime(datum_pohovoru, "%d.%m.%Y")
        self.zapis_z_pohovoru = ""
    def uloz_zapis(self,text):
        if self.datum_pohovoru > datetime.now():
            print(f"Uchazec: {self.jmeno}. Pohovor probehne {self.datum_pohovoru}.")
        else:
            self.text = text
            print(f"Uchazec: {self.jmeno}, zapis ulozen.")
            print(f"Zapis: {self.text}")

uchazec1 = Uchazec("Jan Novy","j.novy@seznam.cz","18.05.2021")
uchazec1.uloz_zapis("text")
uchazec2 = Uchazec("Klara Mala","k.mala@seznam.cz","14.03.2021")
uchazec2.uloz_zapis("text")