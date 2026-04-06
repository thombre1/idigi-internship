import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

# What if we have a function that is not async
# It will block the execution of the current thread if it takes time
# so we use ThreadPoolExecuter to form another thread for that particular method
# The method runs in another thread while our current thread remains unblocked


# a simple function, which will block the working thread for 3 seconds
def check_item_stock(item):
    print(f"Check {item} in store...")
    time.sleep(3)
    print(f"{item} stock: 42")

# an async function which uses the ThreadPoolExecutor

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_item_stock, "Masala")
        print(result)


asyncio.run(main())
