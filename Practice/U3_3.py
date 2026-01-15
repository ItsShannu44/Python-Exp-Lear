# A program performs arithmetic operations on mix types handle the type errors that are caused by incompatible operations.

def arithmetic_operation():
    try:
        a = int(input("Enter first value: "))
        b = input("Enter second value: ")
        result = a + b      
        print("Result:", result)
    except TypeError:
        print("Type Error: Incompatible data types for arithmetic operation.")

arithmetic_operation()
