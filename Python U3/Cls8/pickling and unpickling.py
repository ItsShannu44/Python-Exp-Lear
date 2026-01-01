import pickle as p 

a, b, c=10, 10.5, 10-9j

with open('numeric.pkl','wb') as f:
    p.dump(a,f)
    p.dump(b,f)
    p.dump(c,f)

with open('numeric.pkl','rb') as f:
    data=p.load(f)
print(f'Unpickled data is {data}')


#2.--------LIST------------
print()
l1=['apple',23,56,78,'Banana',89-9j,['a','b','c']]
print()
with open('list.pkl','wb') as f:
    p.dump(l1,f)
with open('list.pkl','rb') as f:
    p_l1=p.load(f)
print(f'Unpickled List is : {p_l1}')
print(f'Type of p_l1 is {type(p_l1)}')
print(f'Type of f is {type(f)} and type of list.pkl is {list('list.pkl')}')

#3.----------DICT-----------
print('\n\n')
d_1={'name':'Alpha','age':20,'city':'Bangalore','phone':9900909090}
with open('dict.pkl', 'wb') as f:
    p.dump(d_1, f)
with open('dict.pkl','rb') as f:
    p_d_1=p.load(f)
print(f'Unpickled data is {p_d_1}')


#4.----------Custom Object----------

print('\n\n')
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def __repr__(self):
        return f'Person (name:{self.name}, age: {self.age})'
p1=Person('Alpha', 24)

with open('obj.pkl','wb') as f:
    p.dump(p1, f)
with open('obj.pkl','rb') as f:
    p_obj=p.load(f)
print(f'Unpickled Object is {p_obj}')

#5.----------Multiple Object----------
print('\n\n')
l1=[1,2,3,'apple',[2,3,4],89+9j]
d1={1:2,3:4}
s1="Morning Everyone"
with open('all.pkl','wb') as f:
    p.dump(l1, f)
    p.dump(d1, f)
    p.dump(s1, f)
with open('all.pkl','rb') as f:
    p_l1=p.load(f)
    p_d1=p.load(f)
    p_s1=p.load(f)
print(f'{p_l1},{p_d_1},{p_s1}')


#6.-----------Functions---------

def greet(name):
    return f'Hello {name}'

with open('func.pkl','wb') as f:
    p.dump(greet, f)
with open('func.pkl','rb') as f:
    p_f=p.load(f)

g1=greet('Alpha')
g2=greet('Beta')
print(g1,g2)

#7.--------------Data Frames----------
print('\n\n')
import pandas as pd

data={'Name':['Alpha','Beta','Gamma'],
      'Age':[12,34,67],
      'City':['Bangalore','Mangalore','Mysore']}
df=pd.DataFrame(data)
print(df,'\n',type(df))

df.to_pickle('df.pkl')
p_df=pd.read_pickle('df.pkl')
print(p_df,'\n',type(p_df))


#-------------LOADS and Dumps--------
# dump-serialize the data from a Fille
# load-desiarable data from a File
# dumps- serialize the data as bytes in memory
# loads- desirable bytes into data


print('\n\n')

a=10
p_a=p.dumps(a)
print(p_a),print(type(p_a))
print(p.loads(p_a))

b, c, d= 45, 7, "Hello"
p_b=p.dumps(b)
p_c=p.dumps(c)
p_d=p.dumps(d)
print(f'Deserialized data is {p.loads(p_b)},{p.loads(p_c)},{p.loads(p_d)}') 