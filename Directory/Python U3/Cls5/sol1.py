import xml.etree.ElementTree as xml
employees=[
    {'Name':"Tom",
     'Age':24,
     'Salary':20000,
     'Category':'Dayscholar'},
    {'Name':"Max",
     'Age':26,
     'Salary':18500},
    {'Name':"Steve",
     'Age':44,
     'Salary':32000,
     'Category':'Accomodation'},
]

root=xml.Element("employees")
print(type(root))
print(employees)
for emp in employees:
    empl=xml.Element('employees')
    root.append(empl)
    empl.set('Category',empl['Category'])
    name=xml.SubElement(empl,'Name')
    name.text=empl['Name']
    age=xml.SubElement(empl,'Age')
    age.text=empl['Age']
    salary=xml.SubElement(empl,'Salary')
    salary.text=str(empl['Salary'])
tree=xml.ElementTree(root)

for p in root.iter('Salary'):
    p=int(p.text)#-----This converts the str val to int
    p+=20
    p.text=str(p)