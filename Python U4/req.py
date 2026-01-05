import requests as r
import json
import csv

response=r.get('https://dummyjson.com/posts/120')
print(type(response))
print(response)


#Check if the request was successful.
if response.status_code==200:
    print('Request Successful')
else:
    print(f"req failed: {response.status_code}")

print(type(response.text), response.text)

data=response.json()
print(f'Post Title: {data['title']}')

print(f'Post User: {data['userId']}')


print("\n\n")
#Write a single API data into a JSON File
response=r.get("https://dummyjson.com/posts/121")
data=response.json()
print(data)
print(type(data))

#Save the data to the json file with format
with open('api_data.json','w') as f:
    json.dump(data, f, indent=4)
print('Data Saved to file.')
print("\n\n")


#Write multiple api data into a json file
response=r.get('https://dummyjson.com/posts')
#convert the data to JSON Obj
data=response.json()
print(data)

#save data to json
#process data to individual rec
posts_list=[]
for post in data['posts']:
    posts_list.append({'id':post['id'],
                       'titlt':post['title'],
                       'body':post['body'],
                       'userId':post['userId'],
                       'reactions':post['reactions']})
print()
print(posts_list)

#store
with open('api_data_1.json','w')as f:
    json.dump(posts_list,f ,indent=4)
print('Data inserted successfully')

#save single api data into csv file
with open('api_data.csv','w',newline="")as f:
    writer=csv.writer(f)
    writer.writerow(['Id','Title','Body','userId'])
    writer.writerow([data['id'],data['title'],data['body'],data['userId']])
print('Data stored in a csv file.')
