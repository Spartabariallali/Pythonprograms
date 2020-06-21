class NormalCar():
    
    def __init__(self, make, model,year):
        self.make = make 
        self.model = model
        self.year = year 
        self.odometer_reading = 0

    def descriptive_name(self):
        long_name = str(self.year) + ' ' +  self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("this car has " + str(self.odometer_reading)+ "miles on it")

    def update(self, mileage):
        if mileage >= self.read_odometer:
            self.odometer_reading = mileage
        else:
            print("you can roll back an odometer")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    
class ElectricCar(NormalCar):
    
    def __init__(self, make, model, year):
        super().__init__()
        self.battery_size = 70
    
    def describe_battery(self):
        print("this car has " + str(self.battery_size) + "-kwh battery.")

            


my_tesla = ElectricCar('telsa','model s', '2016')
print(my_tesla.descriptive_name())
my_tesla.describe_battery()


