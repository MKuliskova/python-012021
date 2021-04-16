sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
total = 0
for key, value in sales.items(): #knihu ulozi do promenne key, pocet do value, diky items python vi, ze me zajima cela dvojice,
    # pokud tam dam jen sales bez .items tak pise error too many values to unpack, python jinak totiz pracuje jen s klici, takze items mu rikam, ze chci i ty hodnoty
    print(f"Knihy {key} se prodalo {value} ks.")
    total += value
print(f"Celkem bylo prodano {total} kusu.")