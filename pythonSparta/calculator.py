# creating a class
# class defines the behavior of an object and the kind of information an object can store
# the information in a class is stored in attributes and functions that belong to a class are called methods
# a child class inherits the attributes and methods from its parent class

# create a basic calculator
class Python_Calcalutor():
# should have add, divide,multiply,subtract and remainder   
    def number_subtraction(number1,number2):
        return (number1 - number2)

    def number_division(number1,number2):
        return (number1/number2)

    def number_remainder(number1,number2):
        return (number1 % number2)

    def number_multiplier(number1,number2):
        return (number1*number2) 

# create an object of the class / run the class

number1 = int(input("please choose any number: "))
number2 = int(input("please choose any second number: "))

calc_obj = Python_Calcalutor

print(calc_obj.number_subtraction(number1,number2))

print(calc_obj.number_multiplier(number1,number2))






