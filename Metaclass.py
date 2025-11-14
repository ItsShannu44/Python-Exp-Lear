
#Creating the class without using the class keyword.

def greet(self):
    print(f"Hello {self.name}")

Student=type('student',(object,),{'greet':greet, 'name':'XYZ'})

#create the obj of cls

s=Student()
print(type(s))


s.greet()





#Creation of custom metaclass

class RequiredId(type):
    def __new__(cls, name, bases, attr):
        if 'id' not in attr:
            attr['id']=100
        return super().__new__(cls, name, bases, attr)
    


#Create a class that uses the custom meta class
class Student(metaclass=RequiredId):
    def __init__(self, name):
        self.name=name

s=Student('ABC')
print(s.name)
print(s.id)

class Teacher(metaclass=RequiredId):
    id=20
    def __init__(self, name):
        self.name=name
t=Teacher('XYZ')
print(t.name)
print(t.id)




#Create metaclass with Inheritance

class CMeta(type):
    def __new__(cls, n, b, d):
        print(f'Creating a class {n}')
        d['createdby']='CMeta'
        d['createdon']='14 NOv'
        return super().__new__(cls, n, b, d)
    
#use metaclass keyword
class ExampleA(metaclass=CMeta):
    def greet(self):
        print("Hello from ExampleA")

class ExampleB(ExampleA):
    def greet(self):
        print('Hello from ExampleB')

ExampleA().greet()
ExampleB().greet()

print(ExampleA().createdby)
print(ExampleA().createdon)

class ExampleC(ExampleB):
    def greet(self):
        print('Hello from ExampleC')

print(ExampleC().createdby)