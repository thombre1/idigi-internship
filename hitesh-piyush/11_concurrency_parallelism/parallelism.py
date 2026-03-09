from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start brewing #{name}")
    time.sleep(2)
    print(f"End brewing #{name}")

if __name__ == "__main__":
    
    # Make a List with elements as processes
    chai_maker = [
            Process(target=brew_chai, args=(f"{i} flavour",)) for i in range(3)
            ]

    # Run a Loop to start these processes parallely

    for p in chai_maker:
        p.start()
    for p in chai_maker:
        p.join()
