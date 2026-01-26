import json

p='{"Name":"Stacy", "Age":24}'
p_data=json.loads(p)
print(type(p),'\n', p_data)
print(p_data["Name"])

with open('pr_json_file.json','w+')as f:
    json.dump(p_data, f) #write
    f.seek(0)
    print(json.load(f)) #read
