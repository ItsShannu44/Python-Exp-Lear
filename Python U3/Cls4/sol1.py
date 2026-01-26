import csv

input_file = "emp_details.csv"    
output_file = "EMP_Sal.csv"        

def calculate_salary(salary):
    hra = 0.02 * salary  
    da = 0.18 * salary  
    gross = salary + hra + da 
    return hra, da, gross

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=';')
    
    print(f"CSV Headers: {reader.fieldnames}")

    employees = []
    for row in reader:
        name = row['Name'].strip()
        empid = row['Empid'].strip()
        dept = row['Dept'].strip()
        salary = float(row['Salary'].strip())

        hra, da, gross = calculate_salary(salary)

        employees.append({
            "Name": name,
            "Empid": empid,
            "Dept": dept,
            "Salary": salary,
            "HRA": round(hra, 2),
            "DA": round(da, 2),
            "Gross Salary": round(gross, 2)
        })

with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    fieldnames = ["Name", "Empid", "Dept", "Salary", "HRA", "DA", "Gross Salary"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    writer.writerows(employees)

print("EMP_Sal.csv generated successfully.")


