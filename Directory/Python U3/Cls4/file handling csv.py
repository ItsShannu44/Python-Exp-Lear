import csv

# Read CSV files
with open('data.csv','r') as f:
    read=csv.reader(f)
    for r in read:
        print(r)


with open('data1_8dec.csv','r') as f:
    read=csv.reader(f, delimiter= ';', skipinitialspace= True)
    for r in read:
        print(r)
        