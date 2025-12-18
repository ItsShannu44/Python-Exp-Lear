import csv
d={}
for r in csv.DictReader(open("daily_sales.csv")):
    d[r['Region']]=d.get(r['Region'],0)+float(r['Amount'])

w=csv.writer(open("region_sales.csv","w",newline=""))
w.writerow(["Region","TotalSales"])
for k,v in d.items():
    if v>=50000: w.writerow([k,v])
