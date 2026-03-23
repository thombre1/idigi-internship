class Chai:
    pass

gingerChai = Chai()

# Check if the object is of type 'Chai' class
print(type(Chai))
print(type(gingerChai) is Chai)

# self Keyword is the context of the object from where the variables are supposed to be accessed from
# Class Context using object

class ChaiMaker:
    size = 120

    def describe(self):
        return f"My cap: {self.size}"

chai = ChaiMaker()

#here the context is the object 'chai' from class 'ChaiMaker'
print(chai.describe())
chai.size = 190
# syntax sugar for doing the same thing
print(ChaiMaker.describe(chai))

chai_two = ChaiMaker()
chai_two.size = 90
print(ChaiMaker.describe(chai_two))
