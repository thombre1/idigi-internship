import threading 
import time

count = 0
def cpu_heavy():
    global count
    for _ in range (10**8):
        count += 1

start = time.time()

n = 20
Threads = [threading.Thread(target=cpu_heavy) for _ in range (n)]
[t.start() for t in Threads]
[t.join() for t in Threads]

end = time.time()

print(f"For {n} threads, time required {end-start:.2f}")
