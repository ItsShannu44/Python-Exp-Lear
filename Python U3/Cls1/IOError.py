try:
    f=open('new.txt','w+')
    # f.write("shannu")
    s=input("Enter the content:")
    f.writelines(s)
    f.seek(2)
    print(f.read())
except IOError as e:
    print(f'IOError: {e}')