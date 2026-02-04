myList = ["salt","onion","ors","water","lemon"]
myList.append("watch")
print(myList)
myList.remove("onion")
print(myList)

myShortList = ["ginger","milk","tea"]
print(myList)

myShortList.insert(2,"elaichi")
print(myShortList)


#membership - check {"element" in "array"} => returns Boolean
print(f"Is Ginger in my list: {"ginger" in myList}")
print(f"Is Water in my list: {"water" in myList}")


# ByteArray - network communication me use hoga i guess
raw_data = bytearray(b"Ginger")
print(f"RawData: {raw_data} ID: {id(raw_data)}")

#replaces but did not write backs
raw_data.replace(b"Gin",b"Trig")
print(f"RawData: {raw_data} ID: {id(raw_data)}")

#replaces and writes back but now id is different...
raw_data = raw_data.replace(b"Gin",b"Trig")
print(f"RawData: {raw_data} ID: {id(raw_data)}")


