from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request):
      #  return HttpResponse('Zde bude titulni stranka.')
      #  return HttpResponse("""""""<a href='http://localhost:8000/katalog/seznam/'>Seznam aut</a>""")
        return HttpResponse("""<h1>Vítejte v naší autopůjčovně!</h1>   
        <h2>Půjčte si auto ještě dnes!</h2>  
        <p>Jsme profesionální a spolehlivá autopůjčovna - půjčujeme malé vozy, vozy střední třídy, vozy vyšší třídy i luxusní vozy.<br>
        <h3>Právě teď akce na vybraná vozidla!</h3> 
        </p>Připravili jsme pro Vás velký výběr různých typů aut. Nabídku naleznete na odkazu níže:</p>
        <a href='http://localhost:8000/katalog/seznam/'>Zobrazit seznam aut</a><br>
        """)
class SeznamView(View):
    def get(self, request):
        return HttpResponse("Zde bude seznam aut.")

