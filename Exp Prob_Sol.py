#______________Craete a list of all uopercase words form a given list.___________

words=["shannu",'vaibhav','shridhar']
up_list=[word.upper() for word in words ]
print(up_list)


#_______________Given a list of words, create a list with words that start with a vowel.__________

words = ["shannu", "vaibhav", "shridhar"]
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_start_words = [word for word in words if word[0].lower() in vowels]
print(vowel_start_words)

