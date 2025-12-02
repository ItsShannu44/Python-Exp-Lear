students=[]
n=int(input("Enter the number of stud."))
for i in range(n):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    marks=int(input("Enter the marks sub vise:"))
    score={
        "Maths":marks,
        "Science":marks,
        "English":marks
    }
    student={"name": name, 
            "age": age,
            "marks":marks}
    students.append(student)
print(students)