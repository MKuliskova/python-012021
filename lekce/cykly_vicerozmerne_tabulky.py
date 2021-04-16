books = [
  {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
  {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
  {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]
total = 0
for item in books: #nepisu .items protoze jsem uvnitr seznamu, ne ve slovniku, item je jeden radek
    if item["year"] == 2019:
        total += item["sold"] * item["price"]
print(f"Celkove trzby jsou {total}.")