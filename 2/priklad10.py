#Obchodníci v naší softwarové firmě používají jednoduchý systém,
# aby odhadli šanci na úspěch potenciální zakázky. Každé zakázce přiřadí body od 0 do 10 a platí:

# Pokud má zakázka méně než 5 bodů, šance na záskání je malá.
# Pokud má zakázka 6 až 8 bodů, šance na získání je střední.
# Pokud má zakázka více bodů, šance na získání je vysoká.
# Body přidělují podle následujících kritérií:

# Odvětví: Firma nejlépe prodává do automotive, o něco hůře do retailu.
# Pokud potenciální zákazník podniká v automotive, přičti 3 body, pokud v retailu, přičti 2 bod, jinak 0.
# Obrat: Firma nejlépe prodává zákazníkům se středním obratem.
# U malých většinou neuspěje, u velkých občas ano. Pokud má firma obrat menší než 10 mil. Euro, přičti 0.
# Pokud je mezi 10 a 1 000 mil. Euro, přičti 3 body, jinak 1 bod.
# Země: Firma je nejúspěšnější v Česku a na Slovensku (2 body), o něco méně v Německu a ve Francii (1 bod). Ostatním zemím dej 0.
# Konference: Firma loni pořádala odbornou konferenci pro zákazníky. Pokud se zákazník konference účastnil, přičti 1 bod, jinak 0.
# Newsletter: Firma též rozesílá newsletter o svém produktu. Pokud zákazník newsletter odebírá, přičti 1 bod.
# Napiš funkci, které bude mít 5 parametrů, které reprezentují zadaná kritéria.
# Poslední dvě kritéria zadej jako nepovinná s výchozí hodnotou False. Funkce vrátí šanci na získání zakázky jako řetězec.

def uspechZakazky(odvetvi, obrat, zeme, konference = False, newsletter = False):
    points = 0
    if odvetvi == "automotive" or odvetvi == "Automotive":
        points += 3
    elif odvetvi == "retail" or odvetvi == "Retail":
        points += 2
    else:
        points += 0
    if obrat < 10000000:
        points += 0
    elif obrat in range(10000000, 1000000001):
        points += 3
    else:
        points += 1
    if zeme in ('Cesko','Slovensko'):
        points += 2
    elif zeme in ('Nemecko', 'Francie'):
        points += 1
    else:
        points += 0
    if konference:
        points += 1
    else:
        points += 0
    if newsletter:
        points += 1
    else:
        points += 0
    if points < 5 :
        return "Nizka sance"
    elif points < 8:
        return "Stredni sance"
    else:
        return "Vysoka sance"

odvetvi = input("Zadej odvetvi: ")
obrat = int(input("Zadej obrat: "))
zeme = input("Zadej zemi: ")
konference = input("Byl zakaznik na konferenci?")
newsletter = input(("Odebira zakaznik newsletter?"))
if konference == "Ano" or konference == "ano":
    konference = True
else:
    konference = False
if newsletter == "Ano" or newsletter == "ano":
    newsletter = True
else:
    newsletter = False
print(uspechZakazky(odvetvi,obrat,zeme,konference,newsletter))


