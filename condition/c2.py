#5-8. Hello Admin: Make a list of five or more usernames, including the name 
#admin'. Imagine you are writing code that will print a greeting to each user 
#after they log in to a website. Loop through the list, and print a greeting to 
#each user:
#•	If the username is 'admin', print a special greeting, such as Hello admin, 
#would you like to see a status report?
#•	Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
#logging in again.

user_name = ['thor','admin','stark','peter','robbisphere']

for invi in user_name:
    if invi.lower() == 'admin':
        print(f"helloe {invi},would u like to c a status report ? ")
    else:
        print(f"hello {invi},thank you for loggin in again")


# 5-10. Checking Usernames: Do the following to create a program that simulates 
#how websites ensure that everyone has a unique username.
#•	Make a list of five or more usernames called current_users.
#•	Make another list of five usernames called new_users. Make sure one or 
#two of the new usernames are also in the current_users list.
#•	Loop through the new_users list to see if each new username has already 
#been used. If it has, print a message that the person will need to enter a 
#new username. If a username has not been used, print a message saying 
#that the username is available.
#•	Make sure your comparison is case insensitive. If 'John' has been used, 
#'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
#current_users containing the lowercase versions of all existing users.
current_users = ['alpha','bravo','charlie','delta','India']
current_user = []
for x in current_users:
     current_user.append(x.lower())
print(current_user)
new_users = ['gamma','AlpHa','Bravo','Kilo','mike']
new_user =[]
for y in new_users:
     new_user.append(y.lower())
print(new_user)
flag = 0

for y in new_user:
    for x in current_user:
        if x == y:
            flag = 1
    if flag != 0:
        print(f"u can't take this name {y}")
        flag = 0
    else:
        print(f"u can take this name {y}")
            