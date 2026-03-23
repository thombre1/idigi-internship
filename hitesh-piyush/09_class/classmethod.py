# The classmethod is used, mostly to take arguments with any format and then pass on to the constructor
# Create Object -> Pass Args -> goes to one of the class method depending on format of input -> the classmethod makes the data according to the expectations of the constructor -> Pass the values to the constructor
class ChaiThela:

    # Initialize the 
    def __init__(self, type_, quantity, price):
        self.type_ = type_
        self.quantity = quantity
        self.price = price
    
    #every class method takes cls as arg

    #this classmethod handles dictionary inputs
    @classmethod
    def from_dictionary(cls, order_dict):
        return cls(
            order_dict["type_"],
            order_dict["quantity"],
            order_dict["price"]
                )

    # this classmethod handles string inputs
    @classmethod
    def from_string(cls, order_string):
        type_, quantity, price = order_string.split(",")
        return cls(type_, quantity, price)


cup = ChaiThela.from_dictionary({
    "type_": "Masala",
    "quantity": "200",
    "price": "20"
    })

cup2 = ChaiThela.from_string("Ginger, 100, 10")
print(cup.type_)
print(cup2.__dict__)


# This takes input as expected by the constructor directly without any classmethod
cup3 = ChaiThela("Elaichi","120","12")
