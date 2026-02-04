train_type = input("What train type?(sleeper/General/AC/Luxury): ").lower()

match train_type:
    case "sleeper":
        print("Sleeper has bare bone requirements fulfilled, bed, fan and toilet.")
    case "general":
        print("Value for Money. Most people travel in this segment")
    
    case "ac":
        print("More comfortable than general")

    case "luxury":
        print("Best services will be provided")

    case _:
        print("Unknown train type. Try again later...")



