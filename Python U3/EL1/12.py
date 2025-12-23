class OperationError(Exception): pass
class InputError(Exception): pass

while True:
    try:
        op = input("Enter operation (+ - * /) or exit: ")
        if op == "exit":
            break

        if op not in ["+", "-", "*", "/"]:
            raise OperationError("Unsupported operation")

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except:
            raise InputError("Invalid input")

        if op == "+": print(a + b)
        elif op == "-": print(a - b)
        elif op == "*": print(a * b)
        elif op == "/": print(a / b)

    except (OperationError, InputError) as e:
        print("Error:", e)
