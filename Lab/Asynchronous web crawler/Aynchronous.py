import asyncio
import aiohttp
import time

urls = ["https://example.com", "https://example.org"]

async def fetch(session, url):
    for _ in range(3):
        try:
            async with session.get(url) as r:
                print(url, r.status)
                return
        except:
            print("Retry:", url)

async def main():
    async with aiohttp.ClientSession() as s:
        await asyncio.gather(*(fetch(s, u) for u in urls))

start = time.time()
asyncio.run(main())
print("Time:", time.time() - start)