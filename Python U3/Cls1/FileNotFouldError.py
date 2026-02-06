try:
    f=open('new34.txt','r')# r opens the file if its in read mode
    print('File opened')
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}") 