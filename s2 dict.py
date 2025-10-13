#------------Dictionary----------

d={1:'a'}

print(type(d), id(d))

#--------Methods----
#Adding
d[2] = 'c'
print(d)
d[3] = 'd'
print(d)


#get
print(d.get(2))

#display
print(d.items())

#access key
print(d.keys())

#access val
print(d.values())

#pop()
print(d.pop(2))

#popitem()
print(d.popitem())