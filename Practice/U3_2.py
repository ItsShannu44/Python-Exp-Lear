#A program converts user input into an integer. Handle invalid inputs such as alphabetic  strings and sym

def convert_to_int():
    try:
        n = int(input("Enter a number: "))
        print("Converted integer is:", n)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

convert_to_int()
