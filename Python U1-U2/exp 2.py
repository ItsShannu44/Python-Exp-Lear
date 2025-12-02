from collections import Counter

ShoppingItems=[]
for i in range(5):
    item= input("Enter the items:")
    ShoppingItems.append(item)
    
freq=Counter(ShoppingItems)
maximum=max(freq.values())
print("Shopping items which have occured frequently:")

for itm,count in freq.items():
    if count==maximum:
        print(f"{itm} appears {count} times.")

