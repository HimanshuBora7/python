#polymorphism is a way to generalize the functanailty so it can work on diffn types
"""In summary, polymorphism in Python allows you to write more flexible code by using the same method names across different 
classes or objects while adapting their behavior as needed! """

class dog:
    def eat(Self):
        print("dog is eating dog food!\n")
class cat:
    def eat(self):
        print("cat is eating is its cat food\n")


animal1 = dog()
animal2 = cat()

animal1.eat()
animal2.eat()

