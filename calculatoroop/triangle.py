from calc_functions import Python_Calcalutor

class Triangle(Python_Calcalutor):
    def area_of_triangle(half,number1,number2):
        half = 0.5
        return (half*(number1*number2))


triangle1 = Triangle()
print(triangle1.area_of_triangle(20,10))

print(triangle1.number_multiplier(20,2))




