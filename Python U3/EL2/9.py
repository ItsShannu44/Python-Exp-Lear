import pandas as p
df=p.read_excel("returns.xlsx")
v=df[(df.Amount>0)&(df.RefundMode.isin(["UPI","CARD","WALLET"]))]
e=df.drop(v.index)
v.to_csv("returns_clean.csv",index=False)
e.assign(ErrorReason="Invalid Data").to_excel("returns_error_log.xlsx",index=False)
