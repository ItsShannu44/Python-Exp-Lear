def is_even(n):
    if n%2==0:
        return n
    
l=list(filter(is_even,range(20)))
print(l)
