# class MyUserDict(MyUserDict):
#     def get_keys(self):
#         return 


from collections import namedtuple

Person=namedtuple('Person',{'name','age'})

p1=Person(name='Alias',age=10)
p2=Person('Bob',70)
p3=Person(age=11,name='Harry')

print(p1)
print(p3.name)

#____________USER LIST___________

from collections import UserList

#Create a custom list of a type userList

class CustomList(UserList):
    def addtwice(self, value):
        self.data.append(value)
        self.data.append(value)
    def remtwice(self, pos):
        self.data.pop(pos)
        self.data.pop(pos)

#----Create an instance of CustomList

cl=CustomList([1,2,3,4,5,6,7])
cl.append(8)
print(cl)
cl.extend([9,10])
print(cl)
cl.insert(0,0)
print(cl)
cl.pop(3)
print(cl)
cl.remove(4)
print(cl)
cl.reverse()
print(cl)
cl.sort()
print(cl)

#------Custom Methods
cl.addtwice(12)
print(cl)
cl.remtwice(5)
print(cl)

#----USER STRING-----
from collections import UserString

class MyString(UserString):
    def uppercon(self):
        return self.upper()
    
    def add_exclamation(self):
        return self.data+"!!!"
    
cs= MyString("hello, how r u")
print(cs)

#Custom Methods
print(cs.uppercon())

cs=cs.add_exclamation()
print(cs)

print(id(cs))