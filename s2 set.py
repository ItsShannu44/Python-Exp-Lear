#----------------SET----------------
s={1,2,3}
print(type(s), id(s))


s={1,2,3,4,4,4,1,1,2,3,5,2,1}
print(s)


#Set Methods

#add
s.add(6)
print(s)

s1={1,7,8,9,3}
print(s.intersection(s1))


#union and intersection
print(s1&s)
print(s1|s)


l = [1,2,3]
l1 = [1,2,3]
s = {1,2,3}
t= (1,2,3)
print(id(l),id(s),id(t),id(l1))

fl=frozenset(l)
fs=frozenset(s)
ft=frozenset(t)
print(type(l),type(fl),type(s),type(fs),type(t),type(ft))

