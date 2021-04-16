class Employee: #vzdy velke pismeno pro nazev tridy
  def takeHoliday(self, days):
    if self.remainingHolidayDays >= days:
      self.remainingHolidayDays -= days
      return f"Užij si to."
    else:
      return f"Bohužel už máš nárok jen na {self.remainingHolidayDays} dní."
  def getInfo(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position): #konvence psat init uplne dolu nebo nahoru
    self.name = name
    self.position = position
    self.remainingHolidayDays = 25 #pisu primo atribut, protoze vsichni maji 25, hodnota se nemeni
    #atribut vzdy zacina self., ma zivotnost mimo fci, ostatni plati jen uvnitr fce

  def __str__(self): #tato fce zpusobi to, ze se objekt vypise pres print(frantisek)
    return self.name + ', ' + self.position
frantisek = Employee("Frantisek","prodavac")
print(frantisek)
print(frantisek.takeHoliday(80))
#__ fce se volaji automaticky, zbytek musime zavolat
# self odkazuje na atribut objektu