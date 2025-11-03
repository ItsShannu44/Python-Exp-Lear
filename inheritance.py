class Laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
        self.battery_level=100

    def turn_on(self):
        print(f"{self.model} of {self.brand} is now turned ON.")
    
    def turn_off(self):
        print(f'{self.model} of {self.brand} is now turned OFF')

    def check_battery(self):
        print(f"The laptop has {self.battery_level}% battery remaining")
    
    def dec_battery(self,usage):
        if usage<0:
            print("Usage amt cannot be negative.")
        elif self.battery_level-usage<0:
            print("Battery is too low. Please charge the laptop")
        else:
            self.battery_level-=usage
            print(f"Battery decreased by {usage}%. Current Level: {self.battery_level}")

#child class
class GamingLaptop(Laptop):
    '''Inherits the attributes from the parent class laptop'''
    def __init__(self, brand, model, price, gpu , RAM):
        super().__init__(brand, model, price) #This is a call and not defination, self is taken from the child object that wants to be initialized.
        self.gpu=gpu
        self.RAM=RAM
        
    def boost_mode(self):
        print(f'{self.model} of {self.brand} is running in boost mode')
    
    '''Method Overriding from parent class'''
    def turn_on(self):
        super().turn_on()
        return (f'{self.model} of {self.brand}is starting in high gamig with{self.gpu}')

#Object Initialization
l1=Laptop('Dell','inspiron 15 3000', 55000)
gl1=GamingLaptop('Dell','G15',150000,'Nvidia RTX 4050',64)

#Parent Class usage 
l1.turn_on()
l1.check_battery()
l1.dec_battery(10)
l1.check_battery()

#Child class usage
gl1.turn_on()
gl1.check_battery()
gl1.boost_mode()
gl1.dec_battery(15)
gl1.check_battery()

