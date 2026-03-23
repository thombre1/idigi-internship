from multiprocessing import Process, Value
import time
def some_func(counter):
    for _ in range(10**5):
        # Gets a Lock on the variable
        with counter.get_lock():
            # Multiple Process can access the value at the same time
            # Else a New Copy will be passed to each process
            # This is like a pointer
            counter.value += 1

if __name__ == "__main__":
    # i is the
    counter = Value('i', 0)
    start = time.time()
    Processes = [Process(target=some_func, args=(counter, )) for _ in range(2)]
    [p.start() for p in Processes]
    [p.join() for p in Processes]
    end = time.time()
    print(f"Value: {counter.value} Time taken: {end-start:.2f}")
