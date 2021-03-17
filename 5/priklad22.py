import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
import pandas
postavy = pandas.read_csv("character-deaths.csv")
postavy = postavy.set_index("Name")
print(postavy.columns)
print(postavy.loc["Hali"])
print(postavy.loc["Gevin Harlaw":"Gillam"])
print(postavy.loc["Gevin Harlaw":"Gillam","Death Year"])
print(postavy.loc["Gevin Harlaw":"Gillam","GoT":"DwD"])
