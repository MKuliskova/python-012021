import wget
wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/studenti.csv")
import pandas
u202 = pandas.read_csv("u202.csv").dropna()
u203 = pandas.read_csv("u203.csv").dropna()
u302 = pandas.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
maturita = pandas.concat([u202,u203,u302],ignore_index=True)
studenti = pandas.read_csv("studenti.csv")
vysledky_se_jmeny = pandas.merge(maturita, studenti, how="left") #rikam ze chci left join
print(vysledky_se_jmeny)
print(vysledky_se_jmeny[vysledky_se_jmeny["jmeno"].isnull()]) #rekne mi, kde nemam vyplnene jmeno

vysledky_se_jmeny = pandas.merge(u202, studenti, how="left") #rikam ze chci left join
print(vysledky_se_jmeny)

#nahrava novy soubor predsedajici, ktery chce najoinovat pres den, pokud pycharmu nezadame primo pres co to chceme,
#tak to udela pres jmeno, protoze se nam tyto dva nzvy sloupcu shoduji v obou tabulkach
# import wget
# wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/agregace-a-spojovani/assets/predsedajici.csv")
# import pandas
#
# u202 = pandas.read_csv("u202.csv").dropna()
# u203 = pandas.read_csv("u203.csv").dropna()
# u302 = pandas.read_csv("u302.csv").dropna()
# u202["mistnost"] = "u202"
# u203["mistnost"] = "u203"
# u302["mistnost"] = "u302"
# maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# studenti = pandas.read_csv("studenti.csv")
#
# vysledky_se_jmeny = pandas.merge(u202, studenti, how="left")
# print(u202.shape)
# print(vysledky_se_jmeny.shape)
# import pandas
#
# u202 = pandas.read_csv("u202.csv").dropna()
# u203 = pandas.read_csv("u203.csv").dropna()
# u302 = pandas.read_csv("u302.csv").dropna()
# u202["mistnost"] = "u202"
# u203["mistnost"] = "u203"
# u302["mistnost"] = "u302"
# maturita = pandas.concat([u202, u203, u302], ignore_index=True)
# studenti = pandas.read_csv("studenti.csv")
# predsedajici = pandas.read_csv("predsedajici.csv")
#
# vysledky_se_jmeny = pandas.merge(u202, studenti, how="left")
# tady vyhodi tabulky najoinovane pres jmeno
# vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici)
# print(vysledky_se_jmeny_a_predsedajicimi.head())
#RESENI TAKTO
# predsedajici["den"] = predsedajici["den"].str.strip() ##timto opravim chybu a to je mezera v datu, oreze to mezery na konci a zacatku retezce
# vysledky_se_jmeny = pandas.merge(u202, studenti, how="left")
# vysledky_se_jmeny_a_predsedajicimi = pandas.merge(vysledky_se_jmeny, predsedajici, on="den") #pres on rikam pres co to ma propojit
# print(vysledky_se_jmeny_a_predsedajicimi)
