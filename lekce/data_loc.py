import pandas
import wget
wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
staty = pandas.read_json("staty.json")
staty = staty.set_index("name") #pridani indexu, podle unikatniho klice
print(staty.head())
print(staty.loc["Czech Republic"]) #iloc vyhledava dle cisla, loc dle nazvu radku, na ktery mame navazany index, vypise info o CZ
print(staty.loc["Czech Republic":"Dominican Republic"]) #vypise vse od CZ po dominikanu
print(staty.loc[["Czech Republic","Slovakia"],"capital"]) #vypise hlavni mesto techto dvou statu
print(staty.loc[["Czech Republic","Slovakia"]])