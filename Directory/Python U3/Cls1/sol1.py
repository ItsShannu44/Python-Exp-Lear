import math

try:
    n=int(input("Enter a num: "))
    assert n>0
except:
    print("Not a +ve num")
else:
    r=math.sqrt(n)
    print("sqrt value is:",r)
