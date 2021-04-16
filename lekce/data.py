#moduly musime stahnout
#jdu do file-setting-python interpreter a pres plus vlevo dole muzu instalovat
#instalovali jsme pandas a wget
#modul=knihovna
#velky modul = framework
##############import wget
##############wget.download("http://nove.kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/assets/nakupy.csv")
#soubor nemusime diky tomuto rucne stahovat
#wget je stahovatko souboru z netu, jakykoliv format umi stahnout, ne jen csv
#pandas pouzivam, kdyz chci zacit pracovat s daty, umi jakoukoliv manipulaci s daty
import pandas
nakupy = pandas.read_csv('nakupy.csv')
nakupy.info() #informace o datech
print(nakupy.shape) #radek x sloupce
print(nakupy.shape[0]) #pocet radku
print(nakupy.shape[1]) #pocet sloupcu
print(nakupy.columns) #vypise jaky sloupce jsou v datech
#INDEX
#kazdy radek ma prirazeny index
#iloc - index location - slouzi k tomu, abych si vybrala jeden konkretni nakup
print(nakupy.iloc[3]) #vypise ctvrty radek
print(nakupy.iloc[0:3]) #zobrazi prvni ctyri radky
print(nakupy.iloc[8:]) #vypise od 8. nakupu az do konce
pozdrav = "Ahoj Andreo"
print(pozdrav[-6:])
print(pozdrav[-6:-3])
#print(pozdrav.strip()) odstrani mezery na zacatku a konci stringu kdyby bylo napr " Ahoj "
print(nakupy.head(n=3)) #vypise prvni tri zaznamy, kdyz napiseme head() tak vychozi hodnota je n=5, jinak vzdy musime definovat n
print(nakupy.tail(n=2)) #vypise posledni dva zaznamy
#vyber sloupce:
print(nakupy.iloc[:5,0]) #hodnoty ze sloupce Jmeno, ktere jsou na prvnich 5 radcich
print(nakupy.iloc[:5,[0,3]]) #chci prvni a ctvrty sloupec, musim dat 3 do seznamu