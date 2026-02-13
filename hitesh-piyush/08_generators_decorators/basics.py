def get_chai_gen():
    yield "This is Masala Chai"
    yield "This is Ginger Chai"
    yield "This is Elaichi Chai"

holder = get_chai_gen()
print(holder)

# So next() starts the work of generator and saves the state of the yield
print(next(holder))
print(next(holder))

# only have next() as much as the number of yield


# Now infinite generators - I related this to home feed of youtube having infinite scrolling

def infinite_chai():
    count = 1
    while True:
        yield f"Chai #{count}"
        count+=1

# users has reference to the generators
user1 = infinite_chai()
user2 = infinite_chai()

# lets say user1 gets 5 refill of chai
for _ in range(5):
    print(next(user1))

# user2 gets 4 refills
for _ in range(4):
    print(next(user2))

