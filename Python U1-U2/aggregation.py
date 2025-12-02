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


#Aggregat teacher to the school

s1.add_teacher(t1)
s1.add_teacher(t3)
s2.add_teacher(t1)
s2.add_teacher(t2)
s2.add_teacher(t3)

s1.show_teachers()
s2.show_teachers()



# A user creates folder, folder has files, files have paragraph, paragraph have words, each word made up of characters.