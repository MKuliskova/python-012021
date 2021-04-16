#import wget
#wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/nacteni-dat/excs/nabidky/assets/DataAnalyst.csv")
import pandas
jobs = pandas.read_csv('DataAnalyst.csv')
print(jobs.columns)
jobs.info()
print(jobs.shape[0]) #pocet radku
print(jobs.iloc[9])
print(jobs.iloc[12:20,1])