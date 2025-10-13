from collections import Counter

l=[1,2,3,4,5,6,1,4,4,7,1,2,4]
print(Counter(l))

#____________DEQUE_________________

from collections import deque

d=deque([10,20,30,40,50])
print(type(d))

#Insertion
#(Rear)
d.append(60)
print(d)


#Front

d.appendleft(80)
print(d)

#Deletion 
#Rear

d.pop()
print(d)

#Front
d.popleft()
print(d)

#Chainmap

from collections import ChainMap as cm

#Creation

d1={1:"a",2:"b",3:"c"}
d2={3:"e",4:"f"}
d3={5:"g",6:"h"}

c=cm(d1,d2,d3)
print(c)
print(type(c))


#Accessing Values

print(c[1])
print(c[5])
print(c[2])

#adding a new chain at the front of ChainMap
#ChainMap is Immutable 
print(id(c))
c=c.new_child({4:'g',6:'o'})
print(c)
print(id(c))

#View all map except 1st one

print(c.parents)

#Ways to Display

#variable.items() -Key value
#variable.keys() -key
#variable.values() -value


#____________ORDERED DICTIONARY____________

from collections import OrderedDict as od

#Create 
o_d=od({1:'a',2:'b',3:'c',4:'d'})
print(o_d)
print(type(o_d))

o_d1=od([(1,'a'),(2,'b'),(3,'c')])
print(o_d1)
print(type(o_d1))

#Move val
o_d.move_to_end(1)
print(o_d)

#Display it in rev
for k in o_d:
    print(k)

for k in reversed(o_d):
    print(k)

#Default Dict
d={1:'a',2:'b'}
print(type(d))
print(d[1],d[2])

#Integer default dict
from collections import defaultdict as dd

id=dd(int)
id['a']=1
id['b']+=1
print(id,type(id),id['c'])

#Float Default Dictonary
id=dd(float)
id['a']=1
id['b']+=1
print(id,type(id),id['c'])

#Complex default dict
id=dd(complex)
id['a']=1
id['b']+=1
print(id,type(id),id['c'])

#List default dict
id=dd(list)
id['a']=1
id['b']=1
print(id,type(id),id['c'])

#Dict default dict
id=dd(dict)
id['a']=1
id['b']=1
print(id,type(id),id['c'])

#Set default dict
id=dd(set)
id['a']=1
id['b']=1
print(id,type(id),id['c'])

#Tuple default dict
id=dd(tuple)
id['a']=1
id['b']=1
print(id,type(id),id['c'])

#String defaut dict
id=dd(str)
id['a']=1
id['b']=1
print(id,type(id),id['c'])

#Function default dict
def valueisnotpresent():
    return 'Value is not present'
id=dd(valueisnotpresent)
id['a']=1
id['b']=1
print(id,type(id),id['c'])

#_______________________________________________



stud=[{'name':'John','score':23,'name':'bob','score':67,'name':'mark','score':23}]

group_by_score=dd(list)

for s in stud:
    group_by_score[s["score"]].append(s)

for score, s_list in group_by_score.items():
    print(f'Score - {score}')
    for s in s_list:
        print(f'\t-{s['name']}')

