class NegativeMarkError(Exception): pass
class HighMarkError(Exception): pass

valid = []

try:
    for line in open("stud_marks.txt"):
        try:
            m = int(line)
            if m < 0:  raise NegativeMarkError
            if m > 100: raise HighMarkError
            valid.append(m)
        except NegativeMarkError:
            print("Negative:", line.strip())
        except HighMarkError:
            print("Above 100:", line.strip())

    with open("clean_marks.txt", "w") as f:
        f.writelines(str(m) + "\n" for m in valid)

except FileNotFoundError:
    print("stud_marks.txt missing")
 