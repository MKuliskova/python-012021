def greetUser(name):
  print(f"Ahoj {name}.")
greetUser("Jirko")

def sumTwoNumbers(a, b):
   return a+b #pomoci return vracim vysledek
result = sumTwoNumbers(5, 9)
print(result)

def getMark(points,bonus=0): #bonus je nepovinny parametr, pokud nic nezadam tak fce si bere to co je za =
  if points + bonus<= 60:
    mark = 5
  elif points + bonus<= 70:
    mark = 4
  elif points + bonus<= 80:
    mark = 3
  elif points + bonus<= 90:
    mark = 2
  else:
    mark = 1
  return mark
points = input("Pocet bodu: ")
points = int(points)
bonus = input("Pocet bonusovych bodu: ")
bonus = int(bonus)
mark = getMark(points, bonus)
if mark == 5:
  points = input("Počet bodů z opravného testu: ")
  points = int(points)
  mark = getMark(points)
print(f"Výsledná známka je {mark}.")
