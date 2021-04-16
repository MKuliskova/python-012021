class Package:
    def __init__(self, address, weight):
        self.address = address
        self.weight = weight
        self.delivered = False

    def deliver(self):
        self.delivered = True

    def get_info(self):
        return f'Adresa: {self.address}, Vaha: {self.weight}, Stav doruceni: {self.delivered}'

class ValuablePackage(Package):
    def __init__(self, address, weight, value):
        super().__init__(address,weight)
        self.value = value

valuablePackage = ValuablePackage("Plzenska",3,100)
valuablePackage.get_info()
valuablePackage.deliver()
valuablePackage.get_info()