import platform, random as r, os

print(f"The host name is: {platform.node()}")

if "USERPROFILE" in os.environ:
    home=os.environ['USERPROFILE']
    print(f"Home directory is :{home}")



#-------------------API ENVIRONMENT----------
# api_key=os.getenv("API_KEY")

# if not api_key:
#     print("Error: Missing Api Env")
#     exit(1)
# else:
#     print("API Key fnd.",api_key)


#---------------------------------WINDOWS_______________________

# result=os.system("Ping -n 3 google.com")
# if result== 0:
#     print("Ping Success ")
# else:
#     print("failed")



#_________________RANDOM________________

r.seed(10) 
print(f"Random int val in given range is : {r.randint(10,10000)}")

print(f"Random num bwn 0 and 1 is {r.random()}")


c=['apple','banana','grape', 'cherry', 'durian']
print(f"Random choice from the list is {r.choice(c)}")

r.shuffle(c)
print(c)