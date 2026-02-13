# Lets try to create a chai stall with user inputs and yield

def chai_order():
    print("Welcome to chai stall! May I take your order")
    order = yield
    while True:
        print(f"Preparing {order}")
        order = yield

# Give reference of the first Yield
online_user = chai_order()
# Print after the first stop
next(online_user)

#We are sending this to the variable which has yeild so its like reverse returning🤯
online_user.send("Ginger Chai")
# executes after the yeild inside in while loop and stops after the first yeild
# waiting for yeild to be triggered again
online_user.send("Elaichi Chai")
        
