from animalone import Animal

class Big_Cats(Animal):
    def __init__(self,name,species,breathing=True,hunt=True,mood="happy",climbing_ability=True): #add additional arguments
        super().__init__(name,species,breathing=True,hunt=True) # contains attributes of parent class
        self.mood = mood
        self.climbing_ability = climbing_ability # initialise any additional attributes specific to the subclass 

    def roar(self):
        if self.mood == "happy":
            print(self.name + " is purring")
        elif self.mood != "happy":
            print(self.name + " is Roaringgg")
    
    def play_fighting(self):
        if self.mood == "happy":
            print(self.name + " is play fighting")
        elif self.mood != "happy":
            print(self.name + " is ready to kill. Be careful")
    
    def protect_prey(self):
        if self.climbing_ability == True:
            print(self.name + " is in a tree, with his prey")
        elif self.climbing_ability == False:
            print(self.name + " is eating his prey on the ground")
    
    def hunting(self):
        if self.mood != "happy" and self.climbing_ability == True:
            print("The " + self.species + " is ready to hunt")
        elif self.mood == "happy" and self.climbing_ability == True:
            print("Eventhough the " + self.species + " has the ability to climb he is not in the mood to hunt")
    



lion_two = Big_Cats("Diego","Jaguar",breathing=True,hunt=True,mood="sad",climbing_ability=True)

lion_two.roar()
lion_two.play_fighting()
lion_two.hunting()
lion_two.protect_prey()

