import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
import pandas
akcie = pandas.read_csv('twlo.csv')
print(akcie.shape)
print(akcie.tail(n=1))
print(akcie.head())
print(akcie.iloc[:5])