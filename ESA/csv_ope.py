# Assume that you have csv file of emp details that consist of name, empid, dept, sal read the 
# file and compute the following values DA=18% of sal, HRA=2% of sal. 
# Create an output file called as emp_sal.csv where empid, HRA, DA, Gross sal is written back
import csv

with open("emp_details.csv", "r") as fin, open("emp_sal.csv", "w+", newline="") as fout:
    reader = csv.DictReader(fin)
    writer = csv.writer(fout)

    writer.writerow(["Empid", "HRA", "DA", "GrossSal"])

    for row in reader:
        empid = row["Empid"]
        sal = float(row["Salary"])

        da = 0.18 * sal
        hra = 0.02 * sal
        gross = sal + da + hra

        writer.writerow([empid, hra, da, gross])
        fout.seek(0)
    reader=csv.reader(fout)
    for r in reader:
        print(r)