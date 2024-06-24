#modelling a class dog with  name and age as two piece of information and sitting and barking as behaviour

class Dog:
    """a simple attempt to model a dog """
    def __init__(self,name,age):
        """initializing name and age attributes """
        self.name = name
        self.age = age
    def sit(self):
        """simulate a dog to sit when given command"""
        print(f"{self.name} is sittting ")
    def rollover(self):
        """simulate a dog to do rollover in response to a command """
        print(f"{self.name} is now rolling over in response to ur command ")

#making an instance representing a specific dog:
my_dog = Dog("charlie",3)
print(f"my dog's name is {my_dog.name}")
print(f"age of my dog is {my_dog.age}")
my_dog.rollover()
my_dog.sit()
#creating multiple instances

your_dog=Dog("willey",4)

print(f"my dogs name is {my_dog.name} and he is {my_dog.age} year old")
my_dog.sit()
print(f"your dog's name is {your_dog.name} and he is {your_dog.age} year old")
your_dog.sit()