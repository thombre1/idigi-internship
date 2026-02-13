# the walrus operator is used to store runtime calculated or input values in a single expression

flag= int(input("Enter flag Number: "))

if flag == 4:
    print(f"My flag is there: #{flag}")

# instead we do

if (flag := int(input("inputEnter Flag Number:"))) == 4:
    print("Success 4")


# can use walrus operator to take user input at runtime in one line and then check its availability or against a condition

flavours = ["masala", "ginger", "elaichi", "green", "haldi"]
print(f"Available Flavours: {flavours}")

flag = 1

while (flag):
    if (userInput := input("Enter your choice:")) in flavours:
        print(f"{userInput} tea coming right up!")
        flag = 0

    else:
        print("Invalid Choice! Try Again...")

