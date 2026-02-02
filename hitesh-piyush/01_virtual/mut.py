sugar_amount = 2
print(f"Sugar Amount: {sugar_amount}")
sugar_amount = 10
print(f"New Sugar Amount: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 10: {id(10)}")

# ID's will be different showing that a new variable is created with different ID but with the same name


# set is mutable
spice = set()
print(f"Set ID: {id(spice)}")

spice.add("Ginger")
spice.add("Basil")
print(f"Set ID: {id(spice)}")


