# import wget
# wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas
temperature = pandas.read_csv("temperature.csv")

temperature_november = temperature[temperature["Day"] == 13]
print(temperature_november)
temperature_november = temperature_november[temperature_november["AvgTemperature"] != -99]
print(temperature_november)
print(temperature_november.groupby("Region")["AvgTemperature"].count())
print(temperature_november.groupby("Region")["AvgTemperature"].mean())
print(temperature_november.groupby("Region").agg({"AvgTemperature": ["max","min"]}))
