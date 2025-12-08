x=10
if x==10:
    print(x)

#logical errors

def fact_cal(n):
    r=1
    for i in range(n): #logical error it starts with 0,
        r=r*i
    print(r)

def fact_cal(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    print(r)
fact_cal(4)

#LIst of exceptions handled in py

import builtins

l=[name for name in dir(builtins)
   if isinstance(getattr(builtins, name),type)
   and issubclass(getattr(builtins, name), BaseException)]
print('List of Excep in py')
for i in l:
    print(i)

#Overflow Error
# import math
# math.exp(1000)

# pow(3.14,1000)


def fact_cal(n):
    r=1
    for i in range(1, n+1):
        r*=i
    return r
print(fact_cal(1000))

#Zero division Error

# print(10/0)

#Attribute Error 


# s="Hello to Errors"
# print(s.reverse())

class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, My name is {self.name}")

p1=Person('Deathstroke',45)
p1.greet()