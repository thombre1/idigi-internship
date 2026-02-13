# params can be specified to be as multiple arguments by just 
# having *args(stores in tuple) and **kwargs stores in Dictionary

def chai_special (*ingredients, **extras):
    print("Ingredients: ",ingredients)
    print("Extras: ",extras)

chai_special("cinnamon", "cardamom", Sweetner="Honey", Foam="yes")
