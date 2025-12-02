students = {"A": 80, "B": 65, "C": 90}
result = {k: v for k, v in students.items() if v > 70}
print(result)

#_---------SET__________
string="Shanmukha"
freq={ch: string.count(ch) for ch in set(string) }
print(freq)

word="Hey bro i am shannu here."
words={w for w in word if len(w)<=3}
print(words)

#--------------DICTIONARY-------------
squares={x: x**2 for x in range(1,10)}
print(squares)

students=[{'name':'alice','scores':{'math':90,'science':45}},{'name':'bob','scores':{'math':86,'science':67}},{'name':'john','scores':{'math':80,'science':45}}]
squared_scores={student['name']: {subject: score**2 for subject, score in student['scores'].items()}for student in students}
print(squared_scores)

#_----------ITERATORS

my_list=[22,7,9,0]
my_ite=iter(my_list)
print(next(my_ite))


my_list=[22,7,9,0]
my_ite=iter(my_list)
for item in my_ite:
    print(item)

num=(x for x in range(10**6))
print(next(num))