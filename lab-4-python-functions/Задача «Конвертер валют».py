def rub_to_usd(rub_amount, rate=100.0):
    usd = rub_amount / rate
    return usd

def rub_to_eur(rub_amount, rate=110.0):
    eur = rub_amount / rate
    return eur

rub = float(input("Сумма в руб: "))
print(f"Это {rub_to_usd(rub)} $ или {rub_to_eur(rub)} €")
