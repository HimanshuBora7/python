#working with calsses and objects \

class NCA:
   def who(self):
      print("they r cricketers\n")


class student(NCA):
    def __init__(self,name,age):
      self.name = name
      self.age = age

    def profession(self):
       print("they are ipl players  \n")
       
rohit = student("rohit",35)
kohli = student("kohli",18)

print(rohit.name)
rohit.profession
print(rohit.age)
print(kohli.name)
print(kohli.age)
kohli.profession()
kohli.who()