#guess list 

guestlist = ['Muhammed Ali','Mike Tyson', 'Tyson Fury','Don King']
print("{} was the greatest ever.".format(guestlist[0]))
print("{} was the youngest ever World Heavy Weight Champion at just 19.".format(guestlist[1]))
print("{} is the current Undisputed World Heavy Weight champion.".format(guestlist[2]))

print("{} cannot attend the dinner".format(guestlist[3]))

remove_list = guestlist.remove('Don King')

print("the following are all still attending: ")
print(guestlist)
print("In place of Don King, we have invited Floyd Mayweather")

update_list = guestlist.append('Floyd Mayweather')

print("The new guest list looks as follows:")
print(guestlist)

print("we have successfully managed to upgrade to a bigger table and therefore have the capacity to include three more guest")
guestlist.insert(0,'Roy Jones Jr')
guestlist.insert(3,'Saul Canelo Alvarez')
guestlist.append('Deontay Wilder')
print("The three new guest are: Roy Jones Jr, Saul Canelo Alvarez and Deontay Wilder")

print(guestlist)

print("due to unforeseen circumstances we can only have 2 guest speakers")
guestlist.pop(-1)
guestlist.pop(1)
guestlist.pop(2)
guestlist.pop(3)
print(guestlist)

del guestlist[1]
print(guestlist)



