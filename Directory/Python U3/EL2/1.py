import csv
d={}
for r in csv.DictReader(open("students.csv")):
    d.setdefault((r['RollNo'],r['Name']),[]).append(int(r['Marks']))

w=csv.writer(open("student_summary.csv","w",newline=""))
w.writerow(["RollNo","Name","AverageMarks","Result"])
for (r,n),m in d.items():
    a=sum(m)/len(m)
    w.writerow([r,n,a,"Pass" if a>=40 else "Fail"])
