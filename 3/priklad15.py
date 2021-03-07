from datetime import datetime, timedelta
date = input("Datum: ")
persons = int(input("Pocet osob: "))
date = datetime.strptime(date, "%d.%m.%Y")
if date >= datetime(2021, 7, 1) and date <= datetime(2021, 8, 10):
    price = persons * 250
    print(f"Cena vstupenek je {price} Kc.")
elif date >= datetime(2021, 8, 11) and date <= datetime(2021, 8, 31):
    price = persons * 180
    print(f"Cena vstupenek je {price} Kc.")
else:
    print("V tuto dobu je kino zavrene.")
