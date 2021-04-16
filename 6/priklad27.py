#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

import pandas
vykazy = pandas.read_csv("vykazy.csv")
print(vykazy)

vykazy_grouped = vykazy.groupby("project")["hours"].sum()
print(vykazy_grouped)


