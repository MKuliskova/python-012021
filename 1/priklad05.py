prodeje2019 = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

prodeje2020 = {
    "Zkus mě chytit": 3157,
    "Vrah zavolá v deset": 3541,
    "Vražda podle knihy": 2510,
    "Past": 2364,
    "Zločinný steh": 5412,
    "Zkus mě chytit": 6671,
}

kniha = input("Nazev knihy: ")
if kniha in prodeje2019:
    prodej19 = prodeje2019[kniha]
else:
    prodej19 = 0
if kniha in prodeje2020:
    prodej20 = prodeje2020[kniha]
else:
    prodej20 = 0
prodejTotal = prodej19 + prodej20
print(f"Knihy {kniha} se celkove prodalo {prodejTotal} ks v letech 2019 a 2020.")
