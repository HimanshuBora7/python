#simple function for greeting the user
name = input("enter ur name ")
def greetings(username):
    print(f"hello {username} welcome !! ")
greetings(name)

#the previous example ws of positional argument

#example of keyboard argument is as follows

#taking input from the users
def pet_info(pet,name):
 print(f"{name} is a {pet}")

pett= input("what kind of pet do u have ")
pet_name = input("enter ur pet name ")

pet_info(pet=pett,name=pet_name)