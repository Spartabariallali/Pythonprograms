from animalone import Animal

class Big_Cats(Animal):
    def __init__(self,name,species,breathing=True,hunt=True,mood="happy",climbing_ability=True): #add additional arguments
        super().__init__(name,species,breathing=True,hunt=True)
        self.mood = mood
        self.climbing_ability = climbing_ability # contains attributes of parent class

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
    



lion_two = Big_Cats("Diego","Jaguar",breathing=True,hunt=True,mood="sad",climbing_ability=True)

lion_two.roar()
lion_two.protect_prey()
lion_two.play_fighting()


