import pandas as p
df=p.read_excel("expenses.xlsx")
df.groupby("Category")["Amount"].sum().to_excel("monthly_summary.xlsx")
