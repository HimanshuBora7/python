#a simple calcualtor to do basic calculations    
class Calculator:
    def __init__ (self,x,y):
     self.x= int (x)
     self.y=int (y)
        
    def add(self):
        p = self.x + self.y
        return (p)
    def sub(self):
        p= self.x - self.y
        return p 
    def multi(self):
        p = self.x * self.y     
        return p
    def div(self):
        if self.y == 0:
          p = "can't perform divion"
          return p
        else:  
         p = self.x / self.y
         return p   
        
choice = True
while (choice == True):
    x=input("enter the first number: ")
    y=input("enter the second number:")
    
    calci_01 = Calculator(x,y)
    choi = True
    while (choi == True):

    
     print("what u wanna do with these two number ? ")
     option = int(input("enter 1. ADDITION\t2.SUbtraction\t3.Multiplication\t4.Division "))

     if option == 1:
      op_to_be_perfored = 'addition'
      result = calci_01.add()
     elif option == 2:
      op_to_be_perfored = 'subtraction'
      result = calci_01.sub()
     elif option == 3:
      op_to_be_perfored = 'multiplication'
      result = calci_01.multi()
     elif option == 4:
      op_to_be_perfored = 'division'
      result = calci_01.div()
     else:
      op_to_be_perfored = 'no operation performed due to error'
      result = print("error")
     print(f" !! calculation done !!\n result is {result}")
     file_name = "history_of_calci.txt"
     with open("history_of_calci.txt","+a") as file_object:
       file_object.write(f"two numbers entered = {x},{y}\noperation performed ={op_to_be_perfored}\nresult = {result}\n\n ")

     print("enter 1> to continue calculation with this result 2> to start fresh calculation 3> exit ")
     choi = int(input("enter ur choice "))
     if choi == 1:
      x = result
      y = input("enter the 2nd number ")
      calci_01 = Calculator(x,y)
      continue
     elif choi == 2:
      choi == False
     else:
      choice = False
      break


