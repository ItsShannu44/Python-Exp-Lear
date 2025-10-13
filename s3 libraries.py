import os
print("The current working directory.",os.getcwd())

new="Directory"
os.mkdir(new)
# os.rmdir("Directory")

if os.path.exists(new):
    print(f'Directory{new} is created successfully.')
else:
    print("error in creation.")

os.chdir(new)
print("current dir",os.getcwd())

os.mkdir("dir1")
os.mkdir("dir2")

path1="D:\Github\Python Exp Lear"
path2="D:\Github\Python Exp Lear\Directory"

pth=os.path.join(path1,path2)

print("Path is:",pth)

# if os.path.exists(pth):
#     print(f'{pth}is correct')

if os.path.isdir(pth):
    print(f'{pth} points to dir')
else:
    print("Do not point to dir")



# -------

path="D:/Github/Python Exp Lear/test.txt"
if os.path.isfile(path):
    sts=os.stat(path)
    print(f"File size in bytes :{sts.st_size}")
else:
    print(f"{path} is not correct")
