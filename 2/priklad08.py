def numberVerification(number):
    if len(number) == 9 or len(number) == 13:
        return True
    else:
        return False

def messagePrice(message):
    oneMessagePrice = 3
    messageLen = len(message)
    messageCount = round(messageLen/180)
    if (messageLen % 180) != 0:
        messageCount += 1
    #print(f"Pocet znaku je {messageLen}.")
    return oneMessagePrice * messageCount

number = input("Zadej cislo: ")
numberVerification(number)
if numberVerification(number) == True:
    message = input("Napis zpravu: ")
    price = messagePrice(message)
    print(f"Cena SMS je {price} Kc.")
else:
    print("Spatny format cisla.")



