sklad = {
    "1N4148": 250,
    "BAV21": 54,
    "KC147": 147,
    "2N7002": 97,
    "BC547C": 10
}
kod = str(input("Zadej kod soucastky: "))
mnozstvi = int(input("Zadej mnozstvi: "))
if kod in sklad:
    if mnozstvi > sklad[kod]:
        print(f"Soucastka je skladem, lze prodat maximalne {sklad[kod]} ks.")
        sklad.pop(kod)
    elif mnozstvi <= sklad[kod]:
        print("Soucastka je skladem v danem mnozstvi.")
        sklad[kod] -= mnozstvi
else:
    print("Soucastka neni skladem.")