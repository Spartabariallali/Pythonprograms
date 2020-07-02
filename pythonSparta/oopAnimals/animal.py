class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
       
    def breathe(self):
        print("breahting")
    
    def eat(self):
        print("eating")
       
    def sleeping(self):
        print("sleeping")
        
    def moving(self):
        print("moving")
       
    
lion_one = Animal("Mufasa","Lion")
lion_one.breathe
lion_one.eat
lion_one.sleeping
lion_one.moving