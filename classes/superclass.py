#making parent class and super class 
class Car:
    """ representing information about a car """
    def __init__(self,make,model,year):
      self.make=make
      self.model=model
      self.year=year
      self.odometer_reading = 0
    
    def get_descriptive_name(self):
       long_name=f"{self.model} {self.make} {self.year} "
       return long_name.title()
    
    def read_odometer(self):
       print(f"this car has {self.odometer_reading} miles on it ")

    def update_odometer(self,mileage):
       if self.odometer_reading < mileage:
          self.odometer_reading=mileage
       else:
          print("u can' roll back an odometer ")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

#  defining a child class from parent class

class Electric_Car(Car):
   """represent aspect of a car ,specific to electric car """
   def __init__(self,make,model,year):
      super().__init__(make,model,year)    

my_tesla = Electric_Car('tesla','model s ','2019')
print(my_tesla.get_descriptive_name())   


