import asyncio
import time

async def Job(name,delay):
    start=time.time()
    print(f"The Job {name} is started")
    await asyncio.sleep(delay)
    end=time.time()
    total_time=round(end-start,2)
    print(f'Job {name} executed in {total_time} seconds')
    return name, total_time


async def main():
    t0=time.time()
    await asyncio.gather(Job("a",2),Job("b",5))
    t1=time.time()
    t_t=t1-t0
    print(f"The total execution time in sec:{t_t}")

asyncio.run(main())