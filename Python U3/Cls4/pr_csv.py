import csv

with open("data.csv",'w',newline="")as f:
    writer=csv.writer(f)
    writer.writerow(['Name','Age','Place'])
    n=int(input("how much data you want to enter"))
    for i in range(n):
        name=input("Enter name")
        age=input("Enter age")
        place=input("Enter place")
        writer.writerow([name,age,place])

    print("Data Written successfully")

with open("data.csv",'r')as f:
    read=csv.DictReader(f)
    for r in read:
        print(r)   


