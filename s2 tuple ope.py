t=(1,2,3)

print(type(t), id(t))

t1=(1)
print(type(t1))


t2=tuple('a')
print(type(t2))

t3=('a')
print(type(t3))

t4=((1,2,3),('a','b'),[4,5],'st',0)
print(type(t4))
print(type(t4[2]))

#Count

tpl=(1,2,3,4,1,2,7,1)
print(tpl.count(1))

