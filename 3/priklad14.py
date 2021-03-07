# Přidej třídě atribut salary (výše hrubého platu) a children (počet dětí), jehož výši nastavíš ve funkci __init__().
# Dále přidej funkci get_net_salary(), která vypočte a vrátí výši čisté mzdy.
# Uvažuj zjednodušený výpočet: sazba daně je 15 % a sleva na jedno dítě 1500 Kč.
# Vzorec pro výpočet daně tedy je: daň = hrubá mzda * 0.15 - počet dětí * 1500.
# Funkce vrátí výši čisté mzdy, tj. čistá mzda = hrubá mzda - daň.

class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def get_net_salary(self):
    self.tax = self.salary * 0.15 - self.children * 1500
    self. net_salary = self.salary -self.tax
    return f"Cista mzda je {self.net_salary} Kc."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children
Klara = Employee("Klara","ucetni",40000,2)
print(Klara.get_info())
print(Klara.get_net_salary())