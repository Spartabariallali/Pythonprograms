from animalone import Animal
from mammals import Big_Cats

class Lion(Big_Cats):
    def __init__(self,name,species,breathing=True,hunt=True,mood="happy",climbing_ability=True,hunter="female",mane=True,pride=0):
        super().__init__(name,species,breathing=True,hunt=True)
        self.hunter = hunter
        self.mane = mane
        self.pride = pride 
    
    def go_for_hunt(self):
        if self.hunter == "female" and self.pride > 3:
            print(self.name + " the female" + self.species + " is out on a hunt")
        elif self.hunter == "male" and self.pride > 3:
            print(self.name + " is protecting the pride")
    
    def protect_pride(self):
        if self.mane == True and self.pride > 3:
            print(self.name + "is protecting the pride")
        if self.mane == False and self.pride < 3:
            print(self.name + "is a young" + self.species + "finding his way in the wild")

lion_three = Lion("Scar","lion",breathing=True,hunt=True,mood=True,climbing_ability=True,hunter="female",mane=True,pride = 4)

lion_three.go_for_hunt()
lion_three.protect_pride()
lion_three.protect_prey()
lion_three.roar()