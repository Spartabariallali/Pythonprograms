def greet_user():
    pass
    """ Display a message greeting user"""
    print("hello!")

greet_user()

def greet_user1(username):
    pass
    """ Display a greeting to the username"""
    print("hello"  +  username.title()  +  "!")

greet_user1("bari")

def favourite_book(title):
    pass
    """should return favourite book"""
    print("my favourite book is {}".format(title))

favourite_book("Alice in Wonderland")

#posistional arguements

def describe_pet(animal_type, pet_name):
    pass
    """display information about a pet"""
    print("I have a {}.".format(animal_type))
    print("my {}'s name is {}".format(animal_type,pet_name))

describe_pet("cat","jeffrey")

#keyword arguments

def describe_pet1(animal_type, pet_name):
    print("I have a {}".format(animal_type))
    print("my {}'s name is {}".format(animal_type,pet_name))

describe_pet1(animal_type="hamster",pet_name="todd")


def make_tshirt1(size,message):
    pass
    print("the size of the shirt is {}".format(size))
    print("the message on the  t-shirt = {}".format(message))

make_tshirt1(size="medium",message="YOLO")


#city function 
def describe_city(name_of_city, country):
    """print city name and country of origin"""
    print("The city is called {}".format(name_of_city))
    print("{} is located in the United Kingdon".format(name_of_city,country))

describe_city("London","United Kingdom")



