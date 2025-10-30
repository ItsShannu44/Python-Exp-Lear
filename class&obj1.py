class Dog:
    def __init__(self,name,breed, age):
        self.name=name
        self.breed=breed
        self.age=age
    
    def barks(self):
        print(f'The {self.name} barks.')
    
    def sleeps(self):
        print(f'The {self.name} sleeps all day.')

d1=Dog('Tom','pomeranian',5)
d2=Dog('Shiba','German Shepherd',8)

d1.barks()
d1.sleeps()