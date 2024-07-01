#-14. Lottery: Make a list or tuple containing a series of 10 numbers and 
#five letters. Randomly select four numbers or letters from the list and print a 
#message saying that any ticket matching these four numbers or letters wins a 
#prize.
#-15. Lottery Analysis: You can use a loop to see how hard it might be to win 
#the kind of lottery you just modeled. Make a list or tuple called my_ticket. 
#Write a loop that keeps pulling numbers until your ticket wins. Print a message 
#reporting how many times the loop had to run to give you a winning ticket.

from random import choices
list_1 =['p','i']
list_1+=range(1,3)
print(list_1)
choi = choices(list_1,k=2)

winning_combo=['p','i']

flag=0
while True:
    choi = choices(list_1,k=2)
    print(choi)
    flag+=1
    if choi == winning_combo:
        break
print(f"it took {flag} number of turns to match combo")
print(choi)
