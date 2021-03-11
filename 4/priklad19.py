from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovana_mena = input("Zadej pozadovanou menu: ").upper()
pozadovano_v_cilove_mene = int(input("Zadej pozadovane mnozstvi: "))
cena_v_korunach = prevodnik.convert(pozadovana_mena, 'CZK', pozadovano_v_cilove_mene)
print (f"Potrebujes {cena_v_korunach} CZK.")
