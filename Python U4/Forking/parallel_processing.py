from multiprocessing import Process
import os


def worker(n):
    result=n*n
    print(f'Process ID: {os.getpid()}, Task:{n}, Square:{result}')

if __name__=='__main__':
    tasks=[1,2,3,4,5,6,7,8,9,10]
    process=[]
    for n in tasks:
        p=Process(target=worker, args=(n,))
        p.start()
        process.append(p)
    for p in process:
        print(f'Child process id is {p.pid}')
        p.join()
    print(f'Parent PID: {os.getpid()}. All tasks completed')