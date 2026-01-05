import requests as r
import json

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
