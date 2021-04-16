#import wget

#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")

import pandas
staty = pandas.read_json("staty.json")
staty = staty.set_index("name") #nastaveni indexu

staty["population_density"] = staty["population"]/staty["area"] #vytvoreni kalkulovane sloupce
print(staty.head())
staty = staty.sort_values("population_density") #vychozi je vzestupne
print(staty.head())
staty = staty.sort_values("population_density",ascending=False) #zmena na sestupne
print(staty.head())