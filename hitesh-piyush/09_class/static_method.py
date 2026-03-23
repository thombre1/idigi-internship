# Static Methods dont require any object creation

class ChaiStall:

    #create static method with decorator
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]


raw_text = "Milk, Ginger     , Elaichi,parle-g, Tea Leaves "

print(ChaiStall.clean_ingredients(raw_text))
