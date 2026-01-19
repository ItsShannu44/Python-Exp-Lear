from multiprocessing import Process
import os

def child_activity():
    print('Child Process')
    print(f'Child PID: {os.getpid()}')
    print(f'Parent PID: {os.getpid()}')

if __name__=='__main__':
    print('Before proces starts')
    p=Process(target=child_activity) #process obj
    p.start()
    print("Parent process")
    print(f'Parent PID: {os.getpid()}')
    print(f'parent created the child with ID: {p.pid}')
    p.join()
    print('Parent finished after join')
    