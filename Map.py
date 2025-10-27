#_____________LAMBDA Func________________

x=lambda a: a*a
print(type(x), id(x))

print(x(20))

l=[1,2,7,9,-9,78,90]
print(x(l[4]))

#______________________MAP______________
b=list(map(x,l))
c=list(map(lambda a:a*a,l))
print(c)



d=list(map(len,['apple','banana','cherry','jackfruit','melon']))
print(d)


def square(x):
    return x*x

sq=list(map(square,[1,3,5,6,8,9,10]))
print(sq)


s_upper=list(map(str.upper,['alb','max','bob']))
print(s_upper)

#_________________LAMBDA FUNCTIONS____________________
#__________________condition based________________________


is_even=lambda x: x%2==0
print(is_even(10))



l=list(map(is_even,[12,34,23,67,89,88]))
print(l)













# a=['apple','pineapple','f','mangoes']
# b=list(map(a, 2))
# print(b)