import multiprocessing
import time

count = 0

def cpu_heavy():
    global count
    for _ in range(10**8):
        count += 1

# Process always wants to be made inside main(as far as i know)
# To prevent fork bomb
# Thread dont require this as they are in same process


if __name__ == "__main__":
    n = 10 
    start = time.time()
    Processes = [multiprocessing.Process(target=cpu_heavy) for _ in range (n)]

    [p.start() for p in Processes]
    [p.join() for p in Processes]

    end = time.time()

    print(f"For {n} Processes, Time taken: {end-start:.2f}")
