class Teacher:
    def __init__(self, name, subject):
        self.name=name
        self.subject=subject
    def teach(self):
        print(f"{self.name} teaches {self.subject}")

class School:
    def __init__(self, name):
        self.name=name
        self.teachers=[]
    
    def add_teacher(self,t): #t is the obj of the teacher class
        self.teachers.append(t)

    def show_teachers(self):
        print(f"Teachers in {self.name}:")
        for t in self.teachers:
            print(f"{t.name} for {t.subject}")

s1=School('ABC School')
s2=School('PQR High School')
t1=Teacher("Mr.xyz","Maths")
t2=Teacher("Mr.ABC","Chemistry")
t3=Teacher("Mr.Tuv","CS")