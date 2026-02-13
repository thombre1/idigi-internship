# global gives access of the file level variable
# nonlocal gives access to one function level up

chai_type = "Ginger"
def front_desk():
    chai_type = "Elaichi"

    def kitchen():
        nonlocal chai_type
        chai_type = "Irani"

    kitchen()
    
    print(f"NonLocal Chai: {chai_type}")
    def cafe():
        # global chai_type = "Masala" is invalid syntax
        global chai_type
        chai_type = "Masala"
        print(f"Global Chai Inside: {chai_type} {id(chai_type)}")
    cafe()

print(f"Global Chai Outside: {chai_type} {id(chai_type)}")

front_desk()
