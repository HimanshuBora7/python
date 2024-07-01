#-13. Dice: Make a class Die with one attribute called sides, which has a default 
#value of 6. Write a method called roll_die() that prints a random number 
#between 1 and the number of sides the die has. Make a 6-sided die and roll it 
#10 times.
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.
from random import choice
class Die:
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self):
        side = list(range(1,self.sides+1))
         
        print(choice(side))



user_01 = Die(6)
for x in range(0,10):
 user_01.roll_die()
user_2 = Die(20)
for y in range(0,10):
   user_2.roll_die()