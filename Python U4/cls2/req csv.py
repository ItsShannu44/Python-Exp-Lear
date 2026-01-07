import requests as req
import csv

response=req.get('https://dummyjson.com/post')
data=response.json()
print(data)

posts=data['posts']
print(type(posts), posts)

with open('api_data_1.csv','w',newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["ID","Title","UserID","Views"])
    for p in posts:
        writer.writerow(p['id'],p['title'],p['userId'],p['views'])
print('Data Written Successfully.')

