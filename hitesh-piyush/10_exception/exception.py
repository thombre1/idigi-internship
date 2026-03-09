menu = {
        "Masala Chai":20,
        "Ginger Chai":12,
        "Elaichi Chai":15
        }

# What if user tries to acces a key that does not exist
# print(menu["Rose Chai"])
#We can try once but have multiple exception to catch, only one will be activated

def chai_exception(user_chai_input):
    try:
        print(menu[user_chai_input])
        if user_chai_input == "unknown":
            raise ValueError("Where the fuck I am...")

    except TypeError as TE:
        print(f"Error in Type: {TE}")

    except ValueError as VE:
        print(f"Error in Value: {VE}")

    except KeyError as KE:
        print(f"Error in Key: {KE}")

    else:
        print(f"{user_chai_input} Chai is being prepared")

    finally:
        print(f"Next Order...")


chai_exception("Ginger Chai")
chai_exception("unknown")
chai_exception({})
