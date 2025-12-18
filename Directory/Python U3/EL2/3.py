import pandas as p
df=p.read_excel("attendance.xlsx")
df["AttendanceStatus"]=(df.DaysPresent/df.TotalDays*100<75).map({True:"Shortage",False:"OK"})
df.to_excel("attendance_report.xlsx",index=False)
