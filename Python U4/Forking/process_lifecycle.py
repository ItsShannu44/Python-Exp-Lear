from multiprocessing import Process , freeze_support
import os
import time

def child_activity():
    print("Child started", flush=True)
    print(f'Child Process ID: {os.getpid()}')
    print(f'Parent of Child: {os.getpid()}')
    time.sleep(5)
    print('Exited from child', flush=True)

def main():
    print('Parent Started',flush=True)
    print(f'Parent Process ID: {os.getpid()}')
    p=Process(target=child_activity)
    p.start()
    print(f'Child process with ID {p.pid} created')
    print(f'Is child alive after start: {p.is_alive()}')
    p.join()
    print(f'Is child alive after join: {p.is_alive()}')
    print('Parent Executed')

if __name__=='__main__':
    freeze_support()
    main()