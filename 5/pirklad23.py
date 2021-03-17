import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
import pandas
vaccinations = pandas.read_csv("country_vaccinations.csv")
#print(vaccinations.head())
vaccinations_March = vaccinations[vaccinations["date"] == "2021-03-10"]
print(vaccinations_March)
print(vaccinations_March[vaccinations_March["total_vaccinations"] > 1000000])
print(vaccinations_March[(vaccinations_March["daily_vaccinations"]>100000) | (vaccinations_March["daily_vaccinations"]<100)])
