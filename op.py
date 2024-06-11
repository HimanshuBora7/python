#operator overloading is a way to compare two objects 
class dog:
    def __init__(self,name,age):
     self.name = name
     self.age = age

    def __gt__ (self,other):
       return True if self.age > other.age else  False

roger = dog("roger",8)
syd = dog("syd",6)

print(roger > syd)