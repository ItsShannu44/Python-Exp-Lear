class Student:
    school_name=" PESU"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f"The student {self.name} of {self.age} years is studying in{self.school_name}")
        print(f"The student {self.name} of {self.age} years is studying in{Student.school_name}")

s1=Student('abc',15)
s2=Student('Manu',20)

s1.show()
s2.show()