# import os

# dir=os.getcwd()
# print(dir)

# for ls in os.scandir():
#     print(ls)

try:
    with open("file.txt",'r')as f:
        print("file found")
except FileNotFoundError as e:
    print(f"FileNotFound: {e}")