from datetime import datetime, timedelta
#print(datetime.now())
#muzeme psat rovnou v konzoli, abychom videli rovnou vysledky, nemusime tam psat print
#python konzole slouzi k rychlemu zkouseni novych veci

#V proměnné apolloStart máme uložený datum a čas startu Apolla 11.
# Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané,
# tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. Čas vypisovat nemusíš.
apolloStart = datetime(1969, 7, 16, 14, 32)
print(apolloStart)
print(apolloStart.strftime(("%m/%d/%Y")))

#Satelit Solar Orbiter, který má za cíl pozorování Slunce,
#odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.
#Který den v týdnu Solar Orbiter odstartoval?
#Spočítej, kolik času od jeho startu uplynulo.

start = datetime(2020, 2, 10, 5, 3)
print(start)
