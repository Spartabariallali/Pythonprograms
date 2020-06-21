class Dog():
    """A simple attempt to model a dog"""

    def __init__(self,name,age):
        """initilise name and age attributes"""
        self.name = name 
        self.age = age 

    def sit(self):
        """Simulate a dog sitting down"""
        print(self.name.title() + " is now sitting")
    
    def roll_over(self):
        """Simulate a dog rolling over"""
        print(self.name.title() + " rolled over")
