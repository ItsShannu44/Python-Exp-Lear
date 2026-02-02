x = 2 * 2 ** 3
print(x)

print(0.1 + 0.2 == 0.3)

print("James" * 2 * 3)

#Check Interpreter type
import platform
print(platform.python_implementation())

#ABSOLUTE file path
import os
file = input("Enter filename: ")
print(os.path.abspath(file))

#Decimal->Binary, Octal, Hex
n = int(input("Enter Binary Val to convert: "))
print(bin(n))
print(oct(n))
print(hex(n))



#Count vowels in string
s = input()
count = 0
for ch in s:
    if ch.lower() in 'aeiou':
        count += 1
print(count)

#sum of even numbers function
def sum_even(lst):
    return sum(x for x in lst if x % 2 == 0)


#Recursive function
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
