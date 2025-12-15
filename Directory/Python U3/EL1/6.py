valid = []
try:
    with open("marks.txt", "r") as f:
        for line in f:
            try:
                m = int(line.strip())
                valid.append(m)
            except ValueError:
                print("Invalid mark:", line.strip())

    print("Total:", sum(valid))
    print("Average:", sum(valid) / len(valid))

except FileNotFoundError:
    print("marks.txt not found")
    