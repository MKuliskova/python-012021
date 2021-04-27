from django.db import models

class Auto(models.Model):
  registracni_znacka = models.CharField(max_length=20)
  znacka = models.CharField(max_length=100)
  kilometry = models.IntegerField()
  datum_kontrola = models.DateField()

class Zakaznik(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  cislo_ridicak = models.CharField(max_length=100)
  datum_narozeni = models.DateField()

class Vypujcka(models.Model):
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  cena = models.IntegerField()


