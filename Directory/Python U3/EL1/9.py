try:
    while True:
        print("\n1. Search\n2. Add Contact\n3. Exit")
        c = input("Enter choice: ")

        if c == "1":
            try:
                name = input("Enter name: ")
                with open("contacts.txt", "r") as f:
                    matches = [l.strip() for l in f if name.lower() in l.lower()]
                print("Found:", *matches) if matches else print("Not found")
            except FileNotFoundError:
                print("contacts.txt missing")

        elif c == "2":
            try:
                with open("contacts.txt", "a") as f:
                    f.write(input("Name & number: ") + "\n")
                print("Added")
            except:
                print("Write error")

        elif c == "3":
            break

        else:
            print("Invalid choice")
except:
    print("Error")

