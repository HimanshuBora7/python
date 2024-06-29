#9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
#Add an attribute called number_served with a default value of 0. Create an 
#instance called restaurant from this class. Print the number of customers the 
#restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number 
#of customers that have been served. Call this method with a new number and 
#print the value again.
# Add a method called increment_number_served() that lets you increment 
#the number of customers who’ve been served. Call this method with any num
#ber you like that could represent how many customers were served in, say, a 
#day of business.

#from 9-1
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbered_served = 0
    def describe_restaurant(self):
        print(f"name of this restaurant is {self.restaurant_name }and it serves {self.cuisine_type} ")
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

restaurant_1 = Restaurant("lowkey",'chinese')
restaurant_1.numbered_served = 10
print(f"restaurant_1 = {restaurant_1.restaurant_name} // cuisine = {restaurant_1.cuisine_type} // number of customers served = {restaurant_1.numbered_served}")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_1.check_customer_served()
restaurant_1.number_served(20)
restaurant_1.check_customer_served()
restaurant_1.increment_number_served(10)
restaurant_1.check_customer_served()




