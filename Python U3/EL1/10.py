class InvalidNumberError(Exception):
    pass

try:
    with open("nums.txt", "r") as f:
        for line in f:
            s = line.strip()
            if not s.isdigit():
                raise InvalidNumberError("Line contains letters: " + s)
            print(int(s))
except FileNotFoundError:
    print("nums.txt missing")
except InvalidNumberError as e:
    print(e)
