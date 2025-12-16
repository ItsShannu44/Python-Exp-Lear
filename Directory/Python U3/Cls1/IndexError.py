class HemanthError(Exception):
    pass

try:
    l=[10,20,30,40,50]
    a = int(input("enter the index"))
    print(f'The output is: {l[a]}')
    b = input("Enter your name: ")
    if b == "Hemanth":
        print(b)
    else:
        raise HemanthError("NKN Hemanth antha bari")
except HemanthError as e:
    print(f'{e} Only Hemanth allowed')
except IndexError as e:
    print(e)
except ValueError as h:
    print(h)
except:
    print("Provide correct values")
finally:
    print("End of program")
