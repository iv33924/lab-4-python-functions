def get_vat(price):
    vat_amount = price * 0.20
    return vat_amount

user_price = float(input("Введите цену товара: "))

tax = get_vat(user_price)

print(f"Налог составит: {tax} руб.")