class Laptop:
    '''__inti__(): method gets called automatically when the object 
    has been created for this class, this function initializes the 
    values associated with the object
    self- represents the object and should be the first parameter'''
    def __init__(self, brand, model, price):
        self.brand=brand
        self.model=model
        self.price=price
    
    def turn_on(self):
        '''self represents the current obj that has called this method'''
        print(f'{self.model}of {self.brand} is now ON.')

    def specification(self):
        print(f'LAPTOP DETAILS \nBrand: {self.brand}\nPrice: Rs.{self.price}')
    
    def turn_off(self):
        print(f'{self.model} of {self.brand} is now OFF.')

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
