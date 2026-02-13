def local_chai():
    yield "Ginger Chai"
    yield "Elaichi Chai"

def global_chai():
    yield "Macha Tea"
    yield "Oolong Tea"

def full_menu():
    yield from local_chai()
    yield from global_chai()

# I will need some time getting used to this syntax
for chai in full_menu():
    print(chai)



# Some try and Catch syntax
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai"
    except:
        print("Tea Stall Closed")

stall = chai_stall()
# So till the yield is called it will go to the try block
# When not called it will got to the except block
print(next(stall))
print(next(stall))


# Its always a good practice to close your generator
# so that it wont be misused or go to wrong hands
stall.close()
