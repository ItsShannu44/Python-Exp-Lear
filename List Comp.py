#_________Simple Comprehension____________
# Simple Comprehension  [<expr for <variable> in <iterate>]

# CREATE AN EMPTY LIST
# EXECUTE THE FOR PART OF THE LIST COMPREHENSION

# Conditional list comprehension
# new_list = [exprehension for variable in iterable if condition == True]




#__________Simple Comprehension______________



l=[a for a in range(10)]
print(l)


l=[a*2 for a in range(10)]
print(l)

#____________Conditional Coprehension________________

l=[a*a for a in range(10) if a%2==0]
print(l)


#____________Nested Comprehension__________________

l=[a*b for a in range(1,5) for b in range(1,3)]
print(l)