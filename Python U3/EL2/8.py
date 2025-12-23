import csv,pandas as p
fare=lambda d:400 if d<=5 else 650 if d<=10 else 900
rows=[]
w=csv.writer(open("bus_pass_fare_list.csv","w",newline=""))
w.writerow(["ReqID","StudentID","Fare"])

for r in csv.DictReader(open("bus_pass_requests.csv")):
    f=fare(int(r['DistanceKm']))
    r["Status"]="Pending"
    rows.append(r)
    w.writerow([r["ReqID"],r["StudentID"],f])

p.DataFrame(rows).to_excel("bus_pass_status.xlsx",index=False)
