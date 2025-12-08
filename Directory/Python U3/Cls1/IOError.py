try:
    f=open('new.txt','r')
    print('File opened')
except IOError as e:
    print(f'IOError: {e}')