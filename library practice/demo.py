try:
    a = int(input("enter the first number"))
    b = int(input("enter second number"))
    sum = (a+b)
except ValueError as e :
    print(f'{e} provide the right input')
finally:
    print(sum)

