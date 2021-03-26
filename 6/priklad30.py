# Ulož tabulku s cekovými počty vykázaných hodin, kterou jsi vytvořila v příkladu 27 jako Excel soubor.
# Pokud jsi tento příklad nezpracovala, ulož libovolnou jinou tabulku jako Excel sešit.
# Výsledný sešit si otevři a zkontroluj. K uložení použij funkci to_excel, se kterou pracuj stejně,
# jako jsme na lekci pracovali s funkci to_csv.
# Zkus data z Excelu naopak načíst pomocí funkci read_excel() a ověř, že se soubor načetl v pořádku.
import pandas
vykazy = pandas.read_csv("vykazy.csv")
vykazy_grouped = vykazy.groupby("project")["hours"].sum()
print(vykazy_grouped)
vykazy_grouped.to_excel("vykazy.xlsx")
vykazy = pandas.read_excel("vykazy.xlsx")
print(vykazy)
