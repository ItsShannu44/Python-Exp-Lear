#----A dog has a name  and is of a particular breed and has an age. The dog barks and sleeps.
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

#----A car has a make model & year the car can be started and can be stopped. Every car has an initial reading of 0.
class Car:
    def __init__(self, model, year):
        self.model=model
        self.year=year
        self.reading=0

    def start(self):
        print(f'{self.model} of the year {self.year} is started')    

    def stop(self):
        print(f'{self.model} of the year {self.year} is stopped')
    
    def check_reading(self):
        print(f"The {self.model} of the year {self.year} has run {self.reading}km.")

c1=Car('urus','2022')
c2=Car('Dezire','2020')
c1.start()
c1.check_reading()
c2.stop()
