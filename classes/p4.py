#9-5. Login Attempts: Add an attribute called login_attempts to your User 
#class from Exercise 9-3 (page 162). Write a method called increment_login 
#_attempts() that increments the value of login_attempts by 1. Write another 
#method called reset_login_attempts() that resets the value of login_attempts 
#to 0.
# Make an instance of the User class and call increment_login_attempts() 
#several times. Print the value of login_attempts to make sure it was incremented 
#properly, and then call reset_login_attempts(). Print login_attempts again to 
#make sure it was reset to 0.

#from exercise 9-2 

class User:
    def __init__ (self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0 
    
    def describe_user(self):
        print(f"first name of the user is {self.first_name} and his last name is {self.last_name}")
    def greet_user(self):
        print(f" hello {self.first_name} {self.last_name} greetings !! ")
    def increment_login_attempt(self):
        self.login_attempts+=1
    def reset_login_attempt(self):
        self.login_attempts=0



user_1=User("walter","white")
user_2=User("soul","goodman")

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3=User("gus","fring")
print(f"{user_3.greet_user()}")
print(f"{user_3.login_attempts}")
user_3.increment_login_attempt()
print(f"{user_3.login_attempts}")
user_3.increment_login_attempt()
user_3.increment_login_attempt()
user_3.increment_login_attempt()
print(f"{user_3.login_attempts}")
user_3.reset_login_attempt()
print(f"{user_3.login_attempts}")