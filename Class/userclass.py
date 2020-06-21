class UserInformation():

    def __init__(self,first_name, last_name,age,location,occupation):
        self.first_name = first_name 
        self.last_name = last_name 
        self.location = location
        self.age = age
        self.occupation = occupation
    
    def Describe_user(self):
        print("Information about the User: ")
        print("- {}".format(first_name))
        print("- {}".format(last_name))
        print("- {}".format(age))
        print("- {}".format(location))
        print("- {}".format(occupation))
    
    
    def Greet_user(self):
        print("Hello {} {}, you are currently {} years old.".format(first_name,last_name,age))
        print("You currently live in {} and your job title is {}".format(location,occupation))

    user = UserInformation('bari','allali','24','Essex','DevOps')
  
    print(user.Describe_user())
    print(user.Greet_user())