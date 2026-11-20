def calculate_total(cart, discount_limit = 10):
    total = 0
    with_sale = 0

    for i in cart:
        mehsul_qiymet = cart[i][0] * cart[i][1]
        total += mehsul_qiymet
        print(f"{i}  {cart[i][0]} x {cart[i][1]} = {mehsul_qiymet}")
        

    if total >= discount_limit:
        with_sale = total * 0.9

    else:
        with_sale = total

    return total, round(with_sale, 2)


cart = {"alma": (1.5, 6), "çörək": (0.8, 2), "süd": (2.2, 1)}
#cart = {"su": (0.5, 4)}

total, with_sale = calculate_total(cart)

print(f"Cemi: {total} AZN")
print(f"Endirimli: {with_sale:.2f} AZN")
