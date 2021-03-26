# import wget
#
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")
import pandas
praha = pandas.read_csv("zam_praha.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
liberec = pandas.read_csv("zam_liberec.csv")
platy = pandas.read_csv("platy_2021_02.csv")

praha["mesto"] = "Praha"
plzen["mesto"] = "Plzen"
liberec["mesto"] = "Liberec"

zamestnanci = pandas.concat([praha,plzen,liberec],ignore_index=True)
print(zamestnanci)
print(platy)
zamestnanci_platy = pandas.merge(zamestnanci,platy)
print(zamestnanci_platy)
print(zamestnanci_platy.shape)
print(platy.shape)
print(zamestnanci.shape)
print(zamestnanci_platy.groupby("mesto")["plat"].mean())