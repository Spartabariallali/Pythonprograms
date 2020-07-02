# control flow  - statements and loops

# if, elif, else, for loop, while loop 

# and - two conditions need to be true
# or - only one conditions needs to be true 

weather = "sunny"
conditional_weather = "rain"

# if weather == "snow" and conditional_weather == "rain": use and when two conditions need to be true
#     print("dont go to the beach")
# else: 
#     print("no ice cream")

if weather == "snow" or conditional_weather == "rain": # use or when one condition needs to be true
    print("dont go to the beach")
else: 
    print("no ice cream") 


age = 18 

if age == 18 or age > 18: # if age >= 18:
    print("welcome to the this movie")
else:
    print("you are not legal age to watch this movie")


# write a U, PG13, 15, 18 

#write a program to check these conditions by getting user input

#if age <= 17 = cant watch 18 movies or above 

# if age 12 < less cant watch PG 13 or above movies 

#display messages accordingly 

age = input("how old are you? ")

if age <= 17 
    print("you cannot watch over 18s movie")
elif age >= 13 and age <=17:
    print("you can watch ")