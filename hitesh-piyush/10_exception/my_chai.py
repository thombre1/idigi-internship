class InvalidChaiError(Exception):
    pass

menu = {
    "Masala Chai": 20,
    "Ginger Chai": 10
}

def bill_machine(flavour, cups):
    try:
        if flavour not in menu:
            raise InvalidChaiError("Chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Cups Invalid Type")
        print(f"{flavour} with {cups} cups ready...")

    except Exception as e:
        print(f"Error: {e}")

bill_machine("mint",2)
bill_machine("Ginger Chai","two")
bill_machine("Ginger Chai",2)
