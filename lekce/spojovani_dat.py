import pandas

u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()

maturita = pandas.concat([u202,u203,u302])
print(maturita) #kazdy soubor si uchoval svuj index, svoje cisla radku
print(maturita.loc[1]) #jsou tam tri radky ktere maji index 1

maturita = pandas.concat([u202,u203,u302],ignore_index=True) #vyrobi index automaticky, ale ztracime info o tom, v jake mistnosti kdo maturoval
print(maturita)
#proto pridame sloupec mistnost, predtim nez tabulky spojime:
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202,u203,u302],ignore_index=True)
print(maturita)
maturita.to_csv("maturita.csv", index = False) #ukladam do pocitace jako csv