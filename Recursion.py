def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter the number"))
print(f"The factorial of {n} is:", factorial(n))



#_______________ Recursive function for adding up to n val___________

def sumofn(n):
    if n==0:
        return 0
    return n+sumofn(n-1)

n=int(input("Enter the num"))
if n<0:
    print(f"sum of {n} values is not possible")
else:
    print(f"sum of n is {sumofn(n)}")