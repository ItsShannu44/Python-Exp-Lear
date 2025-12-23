valid = []
try:
    with open("numbers.txt", "r") as f:
        for line in f:
            try:
                valid.append(int(line.strip()))
            except:
                print("Invalid:", line.strip())

    with open("clean_numbers.txt", "w") as f:
        for n in valid:
            f.write(str(n) + "\n")

except FileNotFoundError:
    print("numbers.txt not found")
