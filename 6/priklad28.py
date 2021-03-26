# import wget
#
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

import pandas
staty = pandas.read_json("staty.json")
gdp = pandas.read_csv("gdp.csv")

staty_evropa = staty[staty["region"] == "Europe"]
print(staty_evropa)
print(staty_evropa.groupby("subregion")["name"].count())
print(staty_evropa.groupby("subregion")["population"].sum())