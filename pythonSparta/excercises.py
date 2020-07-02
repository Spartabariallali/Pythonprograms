# create a dictionary with employee records (minimum 5 key:value pairs)
employee_records = {
    "Name":"Bari Allali",
    "position":"sales represenatative",
    "salary":35000,
    "location":"London",
    "driving_license":"yes"
    }
# using loop iterate through the loop
for key, value in employee_records.items():
    print(key,value)

# display the values of only the keys in the dictionary
for records in employee_records:
    print(records)

viewer_age = int(input("how old are you? "))

if viewer_age >= 18:
    print("you can watch all movies")
elif viewer_age == 17:
    print("you cannot watch over 18 movies")
elif viewer_age == 15 and viewer_age <=17:
    print("you can watch watch 15 and over")
elif viewer_age == 13 and viewer_age <=14:
    print("you can watch PG 13 movies")
elif viewer_age <= 12:
    print("you cant watch PG 13 movies, only Universal movies")