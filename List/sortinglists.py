cars = ['bmw','audi','toyota','sabaru']
cars.sort()
print(cars) #sort() - alphabetical order 

cars.reverse() #reverses the order of the list 
print(cars)

#finding the length of a list 

cars = ['bmw','audi','toyota','subaru']

print(len(cars))


#looping through an entire list 

magicians = ['david','ollie','nathan']

for magician in magicians:
    print(magician)

favourite_pizza = ['Hot veggie','Chicken','peppoeroni','pineapple']

for pizza in favourite_pizza:
    print("My favourite pizza is {}".format(favourite_pizza[1]))
    print("my least favourite pizza is {}").format(favourite_pizza[3])

#using the range() function 

for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2)) #the range between 2-11, increment steps = 2
print(even_numbers)

squares = []
for value in range(1,11):
    sqaure = value ** 2
    squares.append(sqaure)
print(sqaure)

#excercises 

List = list(range(1, 20))
print(List)



