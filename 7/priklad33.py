#import wget

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

import pandas
import matplotlib.pyplot as plt

velikonoce = pandas.read_csv("velikonoce.csv")
print(velikonoce)
Datum = velikonoce["Datum"]
Pocet = velikonoce["Počet"]
plt.bar(Datum,Pocet)
plt.xlabel("Datum")
plt.ylabel("Pocet")
plt.title("Kolikrat pripadaly Velikonoce na dany datum")
plt.show()