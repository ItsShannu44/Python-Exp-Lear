s1='Hello'
s2="Hello"
s3='''Hello'''
s4="""Hello"""

print(s1, s2 , s3, s4)
print(id(s1), id(s2), id(s3), id(s4))

s1="Hi"
print(id(s1), id(s2), id(s3), id(s4))

# num1 = 256
# num2 = 256
# num3 = -5678
# num4 = -5678
# print(id(num1), id(num2), id(num3), id(num4))

s1="hello this statement is used for counting"
c=s1.count('o')
print(c)

#count
c=s1.count('O')
print(c)


#find
s1="Hello this string is used for implementing the find method"
f=s1.find('o')
print(f)


#index
s2="Hello this string is used to implement Index method"
print(s2.index('o'))  #returns the index if val is only found otherwise err



#parttiion
new="This string will be partitioned based on a value"
print(new.partition(' '))
print(new.partition('S'))
print(new.partition('s')) #('Thi', 's', ' string will be partitioned based on a value')
print(new.partition('T'))


#split
new="This string will be split based on a value"
print(new.split(' ')) # ['This', 'string', 'will', 'be', 'split', 'based', 'on', 'a', 'value']
print(new.split('S')) #['This string will be split based on a value']
print(new.split('s')) #['Thi', ' ', 'tring will be ', 'plit ba', 'ed on a value']
print(len(new))

#------------------   LISTS ---------------------

l=[1,4,6,3,2]
print(type(l))


l1=list("This is a list15")
print(l1)
print(len(l1))
print(type(l1[15]))

l2 = [1,2,3,4,5,6,"12345"]
print(type(l2))


l5=[1,2,3,4]
l6=l5.copy()
print(l5,l6)

l5[2]=45
print(l5,l6)

print(id(l5), id(l6)) #diff loc cuz the l6 is an copy of l5 so the loc changes


