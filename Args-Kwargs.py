import os
os.system('cls')

# def outer():
#     def inner():
#         print("Inside Inner")
#     inner()
#     print("Inside Outer")
# outer()



#-----------------LOCAL Variables in nested Func--------------

# def outer():
#     x=10
#     print(f"Memory loaction of x is {id(x)}")
#     print(f"x={x}")
#     def inner():
#         x=10.0 
#         print(f"Memory loaction of x is {id(x)}")
#         print(f"x={x}")
#     inner()
#     print(f"Memory loaction of x in outer id {id(x)}")
#     print(f"x in outer ={x}")
# outer()

#---------------Passing args to nested functions---------------

# def outer(n):
#     print(f"The value of n in outer is {n}")
#     def inner():
#         m=int(input("Enter the number: "))
#         print(f"The value of m in inner is {m}")
#         print(f"The value of n in inner is {n}")
#     inner()
#     # print(f"The value of m in outer is {m}")
#     print(f"The value of n in outer is {n}")
# n=input("Enter the value:")
# outer(n)

#---------------Packing & Unpacking of Values------------------------

(a,b,c)=[1,2,3]
print(f"a={a}") 
print(f"b={b}") 
print(f"c={c}\n") 



(a,b,c)=["alpha",20,6+4j]
print(f"a={a}") 
print(f"b={b}") 
print(f"c={c}\n") 

def unpack(values):
    a,b,c=values
    print(f"a= {a}, b= {b}, c= {c}\n")
unpack((23,54,79))

