baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
cisloBaliku = input("Zadej cislo baliku: ")
if baliky[cisloBaliku] == True:
   print("Balik byl predan kuryrovi.")
else:
    print("Balik nebyl predan kuryrovi.")