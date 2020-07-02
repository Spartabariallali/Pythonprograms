#lists
#manage data 
#access data
#add, remove data

# syntax variable = [] , () = tuple, dictionary {key:value} pairs
#tuples are immutable 

# guestlist = ["Muhammed Ali","Mike Tyson", "Tyson Fury","Don King"]
# print(guestlist[3])

# guestlist[3] = "Roy Jones jr" # replaced the data at index 3 with the new data

# print(guestlist) 

# guestlist.append("Vasyl lomachenko")
# guestlist.append("Don King")
# print(guestlist)

# guestlist.remove("Don King")
# print(guestlist)

# guestlist.pop()
# print(guestlist)

# guestlist.insert(4,"Vasyl Lomachenko")
# print(guestlist)


mix_type_string = [[1,2,3,], ["One","two","three"]]
print(mix_type_string)

string_list = ["One","two","three"]
int_list = [1,2,3,]

mixed_list = (string_list + int_list)
print(mixed_list)