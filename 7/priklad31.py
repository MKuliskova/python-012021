#import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

import pandas
temperature = pandas.read_csv("temperature.csv")

temperature_november = temperature[temperature["Day"] == 13]
temperature_november = temperature_november[temperature_november["AvgTemperature"] != -99]
temperature_november = temperature_november.sort_values("AvgTemperature",ascending=False)
#print(temperature_november)
print(temperature_november.head())
print(temperature_november.tail())