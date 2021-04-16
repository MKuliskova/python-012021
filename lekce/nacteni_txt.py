#txt nacitam stejne jako csv
import matplotlib.pyplot as plt
import pandas
import wget
wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/hazeni-kostkami/assets/kostky.txt")
wget.download("https://kodim.cz/czechitas/progr2-python/python-pro-data-1/vizualizace/excs/call-centrum/assets/callcentrum.txt")

kostky = pandas.read_csv("kostky.txt", header=None)
print(kostky.head())
