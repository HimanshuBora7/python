#10-4. Guest Book: Write a while loop that prompts users for their name. When 
#they enter their name, print a greeting to the screen and add a line recording 
#their visit in a file called guest_book.txt. Make sure each entry appears on a 
#new line in the file.
from datetime import datetime
choice = True
while choice == True:
    name = input("enter ur name ")
    date_n_time_of_visit = datetime.now()
    
    with open('guest_book.txt','+a') as file_object:
        file_object.write(f"guest_name = {name}\ntime of visit = {date_n_time_of_visit}\n")
    opti = input("to quit type q ")
    if opti == "q":
        choice  = False



