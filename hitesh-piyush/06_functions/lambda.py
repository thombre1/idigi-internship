# Impure function is just a function that modifies a global variable
# Lambda function is a one-line function which is mostly used in filters as far as i have observed

chai_types = ["Ginger", "Kadak", "Elaichi", "Rose", "Gulkand", "Masala"]

my_favourite = list(filter(lambda chai: chai != "Gulkand" and chai != "Rose", chai_types))

print(chai_types)
print(my_favourite)
