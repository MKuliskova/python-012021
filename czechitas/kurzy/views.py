from django.shortcuts import render
from django.views import View
from django.http import HttpResponse #odpoved na nejaky nas pozdavek

class MujPrvniPohled(View):
    def get(self, request): #typ pozadavku na server, napr zadam adresu czechitas.cz chci se dostat na jejich web
        return HttpResponse("Vitej na webu czechitas")

#ted musime rict prohlizeci aby otevrel titulni stranku
# a ukazal ten muj pohled, to udelam pres url adresu
# ve slozce czechitas je soubor urls.py, coz bude seznam nasich urls





