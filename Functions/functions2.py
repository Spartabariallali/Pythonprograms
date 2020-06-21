def get_formatted_name(first_name,last_name):
    """Return full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name("jimi","hendrix")
print(musician)

def get_formatted_name1(first_name,middle_name,last_name):
    full_name1 = first_name + ' ' + middle_name + ' ' + last_name
    return full_name1.title()
musician2 = get_formatted_name1('john','lee','parker')
print(musician2)

def get_formatted_name2(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name2('jimi','hendrix')
musician = get_formatted_name2('john','lee','hooker')

#returning a dictionary 

def build_person(first_name,last_name):
    """return a dictionary about a person"""
    person = {'first': first_name, 'last': last_name}
    return person 

musician = build_person('jimi','hendrix')
print(musician)



#excercises 

#city Names 

def city_country(city,country):
    """print city,country in that format"""
    print(city +  ','  + country)

city_country("London", "United Kingdom")
city_country('Pari','Framce')
city_country('Madrid','Spain')

#Album 

#write a function make_album
#build dictionary describing a music album
#the function should take an artist name and an album title
#and should return a dictionary describing these two pieces of information
#use the function to make three dictionaries representing different albumbs 
#print each return value to show that the dictionaries are storing the album information correctly 

def make_album(artist_name, album):
    music = {'artist': artist_name, 'album_name': album}
    return music 

album1 = make_album("Kendrick Lamar","GoodKidMaddCity")
album2 = make_album("Drake","Take Care")
album3 = make_album("The Weeknd", "Triology")

print(album1)
print(album2)
print(album3)





