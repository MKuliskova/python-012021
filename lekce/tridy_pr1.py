#Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů.
# Vytvoř tedy třídu Book, která reprezentuje knihu.
# Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

#Přidej knize funkci getInfo, která vypíše informace o knize v nějakém pěkném formátu.
#Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou.
# Přidej funkci discount, která bude mít jeden parametr - velikost slevy v procentech.
# Funkce sníží cenu knihy o dané procento.

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
    def getInfo(self):
        return f"Nazev knihy je {self.title}, ma {self.pages} stran, stoji {self.price} Kc."
    def getDiscount(self, discount):
        self.price = self.price * (1-discount/100)
        return f"Cena po sleve je {self.price} Kc."
ahoj = Book("ahoj",100,500)
print(ahoj.getInfo())
print(ahoj.getDiscount(50))