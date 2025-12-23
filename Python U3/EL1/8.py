clean = []
rejected = []

try:
    with open("expenses.txt", "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2:
                rejected.append(line)
                continue

            cat, amt = parts
            try:
                amt = float(amt)
                clean.append(line)
            except:
                rejected.append(line)

    with open("clean_expenses.txt", "w") as f:
        f.writelines(clean)

    with open("rejected_expenses.txt", "w") as f:
        f.writelines(rejected)

except FileNotFoundError:
    print("expenses.txt missing")
