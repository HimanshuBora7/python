#9-8. Privileges: Write a separate Privileges class. The class should have one 
#attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance 
#as an attribute in the Admin class. Create a new instance of Admin and use your 

#from exercise 9-7

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

#making admin class with user as its parent class 

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privlige = Privlige()

class Privlige:
    def __init__(self,privilegess =['1.can add post','2.can delete post','3.can ban user ']):
           #lisitng admins priviliges as attributes
        self.pri = privilegess
        
    def show_privileges(self):
         print(f"admin has following priviliges ")
         for x in self.pri:
          print(x)

user_03=Admin('chalie','lol')

user_03.greet_user()
user_03.privlige.show_privileges()