import json

p='{"name":"Gwen","Age":34}'
p_dict=json.loads(p)
print(type(p),type(p_dict))
print(p)
print(p_dict)

print(p[4]) #Accessing using index cuz its string.
print(p_dict["name"]) #accessing using key cuz its dict.


with open('Json_File1.json','r') as f:
    p_json=json.load(f)
    print(type(p_json))
    print(p_json)

with open('Json_File2.json','r') as f:
    p2_json=json.load(f)
    print(type(p2_json))
    print(p2_json)
    print(p2_json[0]["name"])

    #Display all names
    for r in p2_json:
        print(r["name"])
    
with open('Json_File3.json','r') as f:
    p3_json=json.load(f)
    print(type(p3_json))
    print(p3_json)

    print(p3_json["Alex"]["city"][0])
    print(p3_json["Alex"]["city"][1])

    for r in p3_json:
        print(f"Name: {r}")
        print(f"Age: {p3_json[r]["age"]}")
        print(f"City: {p3_json[r]["city"]}")

#-------Writing the data / JSON Objects--------

n_dict={'name':'Delta','age':24}
n_json=json.dumps(n_dict)
print(type(n_dict), type(n_json))
print(n_dict)
print(n_json)

with open('Json_File4.json','w') as f:
    json.dump(n_dict,f)

with open('Json_File4.json','a')as f:
    json.dump(n_dict,f)

with open('Json_File4.txt','w')as f:
    json.dump(n_dict,f)