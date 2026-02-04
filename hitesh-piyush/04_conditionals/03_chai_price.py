chai_size_input = input("What size of chai?(large/medium/small)(large/medium/small)(large/medium/small)(large/medium/small)(large/medium/small)(large/medium/small)(large/medium/small)(large/medium/small)(large/medium/small) :" )

def chai_size_price(chai_size_input):
    chai_size_input = chai_size_input.lower()
    if(chai_size_input == "small"):
        return 10
    elif(chai_size_input == "medium"):
        return 15
    elif(chai_size_input == "large"):
        return 20
    else:
        return None

chai_size_response = chai_size_price(chai_size_input)
print(f"Price: {chai_size_response}")
