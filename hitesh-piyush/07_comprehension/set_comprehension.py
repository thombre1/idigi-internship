recepies = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["Elaichi", "milk"],
    "Spicy Chai": ["ginger", "pepper", "clove"],
}

#this returns unique key values by default as we are storing it in set
unique_recepies = {recepie for recepie in recepies}

## SET COMPREHENSION
#this returns the unique elements in the values
unique_elements = {element for recepie in recepies.values() for element in recepie}

print(unique_recepies)
print(unique_elements)


## DICTIONARY COMPREHENSION
# {expression for iterator in iterable}

my_base_recepies = {recepie:ingredient[0] for recepie,ingredient in recepies.items() if ingredient[0].lower()=="ginger"}
print(f"My Base recepie: {my_base_recepies}")
