try:
    with open("new_file.txt","r") as f:
        lines=f.readlines()
        if not lines:
            print("The file is empty..")
        else:
            for line in lines[:5]:
                print(line.strip())
except FileNotFoundError:
    print("File Not found.")