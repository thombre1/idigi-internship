from multiprocessing import Process
from time import time

def heavy_fun():
    print("Crunching some numbers...")
    
    total=0
    for i in range(10**8):
        total+=i

    print(f"Total: {total}")

start = time()
if __name__ == "__main__":
    Processes = [Process(target=heavy_fun) for _ in range(4)]
    [p.start() for p in Processes]
    [p.join() for p in Processes]

    print(f"Time Taken: {time()-start:.2f} secs")
