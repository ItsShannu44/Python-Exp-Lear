n=int(input("Ente the numerator"))
try:
    d=int(input("Enter the dinominator"))
    print(n/d)
except ZeroDivisionError as f:
    print(f"ZeroDivisionError:{f}")


