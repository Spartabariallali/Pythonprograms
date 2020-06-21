""" A simple attmept to make a car"""

class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    #setting a default value for an attribute 
        self.odometer_reading = 0

    def get_description(self):
        """return neatly formatted descriptive name"""
        long_name = str(self.year )+ ':' + self.make + ':' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("this car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self,mileage):
        """update the reading of the odometer to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you cant roll back an odometer")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_used_car = Car('subaru','outback','2013')
print(my_used_car.get_description())

my_used_car.update_odometer(23500)
my_used_car.read_odometer

my_new_car = Car('audi','a4','2016')
print(my_new_car.get_description())
my_new_car.update_odometer(9)
my_new_car.read_odometer()


#excercises 


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type,number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    
    
    def Describe_restaurant(self):
        print("The restaurant's name is:{}".format(self.restaurant_name))
        print("The cuisine type is: {}".format(self.cuisine_type))
        print("This restaurant serves {} customers on average per day".format(self.number_served))
 
    
    def Open_restaurant(self):
        print("This restaurant is open")
    

restaurant = Restaurant("BarisFish&Chips","FastFood",90)
restaurant1 = Restaurant("cakesandshakes","Dessert",120)
restaurant2 = Restaurant("Marcos","fine dining",89)

print(restaurant.Describe_restaurant())
print(restaurant1.Describe_restaurant())
print(restaurant2.Describe_restaurant())

print(restaurant.Open_restaurant())




