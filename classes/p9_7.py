#9-7. Admin: An administrator is a special kind of user. Write a class called 
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
#or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
#of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of 
#privileges. Create an instance of Admin, and call your method

#from exercise 9-5 

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

    #lisitng admins priviliges as attributes
        self.privileges =['1.can add post','2.can delete post','3.can ban user ']
    def show_privileges(self):
        print(f"{self.first_name} { self.last_name} is admin n he has following priviliges ")
        for x in self.privileges:
            print(x)

user_07 = Admin('john',"d'souza ")
user_07.describe_user()
user_07.show_privileges()




