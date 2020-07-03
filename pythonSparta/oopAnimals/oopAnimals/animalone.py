class Animal:
    def __init__(self,name,species,breathing=True,hunt=True):
        self.name = name
        self.species = species
        self.breathing = breathing
        self.hunt = hunt
# a function that outputs the name and species of the animal    
    def describe_animal(self):
        print(self.name + " is a " + self.species)
# a function that outputs whether the lion is breathing        
    def breathe(self):
        if self.breathing == True:
            print(self.name + " is breathing")
        elif self.breathing == False:
            print(self.name + " is dead")
# a function that outputs the whether lion is eating or hungry    
    def eat(self):
        if self.hunt == True:
            print(self.name + " is eating")
        elif self.hunt == False:
            print(self.name + " is getting hungry")
# a function that outputs whether the lion is hunting or playing       
    def moving(self):
        if self.hunt == True:
            print(self.name + " is moving closer to the prey")
        elif self.hunt == False:
            print(self.name + "chasing female lions")
# a function that outputs whether the lion is awake or sleeping  
    def sleeping(self):
        if self.hunt == True:
            print(self.name + " is sleeping after a big hunt")
        elif self.hunt == False:
            print(self.name  + " cannot sleep because he is hungry")

    
        
    
lion_one = Animal("Mufasa","Lion",breathing=True,hunt=True)
lion_one.describe_animal()
lion_one.breathe()
lion_one.moving()
lion_one.eat()
lion_one.sleeping()
