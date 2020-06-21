#passing and artbitrary amount of arguments 

def make_pizza(*toppings):
    for topping in toppings:
        print('-' + topping)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

make_pizza