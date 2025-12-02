l=[1,2,3,4,5]
l_iter=iter(l)
print(l_iter)

print(next(l_iter))
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())


# n=1234567
# n_iter=iter(n)  ---Typ err


str='Python Prg'
s_iter= iter(str)
print(type(str),type(s_iter))

# s={1,2,3,4,5}
# st_iter=iter(s)



t=(1,2,3,4,5)
t_iter=iter(t)
print(type(t), type(t_iter))


d={1:2,3:4,5:6,7:8,9:8}
d_iter=iter(d)
print(type(d),type(d_iter))


import itertools as it
seq=it.chain(['A','B','C','D','E','F','G','H'])
seq_iter=iter(seq)
for _ in range(5):
    print(next(seq_iter),end=" ") 

for _ in range(3):
    print(next(seq))


#_______________StopIteration___________________

s={1,2,3,5,6}
s_iter=iter(s)
try:
    while True:
        print(next(s_iter))
except StopIteration:
    print('Completed')



