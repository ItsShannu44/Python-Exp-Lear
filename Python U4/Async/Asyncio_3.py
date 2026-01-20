''' Program to implement both synchronous and asynchronous execution for calculating square of a range of numbers'''

import asyncio, time

async def square_async(n):
    await asyncio.sleep(0.1)
    return n*n

async def compute_squares_async(start, end):
    tasks = []
    for i in range(start, end+1):
        tasks.append(square_async(i))
        return await asyncio.gather(*tasks)
    
async def main_async():
    start = int(input("Enter the starting point: "))
    end = int(input("Enter the ending point: "))
    t0 = time.time()
    results = await compute_squares_async(start, end)
    t1 = time.time()
    for i, sq in enumerate(results, start):
        print(f'Async square of {i} is {sq}')
        print(f'Async time of {round(t1 - t0, 2)}')

asyncio.run(main_async())