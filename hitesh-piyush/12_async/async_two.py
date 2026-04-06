import asyncio
import aiohttp
import time

# Just some aiohttp syntax dont worry read docs
async def fetch_data_from_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data_from_url(session, url) for url in urls]
        # Unpacks the tasks array on the go
        await asyncio.gather(*tasks)
        # same as writing await asyncio.gather(tasks[0], tasks[1], tasks[2])

start = time.time()
asyncio.run(main())
end = time.time()
print(f"{end - start:.2f} sec")
