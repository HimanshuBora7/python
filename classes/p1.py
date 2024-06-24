#9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
#Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of 
#information, and a method called open_restaurant() that prints a message indi
#cating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attri
#butes individually, and then call both methods.

class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"name of this restaurant is {self.restaurant_name }and it serves {self.cuisine_type} ")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently opening ")

restaurant_1 = Restaurant("lowkey",'chinese')

print(f"restaurant_1 = {restaurant_1.restaurant_name} // cuisine = {restaurant_1.cuisine_type}")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

#9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
#different instances from the class, and call describe_restaurant() for each 
#instance.

restaurant_2=Restaurant("salmanca ","mexican")
restaurant_3=Restaurant("los pellos ","cuban")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()