try:
    line=input("Enter the line")
    with open("file_2.txt","w") as f:
        f.write(line)
    print("Written Successfully.")
except PermissionError as p:
    print("Permission Error: The file cannot be Rewritable.")