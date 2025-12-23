try:
    filename = "names.txt"
    search = input("Enter name to search: ")
    
    with open(filename, "r") as f:
        names = [n.strip() for n in f]

    if search in names:
        print("Name found")
    else:
        print("Name not found")

except FileNotFoundError:
    print("Names file missing")
