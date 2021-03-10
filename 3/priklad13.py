#Pokračuj ve své práci pro autopůjčovnu z příkladu 11 a příkladu 12.
#Přidej třídě Auto funkci vrat_auto(), která bude mít (krom obligátního self) 2 parametry,
# a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal.
# Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

#Dále ve funkci vypočti cenu za půjčení. Cena je 400 Kč na den,
# pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle.
# Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova return.

#Na konec programu (mimo třídu) přidej dotaz na uživatele,
# kolik kilometrů zákazník ujel a jak dlouo ho měl půjčené. Poté vypiš informaci o ceně.

class Auto:
    def vrat_auto(self,tachometer,daysRented):
        self.kilometres += tachometer
        self.daysRented = daysRented
        if self.daysRented < 7:
            self.price = self.daysRented * 400
        elif self.daysRented >= 7:
            self.price = self.daysRented * 300
        return f"Cena za pujceni je {self.price} Kc. Stav tachometru je {self.kilometres}."
    def auto_pujceno(self):
        self.availibility = False
    def pujc_auto(self):
        if self.availibility:
            return "Potvrzuji zapujceni vozidla"
        else:
            return "Vozidlo neni k dispozici"
    def getInfo(self):
        return f"Registracni znacka vozidla je {self.number} a typ vozidla je {self.type}."
    def __init__(self, number, type, kilometres,availibility = True):
        self.number = number
        self.type = type
        self.kilometres = kilometres
        self.availibility = availibility

Peugeot = Auto("4A2 3020","Peugeot 403 Cabrio",47534)
Skoda = Auto("1P3 4747","Škoda Octavia",41253)

car = input("Zadej auto, ktere si prejes pujcit: ")
if car == "Peugeot":
    print(Peugeot.getInfo())
    print(Peugeot.pujc_auto())
    Peugeot.auto_pujceno()
elif car == "Skoda":
    print(Skoda.getInfo())
    print(Skoda.pujc_auto())
    Skoda.auto_pujceno()
else:
    print("Toto auto nemame k dispozici.")

ujeteKilometry = int(input("Kolik zakaznik ujel kilometru? "))
dnyPujceni = int(input("Kolik dni bylo auto pujceno? "))
if car == "Peugeot":
    print(Peugeot.vrat_auto(ujeteKilometry,dnyPujceni))
elif car == "Skoda":
    print(Skoda.vrat_auto(ujeteKilometry,dnyPujceni))
else:
    print("Nezname auto.")