n=int(input("Enter a numerator"))
try:
    d=int(input("Enter the denominator"))
    print(n/d)
except:
    print("Error: Denominator cannot except 0")
finally:
    print("division may have occured.")