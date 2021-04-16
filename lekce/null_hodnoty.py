import pandas

u202 = pandas.read_csv("u202.csv")
u203 = pandas.read_csv("u203.csv")
u302 = pandas.read_csv("u302.csv")

print(u202)
print(u202["znamka"].isnull()) #vrati true pokud hodnota je null
print(u202[u202["znamka"].isnull()]) #piseme dotaz, vyhodi jen radky kde je null v datech


# dropna() - vrátí datový set očištěn od chybějících dat
# dropna(axis=1) \ - odstraní všechny sloupce, které obsahují chybějící data
# fillna(x) - nahradí všechna chybějící data a hodnoty hodnotou x

u202 = pandas.read_csv("u202.csv").dropna() #muzu pouzit hned pri nacteni, ze vyhodim N/A hodnoty
