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

#____________Nested Conditional Comprehension___________

l=[a*b for a in range(10) for b in range(5) if (a+b)%2==0]
print(l)



#======================SET=================

#______________Simple Comprehension___________________

s={a for a in [1,2,3,4,5]}
print(s)

#____________Conditional Coprehension________________

s={a+2 for a in range(10) if a%2!=0}
print(s)


#____________Nested Comprehension__________________

s={(a,b) for a in [1,2,3,4,5] for b in ['a','b','c']}
print(s)


#____________Nested Conditional Comprehension___________
s={(a,b) for a in [1,2,3,4] for b in [4,5] if(a+b)%2==0}
print(s)

