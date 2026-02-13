myList = ["one item", "two item", "three item", "four item"]
myIndex = [1,2,3,4,5]

#zip() helps us iterate over iterables parallely giving us tuples for each item

for item in zip(myList,myIndex):
    print(item)

# else we can have the values spearately in different variables

for element,index in zip(myList,myIndex):
    print(f"{element} has index {index}")


