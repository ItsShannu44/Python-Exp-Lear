#Append


l=[1,2,3,6,4,5]
l.append(7)
print(l)

# l.append([8,9,10])
# print(l)

#Extend

l.extend([8,9,10])
print(l)

#Pop
l.pop(5)
print(l)

#remove
l.remove(1)
print(l)

#Reverse
l.reverse()
print(l)

#Sort
l.sort()
print(l)

l2=[10,40,4,1,5,1.0]
l2.sort()
print(l2)


l3=[['a'],['A'],['apple']]
l3.sort()
print(l3)

# Sort doesn't work on Heterogenius type.
# l4=[['a'],[1],[4.6],[5+2j]]
# l4.sort()
# print(l4)


