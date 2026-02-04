snack_input  = input("What snack would you like to order? : ")

def check_availability(snack_input):
    snack_input = snack_input.lower()
    if(snack_input == "cookies" or snack_input=="samosa"):
        print(f"✅{snack_input} is available. Order Processing...")
    else:
        print(f"⛔{snack_input} not available. Try again later...")

check_availability(snack_input)
    
