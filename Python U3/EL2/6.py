import csv
d={}
for f in ["theory_marks.csv","lab_marks.csv"]:
    for r in csv.DictReader(open(f)):
        d[r['RollNo']]=d.get(r['RollNo'],0)+int(r['Marks'])

w=csv.writer(open("final_result.csv","w",newline=""))
w.writerow(["RollNo","TotalMarks","Result"])
for k,v in d.items():
    w.writerow([k,v,"Pass" if v>=40 else "Fail"])
