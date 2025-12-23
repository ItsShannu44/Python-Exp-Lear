import pandas as p
df=p.read_excel("emp_data.xlsx")
df["GrossSalary"]=df.BasicSalary*1.28
df[["EmpID","Name","GrossSalary"]].to_excel("emp_salary.xlsx",index=False)
