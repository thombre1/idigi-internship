import threading
import time


#One after the other
def take_orders():
    for i in range(1,4):
        print(f"Taking order #{i}")
        time.sleep(2)

def brew_orders():
    for i in range(1,4):
        print(f"Brewing order #{i}")
        time.sleep(4)

#Create Threads
order_thread = threading.Thread(target=take_orders)
brewing_thread = threading.Thread(target=brew_orders)

#Start Threads
order_thread.start()
brewing_thread.start()

#order_thread.start()
brewing_thread.join()
order_thread.join()


