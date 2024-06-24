#making a class car storing information 

class Car:
    """representing a car """
    def __init__ (self,make,model,year):
        """initializing attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """returns a neatly formatted descriptive name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """print a statement showing car's mileage """
        print(f"this car has {self.odometer_reading} miles on it ")
    #making method to update odometer reading
    def update_odometer(self,mileage):
        """set the odometer reading to the given value """
        """adding extra bit of code to prevent from rolling back odometer reading """
        if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
        else:
         print("u can't role back its value ")
    #making method to increment or decrement a attributes value 
    def modify_odometer(self,mileage):
       self.odometer_reading+=mileage
    
my_new_car = Car("mercedes","q4","2014")

print(my_new_car.get_descriptive_name())
print(my_new_car.read_odometer())

#modifying attributes value 
#to modify a attribues value we have three ways 1.directly through an instance 2.set the value through  a method 3.increment the value through method

#first method -> changing attribute value through instance
my_new_car.odometer_reading = 23
#2nd method is to change attributes value by making a method
my_new_car.read_odometer()
my_new_car.update_odometer(32)
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.read_odometer()
 
#3rd method of changing an attribute value is by incrementing it or decrementing it with the help of method 
my_new_car.modify_odometer(30)
my_new_car.read_odometer()