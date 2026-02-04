chai_order = dict(type="masala", quantity="full", price="Rs.10")
print(chai_order)

# How i think dictionary is - i imagined dictionary as json type syntaxed, lets check
my_chai = {
    "type":"Elaichi",
    "Quantity": "full",
    "price": "Rs.12"
        }
print(type(my_chai))
print(my_chai)
print(my_chai["Quantity"])

#del to delete a key value pair
del my_chai["price"]
print(my_chai)

#dictionary has methods related to it
print(my_chai.keys())
print(my_chai.values())
print(my_chai.items())
# Yep it Works, just like in json


# Now mostly a key may or may not be present and a safe way to check is to use the get("key_to_check", "response if key not there") method

print(f"{my_chai.get("customer_note","no Note")}")
print(f"{my_chai.get("type","no Note")}")

