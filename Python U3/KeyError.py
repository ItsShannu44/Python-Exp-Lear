# d={'name':'Alpha','age':20,'city':'Mangalore'}
# print(d['address'])

#Lookup Error

try:
    d={'name':'Alpha','age':23,'city':'Mangalore'}
    d['address']
except LookupError as e:
    print(f'LookupError:{e}')