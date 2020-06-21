class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def Sit(self):
        print(self.name.title() + " is now sitting.")

    def Roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)

print("my dog's name is " + my_dog.name.title())
print("my dog is " + str(my_dog.age) + " years old")

# Accessing attributes 

my_dog.Sit()
my_dog.Roll_over()

#excercise

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    
    def Describe_restaurant(self):
        print("The restaurant's name is:{}".format(self.restaurant_name))
        print("The cuisine type is: {}".format(self.cuisine_type))
 
    
    def Open_restaurant(self):
        print("This restaurant is open")
    

restaurant = Restaurant("BarisFish&Chips","FastFood")
restaurant1 = Restaurant("cakesandshakes","Dessert")
restaurant2 = Restaurant("Marcos","fine dining")

print(restaurant.Describe_restaurant())
print(restaurant1.Describe_restaurant())
print(restaurant2.Describe_restaurant())

print(restaurant.Open_restaurant())

#User class - store information on users 

