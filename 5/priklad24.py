import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
temperature = pandas.read_csv("temperature.csv")
#print(temperature.head())
print(temperature[temperature["City"] == "Prague"])
print(temperature[temperature["AvgTemperature"]>80])
print(temperature[(temperature["AvgTemperature"]>60) & (temperature["Region"] == "Europe")])
print(temperature[(temperature["AvgTemperature"]>80) | (temperature["AvgTemperature"] < -20)])