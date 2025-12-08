try:
    l=[0,2,4,6,8,10]
    i1=int(input("Enter the first index"))
    i2=int(input("Enter the second index"))
    print(l[i1]/l[i2])
except IndexError as e:
    print(f"IndexError: {e}. Check the index number")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError:{e}.The index is pointing to a 0 value")