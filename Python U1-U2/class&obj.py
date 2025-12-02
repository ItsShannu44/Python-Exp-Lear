class Laptop:
    '''__inti__(): method gets called automatically when the object 
    has been created for this class, this function initializes the 
    values associated with the object
    self- represents the object and should be the first parameter'''
    def __init__(self, brand, model, price=25000):
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level=100 #____initial battery level
    
    def turn_on(self):
        '''self represents the current obj that has called this method'''
        print(f'{self.model}of {self.brand} is now ON.')

    def specification(self):
        print(f'LAPTOP DETAILS \nBrand: {self.brand}\nPrice: Rs.{self.price}')
    
    def turn_off(self):
        print(f'{self.model} of {self.brand} is now OFF.')

    def check_battery(self):
        print(f'This laptop has {self.battery_level}% battery life..')

    def update_battery_status(self,val):
        if 0<=val<=100:
            self.battery_level=val
            print(f'battery level of {self.model}, {self.brand} is updated to {self.battery_level}')
        else:
            print('Invalid battery level!! pls enter a val between 0-100')
    
    def decrease_battery(self, usage):
        if usage<0:
            print('Usage amount cannot be negative. ')
        elif self.battery_level-usage<=0:
            print('battery level is too low! Please change the laptop')
            self.battery_level=0
        else:
            self.battery_level=self.battery_level-usage
            print(f'battery decreased by {usage}%./Current level: {self.battery_level}%')

print(type(Laptop),id(Laptop))
#___________OBJ CREATION________________
l1=Laptop('Dell','Inspiron 15',60000)
l2=Laptop('Asus','Tuf f15', 75000)
print(type(l1),id(l2),type(2), id(2))

l3=Laptop(25900,'HP','pavilian')
# l4=Laptop( ,  )
l4=Laptop(price=200, model='pavilian', brand='HP')

#__________Accessing the data members in a object____________
print(l1.brand, l1.model, l1.price)
print(l2.brand, l2.model, l2.price)
print(f'I own a {l2.model} of {l1.brand} that costs Rs. {l1.price}')


#___________Accessing methods through objects_________________
l1.turn_on()
l2.specification()


print(l1.brand, l1.model, l1.price, l1.battery_level)
l2.check_battery()

#-----------Modification of attribute values once the obj has been created

#______1.Change the value directly using the object

l1.battery_level=90
l1.check_battery()

#_______2. Use a mothod that sets a value each time the method is called
# l2=Laptop('Asus','Tuf f15', 75000)
l2.turn_on()
l2.update_battery_status(20)
l2.check_battery()

#_______3. Increment or decrement an attribute using a method

l3.turn_on()
l3.decrease_battery(10)

l4.turn_on()
l4.decrease_battery(100)
l4.check_battery()