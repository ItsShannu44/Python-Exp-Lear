#------------Create a list of all uppercase words from a given list.

words = ["shannu", 'vaibhav', 'shridhar']
up_list = [word.upper() for word in words]
print(up_list)

#-----------Given a list of words, create a list with words that start with a vowel.

words = ["shannu", "eat", "cat", 'owl', 'new']
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_start_words = [word for word in words if word[0].lower() in vowels]
print(vowel_start_words)

#----------Given a list of strings, create a new list that contains the string and its length.
strings = ['apple', 'banana', 'cherry', 'date']
string_lengths = [(s, len(s)) for s in strings]
print(string_lengths)

#----------Extract all lowercase letters from a string into a set.
input_string = "Hello World! This is a Test String 123."
lowercase_letters = {char for char in input_string if char.islower()}   
print(lowercase_letters)

#----------Given a sentence , create a set of all words that have more than 4 chars.
sentence = "This is an example sentence for creating a set of words"
words = sentence.split()
long_words = {word for word in words if len(word) > 4}
print(long_words)

#---------Create a set of first letters of each word in a given paragraph.
paragraph = "This is a sample paragraph to demonstrate set comprehension in Python."
words = paragraph.split()   
first_letters = {word[0] for word in words}
print(first_letters)

#--------Given a string create a dictionary of each character with its frequency.
input_string = "hello world"
char_frequency = {char: input_string.count(char) for char in set(input_string)}
print(char_frequency)


