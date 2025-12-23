import csv
w=csv.writer(open("reorder_list.csv","w",newline=""))
w.writerow(["ProductID","ProductName","Stock"])
for r in csv.DictReader(open("inventory.csv")):
    if int(r['Stock'])<int(r['ReorderLevel']):
        w.writerow([r['ProductID'],r['ProductName'],r['Stock']])
