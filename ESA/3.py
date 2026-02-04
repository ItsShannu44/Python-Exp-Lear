#Name Mangling 

class Parent:
    def __display(self):
        print("Parent Cls")

class Child(Parent):
    def __display(self):
        print("Child Class")
    
obj=Child()
print(obj._Child__display())





#Super Keyword With MRO

class Parent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print(f"Student name is {self.name}")
    
class Child(Parent):
    def __init__(self,name, age):
        super().__init__(name,age)
        print(f"Student {self.name} of age {self.age} did a suicide at PESU")
ob=Child("Shannu",21)
print(Child.mro())
print(Child.__mro__)
print(help(Child))