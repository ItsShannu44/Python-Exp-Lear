import requests as req
import xml.etree.cElementTree as ET

response=req.get('https://dummyjson.com/post/120')

#Check if the request was successful.
if response.status_code==200:
    print('Request Successful')
else:
    print(f"req failed: {response.status_code}")

print(type(response.text), response.text)

 
data=response.json()
print(data)

root=ET.Element("post")
id_el=ET.SubElement(root, "id")
id_el.text=str(data['id'])
title_el=ET.SubElement(root,"title")
title_el.text=str(data['title'])
user_el=ET.SubElement(root,["userId"])
user_el.text=str(data['userId'])
tree=ET.ElementTree(root)
tree.write("api_data.xml",xml_declaration=True)
print('data stored successfully')