# A function computes a sqrt of a number handle negative inputs.

from math import sqrt

def compute_sqrt():
    try:
        n=int(input("Enter the num to find sqrt: "))
        if(n<0):
            print("Value is negative")
        else:
            print("Square Root of number is:",sqrt(n))
    except ValueError:
        print(f'Value is Negative.')

compute_sqrt()