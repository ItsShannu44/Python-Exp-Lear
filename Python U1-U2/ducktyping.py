class Dog:
    def walk(self):
        print("I have 4 legs and can walk")
class Emu:
    def walk(self):
        print("I have 2 legs and can walk")
class Parrot:
    def fly(self):
        print("I have wings and can fly")
def walk(a):
    a.walk()

Dog().walk()
Emu().walk()
walk(Dog())
walk(Emu())
# walk(Parrot())   ----ERROR
