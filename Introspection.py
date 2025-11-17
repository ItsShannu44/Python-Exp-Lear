l=[1,2,3,4]
s='Hello'
t=(1,2,3)
sets={1,2,3}
d={1:2,2:3,3:4}
n=123

print(dir(l))
print(l.__add__([5]))

print(l.__class__)
print(l.__sizeof__())
print(l.__hash__)
print(l.__contains__(10))
print(dir(s))
print(s.endswith('a'))
print(t.__add__((23,)))
print(id(t))
print(dir(sets))
print()