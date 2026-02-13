# Dont write anything above the docstring else it(__doc__) wont work

def chai_flavour():
    """
    This is a docstring
    This is this functions description. 
    IDK at this point of time why we dont use the comments.
    """
    chai = "ginger"
    return chai

# After giving a doctstring description, we unlock dunder methods
# for the funtion

print(chai_flavour.__doc__)
print(chai_flavour.__name__)

