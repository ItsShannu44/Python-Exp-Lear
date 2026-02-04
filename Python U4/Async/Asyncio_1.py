import asyncio
import time

async def Job(name, delay):
    start = time.time()
    print(f'Job {name} started')
    await asyncio.sleep(delay)
    end = time.time()
    tt = round(end-start, 2)
    print(f'Job {name} executed in {tt} seconds')
    return name, tt

async def main():
    t0 = time.time()
    results = await asyncio.gather(Job(1, 12), Job(2, 3), Job(3, 1), Job(4, 2), Job(5, 5), Job(6, 2))
    t1 = time.time()
    print(f'Overall time taken for execution is {t1 - t0} seconds')
    print('Individual Task Time')
    for name, taken in results:
        print(f'Job {name} took {taken} seconds')

asyncio.run(main())