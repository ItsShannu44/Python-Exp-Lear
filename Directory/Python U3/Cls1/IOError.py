try:
    f=open('new.txt','w+')
    # f.write("shannu du chikdu")
    s=input("Enter the content:")
    f.writelines(s)
    f.seek(0)
    print(f.read())
except IOError as e:
    print(f'IOError: {e}')