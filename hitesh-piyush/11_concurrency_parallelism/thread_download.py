import requests
import threading
import time


# With the lock, only one thread can access the attribute inside lock, time will increase for the operation
# But the chances of something going wrong decreases significantly
lock = threading.Lock()

def downloader(url):
    print(f"Starting download from {url}")
    with lock:
        resp = requests.get(url)
    print(f"Download Finished from {url}. [ {len(resp.content)} ] bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
        ]

# Start the timer
start = time.time()

# Thread doesnt require a main method
# Dont forget to add a comma for single arg, because its a tuple
threads = []

for url in urls:
    thread = threading.Thread(target=downloader, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

 # End the thing
end = time.time()

print(f"Time Taken: {end-start:.2f}")
