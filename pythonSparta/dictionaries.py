# dictionary contains key:value pairs 
# stores connection between pieces of information 
# syntax - use {} to create a dictionary 
# {"cities":"London"} - example of key:value pair 


student_record = {
    "Name":"Bari Allali",
    "course_name":"DevOps",
    "completed_lessons":5,
    "completed_lessons_name":["strings","tuples","variables"]
    }


for record in student_record:
    print(record) # prints out all keys 

for values in student_record.values():
    print(values)


# print(student_record)

# print(type(student_record)) 

# print(sorted(student_record)) #returns the keys 
# print(student_record.values()) # retuns the values 

# completed = student_record["completed_lessons"] = 5

# print(completed)


# #add lists and built in methods 

# student_record["completed_lessons_names"] = "dictionaries", "lists", "operators"
# mod_list = student_record["completed_lessons_names"]
# print(mod_list)

# student_record["completed_lessons_name"].append("lists")
# student_record["completed_lessons_name"].append("dictionaries")

# print(student_record)

# print(student_record["completed_lessons_name"][1])

# print(student_record["completed_lessons_name"][2]) #variables

# print(student_record["Name"]) # value of name









