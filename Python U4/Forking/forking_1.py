from multiprocessing import Process
import os

def child_process(name):
    print(f"Child Process {name}: PID={os.getpid()}, Parent PID={os.getppid()}")

if __name__ == "__main__":
    print("Before process starting")

    # Pass argument using args
    p = Process(target=child_process, args=("A",))
    p.start()

    print(f"Parent Process: PID={os.getpid()}")
    print("Parent created a child with PID:", p.pid)

    p.join()
    
    
    
    
#Program to control the child process
from multiprocessing import Process
import os
import time

def child_activity():
    time.sleep(1)
    print("Child activity started after a pause")
    print(f'Child process ID: {os.getpid()}')
    print(f'Parent process ID: {os.getppid()}')
    
    
if __name__ == "__main__":
    print('Parent starts immediately')
    print(f'Parent process ID: {os.getpid()}')
    p=Process(target=child_activity)
    p.start()
    print(f'Parent created a child with PID: {p.pid}')
    p.join()
    print("After process has finished")