#This is our Custom Error make a class and then extend it with custom exception
class OutOfBounds(Exception):
    pass

def chai_kitchen(milk, sugar):
    if (milk==0 or sugar==0):
        raise OutOfBounds("Material Not Available")

chai_kitchen(0,2)
chai_kitchen(2,0)
    




