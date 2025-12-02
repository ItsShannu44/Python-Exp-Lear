def is_even(n):
    if n%2==0:
        return n
    
l=list(filter(is_even,range(20)))
print(l)

l=list(filter(lambda x: x%2==0, range(20)))
print(l)

#__________________REDUCE()________________
# reduce(callable, iterable)
#------------EX--sum of numbers---------

from functools import reduce
l=reduce(lambda a,b:a+b, [1,2,3,4,5,6,7,8,9,10])
print(l)

#__________________zip()___________________
# zip(iterables.......)

print(list(zip([1,2,3,4,5],['a','b','c','d','e'])))
print(list(zip([1,2,3,4,5],['a','b','c','d','e'],[0.0,1.0,2.0,4.0,5.0])))
print(list(zip([1,2,3,4,5,6,7,8,9,10],['a','b','c','d','e'])))

#_________________Max()____________________

print(max('a','A','aa','AA')) #values type should be same except complex
print(max([1,2,3,4],[1,2,3,5],[1,2,6,7],[1,2,6]))

#_________________Min()_______________________
print(min('a','A','aa','AA')) #values type should be same except complex
print(min([1,2,3,4],[1,2,3,5],[1,2,6,7],[1,2,6]))

#________________operator____________________

import operator as o
print(o.add(10,20))

#sub(), truediv(), floordiv(), mul(), add(), gt(), ge(),le(), eq(), ne(), mod(), or_, and_, not_, xor


