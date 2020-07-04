# phase 1 - create a simple calculator

class Python_Calcalutor:
# should have add, divide,multiply,subtract and remainder   
    def number_subtraction(number1,number2):
        return (number1 - number2)

    def number_division(number1,number2):
        return (number1/number2)

    def number_remainder(number1,number2):
        if (number1 % number2) == 0:
            return True
        elif (number1 % number2) != 0:
           return False
       
    def number_multiplier(number1,number2):
        return (number1*number2) 
    
    def cm_to_inches():
        mode = float(input(
            "Enter 1 for inches to cm: \nEnter 2 for cm to inches: "))  # user input for which conversion they want
        if mode == 1:
            inches = float(input("how many inches? "))
            return print(inches * 2.54)
        elif mode == 2:
            cm = float(input("how many cm? "))
            return print(cm / 2.54)

calc1 = Python_Calcalutor

print(calc1.number_multiplier(3,4))
print(calc1.number_remainder(20,7))
# calc1.cm_to_inches()



