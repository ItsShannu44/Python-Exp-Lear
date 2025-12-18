import csv,pandas as p
ok,er=[],[]
bill=lambda u:u*4 if u<=100 else 400+(u-100)*6 if u<=200 else 1000+(u-200)*8

for r in csv.DictReader(open("meter_readings.csv")):
    u=int(r["CurrentReading"])-int(r["PreviousReading"])
    if u<0: er.append({**r,"ErrorReason":"Negative Units"})
    else: ok.append([r["ConsumerID"],r["Name"],u,bill(u)])
 
p.DataFrame(ok,columns=["ConsumerID","Name","Units","BillAmount"]).to_excel("bills.xlsx",index=False)
p.DataFrame(er).to_csv("billing_errors.csv",index=False)
