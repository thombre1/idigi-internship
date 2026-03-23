class ChaiStall:
    
    # note that type is a keyword in python
    # so we use 'type_'
    
    def __init__(self, type_, size):
        self.type_ = type_
        self.size = size
    
    def summary(self):
        return f"{self.size} for {self.type_}"



order = ChaiStall("ginger", 100)
#Notice the context here is 'chai' object
print(order.summary())
order_two = ChaiStall("masala", 200)
# here the context is 'chai_two' object
print(order_two.summary())


# Now lets talk inheritence

class InheritedStall(ChaiStall):

    def status(self):
        return f"Inheritence Status"

inherit1 = InheritedStall("Elaichi", 111)

print(f"{inherit1.status()} with chai: {inherit1.summary()}")
