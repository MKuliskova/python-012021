import pandas
temperature = pandas.read_csv("temperature.csv")
print(temperature[temperature["Day"] == 13])
US_temperature = temperature[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
print(US_temperature)
print(US_temperature[US_temperature["City"].isin(["Washington","Philadelphia"])])


