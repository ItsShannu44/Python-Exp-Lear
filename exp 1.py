from collections import Counter

string="Hey!! Good Morning.everyone"

freq=Counter(string)
print("Chars with count greater than 2:")

for char in freq:
    count=freq[char]
    
    if count>2:
        print(f"The character {char} appears {count} times.")