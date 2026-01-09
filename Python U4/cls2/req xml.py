import requests as req
import xml.etree.ElementTree as ET

response=req.get('https://dummyjson.com/post')
data=response.json()

root=ET.Element("posts")
for item in data['posts']:

    p_el=ET.SubElement(root,"post")
    id_el=ET.SubElement(p_el,"ID")
    id_el.text=str(item['id'])

    t_el=ET.SubElement(p_el,"Title")
    t_el.text=str(item['title'])

    u_el=ET.SubElement(p_el,"UserID")
    u_el.text=str(item['userId'])

    v_el=ET.SubElement(p_el,"Views")
    v_el.text=str(item['views'])
    tree=ET.ElementTree(root)

    
tree.write('api_data_1.xml', xml_declaration=True)
print("Data Stored Successfully")