# Tuples - same as lists but they are immutable 

# tuples cant be modified 

# should be used when data cannot be manipulated 

# tuples are declared by ()

date_of_birth = ("name","dob","passport number")
print(date_of_birth)

#convert the tuple into a string
#add your name into the list at 0 index 

dob = list(date_of_birth)
print(dob)

dob.insert(0,"bari allali")
print(dob)

