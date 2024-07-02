class Calculator:
    def __init__ (self,x,y):
        self.x=int(x)
        self.y=int(y)
        self.z = 0
    def add(self):
        self.z = self.x + self.y
        return self.z
        
    def sub(self):
        z=self.x-self.y
        return z
    
    
choice = True
while (choice == True):
    x=input("enter the first number: ")
    y=input("enter the second number:")
    calci_01 = Calculator(x,y)
    print("what u wanna do with these two number ? ")
    option = int(input("enter 1. ADDITION\t2.SUbtraction "))
    if option == 1:
     result = calci_01.add()
     print(result)

    choice = input("do u want to continue ")
    if choice == "y":
        choice = True
    else:
        choice = False
