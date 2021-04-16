import pandas
import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/zakladni-dotazy/assets/staty.json")
staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

#print(staty["population"]) #zobrazim sloupec population
populace = staty["population"]
print(populace.sum()) #vrati vysledek jako int
#print(staty["population"] < 1000) #toto vyhodnoti jestli je podmminka splnena jako False/True
pidistaty = staty[staty["population"] < 1000] #musime dat do hranate zavorky a vnorit, pandas zobrazi jen to, kde je true
print(pidistaty[["area","population"]])

lidnate_evropske_staty = staty[((staty["population"] > 20_000_000) & (staty["region"] == "Europe"))] #v pandas se nepouziva and ale &
print(lidnate_evropske_staty)
vyznamne_staty = staty[(staty["population"] > 1_000_000_000) | staty["area"] > 3_000_000] #podminka or
print(vyznamne_staty)
zap_vych_evropa = staty[staty["subregion"].isin(["Western Europe","Eastern Europe"])] #pouziti seznamu v tabulce
print(zap_vych_evropa)

