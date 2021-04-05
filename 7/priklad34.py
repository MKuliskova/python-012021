import pandas
import matplotlib.pyplot as plt
temperature = pandas.read_csv("temperature.csv")
# temperature = temperature[temperature["City"].isin(["Helsinki","Miami Beach","Tokyo"])]
# temperature.plot(kind='box',whis = [0,100])
# plt.show()
Helsinki = temperature[temperature["City"] == "Helsinki"]
Helsinki = Helsinki["AvgTemperature"]
data = Helsinki.to_frame(name = "Helsinki")
data.reset_index(drop=True, inplace=True)

MiamiBeach = temperature[temperature["City"] == "Miami Beach"]
MiamiBeach = MiamiBeach["AvgTemperature"]
MiamiBeach.reset_index(drop=True, inplace=True)
data["MiamiBeach"] = MiamiBeach

Tokyo = temperature[temperature["City"] == "Tokyo"]
Tokyo = Tokyo["AvgTemperature"]
Tokyo.reset_index(drop=True, inplace=True)
data["Tokyo"] = Tokyo

print(data)
data.plot(kind='box', whis=[0, 100])
plt.show()
