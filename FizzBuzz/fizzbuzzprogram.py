# write a program that prints the numbers from 1 to 100
# but for multiples of three print "fizz" instead of the number
#  for multiples of 5 print fizz 
# for numbers that are multiples of both print FizzBuzz 


for number in range(1,101):
    if number % 3 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)
 

class FizzBuzz:
    def fizzbuzz_counter(self):
        for number in range(1,101):
            if number % 3 and number % 5 == 0:
                print("fizzbuzz")
            elif number % 5 == 0:
                print("buzz")
            elif number % 3 == 0:
                print("fizz")
            else:
                print(number)


fizzbuzz1 = FizzBuzz()

fizzbuzz1.fizzbuzz_counter()



       






