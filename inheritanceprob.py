#class car having the attribute  of model and year and has the methods of drive, stop, read the odometer and update.
#Create an electric car that has the attribute battery and has the methods read battery or check battery and also displays  how much time before a recharge.

class car:
    def __init__(self,model,year):
        self.model=model
        self.year=year
        self.odometer=0
        self.battery=100
    
    def drive(self):
        print(f"{self.model} of year{self.year} is in drive mode.")

    def stop(self):
        print(f"{self.model} of year{self.year} is in stop mode.")
    
    def update_odometer(self, read):
        if read<=0:
            print("The Odometer reading must be positive")
        else:
            self.odometer+=read
            print(f"The reading of the car{self.model} is {self.odometer}")

class electric(car):
    def __init__(self,model, year, battery,time):
        super().__init__(model, year)
        self.battery=battery
        self.time=time

    def read_battery(self):
        print(f"The battery {self.battery}% left ")




d1=car('Swift',2020)
d2=car('800',2012)

d1.drive()
d1.update_odometer(59)
d1.stop()
