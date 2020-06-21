def greet_users(names):
    """Print a simple gretting to each user in the list."""

    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

#modifying a list within the body of a function 

unprinted_designs = ['iphone case','robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
print("Printing model: " + current_design)

completed_models.append(current_design)

print("the following models have been printed:")
for completed_model in completed_models:
    print(completed_models)

#excercise 

#magicians 

magicians = ['magician1','magician2','magician3']

def show_magicians():
    print(magicians)

def make_great(magicians):
    for magician in magicians:
        print("The great " + magician)

make_great(magicians)