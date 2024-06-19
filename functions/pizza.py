#creating module to be imported in some other file
def make_pizza(size,*toppings):
    """summarise the pizza we are about to make"""
    print(f"making a {size} - inch piza with the following toppings:")
    for topping in  toppings:
        print(f" - {topping}")