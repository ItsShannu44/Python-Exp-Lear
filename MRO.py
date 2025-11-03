class Root:
    def do(self):
        print('Root.do (completed)')

#Inherited classes
class A(Root):
    def do(self):
        print('A.do')
        super().do()

class B(A):
    def do(self):
        print('B.do')
        super().do()

class C(A):
    def do(self):
        print('C.do')
        super().do()

class D(B, C):
    pass

class E(C,B):
    pass

D().do()

print('MRO of class D:',[cls.__name__ for cls in D.mro()])
print('MRO of class E:',[cls.__name__ for cls in E.mro()])
print(D.__mro__)
print(E.__mro__)