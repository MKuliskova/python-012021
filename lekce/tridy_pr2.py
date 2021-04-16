# Uvažuj, že navrhuješ software pro zásilkovou společnost.
# Vytvoř třídu Package, která bude mít tři atributy - address, weightInKilos a delivered.
# První dva atributy nastav pomocí parametrů funkce __init__. Parametr delivered nastav na začátku jako False.
# Připoj ke třídě funkci deliver, která změní hodnotu parametru delivered na True.
# Přidej funkci getInfo, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
# Zkus si vytvořit nějaké objekty ze třídy Package a ověř, že vše funguje.

class Package:
    def deliver(self):
        self.delivered = True   # tato fce zmeni delivered na True
    def getInfo(self):
        if self.delivered: #toto znamena, ze self.delivered je true, jinak by taky mohlo byt == True
            deliveredText = "Balik dorucen."
        else:
            deliveredText = "Balik nebyl dorucen."
        print(f"Adresa: {self.address}, hmotnost: {self.weightInKilos} kg, dorucen balik: {deliveredText}")
    def __init__(self, address, weightInKilos): #nedavam do zavorky delivered, protoze ho rovnou prirazuju na hodnotu
        self.address = address
        self.weightInKilos = weightInKilos
        self.delivered = False # je na zacatku jako false

balicek1 = Package("U Leskavy", "20")
balicek1.getInfo()
balicek1.deliver() #dokud nezavolam tuto fci tak balicek bude jako nedorucen
balicek1.getInfo()