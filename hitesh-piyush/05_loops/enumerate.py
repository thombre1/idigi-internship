myList = ["Summer", "Rainy", "Autumn", "Spring", "Winter"]

for index,item in enumerate(myList):
    print(f"{index},{item}")

# starting index can be changed with start
for index,item in enumerate(myList, start=2):
    print(f"{index}: {item}")
