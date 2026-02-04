with open('sample_data.txt','w') as f:
    data=input("Enter the content:")
    f.writelines(data)

with open('sample_data.txt','r') as f:
    content=f.read()
    print(content)
