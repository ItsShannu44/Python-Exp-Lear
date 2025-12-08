try:
    n=int(input("Enter a num"))
    assert n%2==0
except:
    print('Not an even num')
else:
    print(n/4)