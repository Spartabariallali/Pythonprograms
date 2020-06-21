#ice cream stand 

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
    
    def set_number_served(self,)

restaurant = Restaurant("BarisFish&Chips","FastFood",90)
restaurant1 = Restaurant("cakesandshakes","Dessert",120)
restaurant2 = Restaurant("Marcos","fine dining",89)

print(restaurant.Describe_restaurant())
print(restaurant1.Describe_restaurant())
print(restaurant2.Describe_restaurant())

print(restaurant.Open_restaurant())