cart_total = int(input("Whats the cart total amount? (Nearest integer please)"))

if(cart_total <= 0):
    print("Enter a valid amount")

else:
    cart_total = (cart_total+30) if cart_total<300 else cart_total 
    print(f"Total fees with delivery charges: {cart_total}")
