#create a variable called - first_name and last_name
first_name = input("what is your first name? ")
last_name = input("what is your last name? ")
#create a variable called full_name
full_name = (first_name + ' ' + last_name)
# display full_name
print(full_name)
# create a variable called age
user_age = int(input("what is your age? "))
# prompt the user for this information
print("the user's name is {} and they are {} year's old".format(full_name,user_age))