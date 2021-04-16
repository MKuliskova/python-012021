#toto jsem vytvorila
#potrebuju z djanga naimportovat fci path
from django.urls import path
from . import views
#rikam ze budu pracovat se souberem views ve stejnem adresari, to znamena .
#tecka rika ze pouzivame stejny adresar
urlpatterns = [
    path("", views.MujPrvniPohled.as_view(), name="index") #name index pouzivam, kdybych na strance chtela udelat navigacni panel, tak djangu pak muzu
    #rikat pouzij url nazvanou index
] #mam adresu ktera mi vede na muj prvni pohled