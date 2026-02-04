#Exception Handling

try:
    num1=int(input("Enter the num1:"))
    num2=int(input("Enter the num2:"))
    res=num1/num2
    print("Division Successful..")
except ZeroDivisionError as e:
    print(f"Division by zero not allowed {e}")
except ValueError as e:
    print(f'Value Error: {e}')

#Try else except finally
try:
    n=int(input("Enter number:"))
    if n%2!=0:
        print("Not an even.")
    else:
        print("Even")
except:
    print("Invalid Input")
finally:
    print("Prgrm ended")

#user defined exception
class AgeError(Exception):
    pass

try:
    age=int(input("Enter the age:"))
    if age<18:
        raise AgeError("Not eligible")
    else:
        print("Eligible to vote")
except AgeError as e:
    print(f"AgeError:{e}")
except ValueError as e:
    print(f"Invalid Input: {e}")
finally:
    print("Prgrm ended")

