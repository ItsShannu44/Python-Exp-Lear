import asyncio
import time

async def square(n):
    start = time.time()
    await asyncio.sleep(1)
    end = time.time()
    print("Square of", n, "is", n*n)
    print("Asynchronous time:", round(end - start, 2))

async def main():
    tasks = [square(i) for i in range(1, 6)]
    await asyncio.gather(*tasks)


asyncio.run(main())



