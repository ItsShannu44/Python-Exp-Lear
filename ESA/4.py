#MAking Multiplication table of given num
n=int(input("Enter the num:"))
print(f"The multiplication table of {n} is as follows:\n")

for i in range(1,11):
    r=n*i
    print(f"{n}X{i}={r}","\n")

#Write a Python program that takes a filename as input from the user and prints the absolute path of the file.
import os

filename = input("Enter the filename: ")

abs_path = os.path.abspath(filename)

print("Absolute path of the file is:")
print(abs_path)


#FInd the vowels in a string
str=input("Enter the str:")
count=0
for s in str:   
    if s in ['a','e','i','o','u']:
        count+=1
print("The number of vowels in str is:",count)

# Write a Python function that takes a list of numbers as input and returns the sum of even numbers
def num():
    n = int(input("How many numbers do you want to add to the list? "))
    li = []

    for i in range(n):
        x = int(input("Enter the number: "))
        li.append(x)

    even_sum = 0
    for x in li:
        if x % 2 == 0:
            even_sum += x

    return even_sum


result = num()
print("Sum of all even numbers is:", result)

#Factorial using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

n=int(input("Eter the num:"))
print(f"FActorial of {n} :",fact(n))
