from collections import defaultdict

n = int(input("Enter number of words: "))

anagrams = defaultdict(list)

for _ in range(n):
    word = input().strip()
    key = ''.join(sorted(word)) 
    anagrams[key].append(word)

for group in anagrams.values():
    if len(group) >= 3:
        print(group)
