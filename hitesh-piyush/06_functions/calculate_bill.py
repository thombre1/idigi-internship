def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

aditya = calculate_bill(4,10)
paras = calculate_bill(1,12)
rohit = calculate_bill(3,15)

print(f"Aditya paid: {aditya}")
print(f"Paras paid: {paras}")
print(f"Rohit paid: {rohit}")

# ok now writing a function that adds tax too

def add_vat(price, vat_rate):
    return price+price*vat_rate

aditya = add_vat(aditya,0.1)
paras = add_vat(paras,0.1)
rohit = add_vat(rohit,0.1)

print(f"Aditya paid: {aditya}")
print(f"Paras paid: {paras}")
print(f"Rohit paid: {rohit}")
