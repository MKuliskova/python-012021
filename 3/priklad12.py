#Třídě Auto přidej funkci pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr.
# Funkce zkontroluje, jestli je vozidlo aktuálně volné.
# Pokud je volné, vrátí text "Potvrzuji zapůjčení vozidla" a změní hodnotu atributu,
# který určuje, zda je vozidlo půjčené. Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".
#Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle
# (stačí registrační značka a značka a typ vozidla) jako řetězec.
#Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
# Uživatel může zadávat hodnoty Peugeot nebo Škoda.
# Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce get_info() a následně použij funkci pujc_auto.

#Dotaz na uživatele a výpis výsledků si v programu zkopíruj,
# abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát.

class Auto:
    def auto_pujceno(self):
        self.availibility = False
    def pujc_auto(self):
        if self.availibility:
            return "Potvrzuji zapujceni vozidla"
            self.availibility = False
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

#nefunguje mi zmena hodnoty na False