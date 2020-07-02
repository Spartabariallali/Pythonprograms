# # data types and operators 
# # strings and casting
# # concatenation
# # single quotes vs double quotes 


# # checking the values as Boolean output(True/False)

# x = 10
# y = 11
 
# print(x == y) #False
# print(x > y)  #False
# print(x < y)  #True
# print(x != y) #True

# age = 18 
# print(age < 19)

# print( 3 % 9) #modular returns the left over value after division 

# #Double quotes VS single quotes 

# print("hello world") #double quotes is best practise 
# print('hello world')

# #single quotations can return error when using apostrophes 
# #print('bari's class is eng 67')  
# #double quotes remove the error
# print("bari's class is eng 67")
# #using \ \ is a method to use apostrophes
# print('bari\'s class is eng 67')


# #Strings, Indexing, Casting, Slicing and concatenation 

# greeting = ("hello")
# print(greeting)

# # indexing 

# print(len(greeting))

# #concatenation
# welcome_user = input("please enter your name: ")
# print(welcome_user)
# print(greeting + ' ' + welcome_user)

# hi = "hello world"

# print(len(hi))

# print(hi[-1])

# for i in hi:
#     print(i)

# print(hi[6:11])
# print(hi[-11:-6]) 
# print(hi[-6:-1])



# #strip removes the space at the end of a string 

# remove_white_space = "strip removes the space at the end of a string"
# print(len(remove_white_space))

# print(len(remove_white_space.strip()))



#boolean values within DATA types

use_text = "here's SOME text with lots of texts"
#count() - counts the substring within the string 

print(use_text.count("t"))

print(use_text.lower())

print(use_text.upper())

print(use_text.capitalize())

print(use_text.title())

#replacing text in the string 
print(use_text.replace("text","jargon"))









