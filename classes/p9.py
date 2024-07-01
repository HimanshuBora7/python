#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
#a class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
#the class will work; just pick the one you like better. Add an attribute called 
#flavors that stores a list of ice cream flavors. Write a method that displays 
#these flavors. Create an instance of IceCreamStand, and call this method

#from 9-1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbered_served = 0
    def describe_restaurant(self):
        if self.cuisine_type != '':
         print(f"name of this restaurant is {self.restaurant_name } and it serves {self.cuisine_type} ")
        else:
           print(f"name of this restaurant is {self.restaurant_name } ") 
    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently opening ")
    #method to set number of customers served 
    def number_served(self,number):
        self.numbered_served = number

    def check_customer_served(self):
        print(f"customer served = {self.numbered_served}")
    #method to increment number of customer served 

    def increment_number_served(self,num):
        self.numbered_served+=num

class Ice_cream_stand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavor=['vanila','choclate','strawberry']

    def list_falavor(self):
        """this method displays all the flavor available"""
        print(f"we have following flavours:")
        for x in self.flavor[:]:
            print(f"{x}")


iceCreamstand_1=Ice_cream_stand("cold ice cream ",'')

iceCreamstand_1.list_falavor()
iceCreamstand_1.describe_restaurant()





