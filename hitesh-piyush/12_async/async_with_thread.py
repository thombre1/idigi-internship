import threading
import asyncio
import aiohttp

# First make two async functions that have a httpbin 2 sec delay and 3 sec delay
# then make threads and make them run concurrently

async def make_chai(name):
    print(f"Making {name} chai...")
    await asyncio.sleep(2)
    print(f"Done with {name}...")


async def fetch_data(session, url, delay):
    async with session.get(f"{url}/{delay}") as response:
        print(f"I got the response from {url} as {response.status}")

# create a wrapper
async def wrapper(name, url, delay):
    async with aiohttp.ClientSession() as session:
        await make_chai(name)
        await fetch_data(session, url, delay)

def entry_point(name, url, delay):
    asyncio.run(wrapper(name, url, delay))


# Create Threads
def thread_handler():
    thread1 = threading.Thread(target=entry_point, args=("Masala", "https://httpbin.org/delay",3))
    thread2 = threading.Thread(target=entry_point, args=("Ginger", "https://httpbin.org/delay",4))
    
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


thread_handler()
