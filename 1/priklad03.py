volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = int(input("Zadej hodinu: "))
if hodina in volnePokoje:
    volneMistnosti = len(volnePokoje[hodina])
    print(f"Pocet volnych mistnosti: {volneMistnosti}")
else:
    print("V tuto hodinu nejsou volne zadne mistnosti.")
