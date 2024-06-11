#using while loops with dictionaries and lists

#Consider a list of newly registered but unverified users of a website. After 
#we verify these users, how can we move them to a separate list of confirmed 
#users? 

verified_users=[]
unverified_users=['loki','thor','kilo','mike']

while unverified_users:
    current_user = unverified_users.pop()
    print(f"currnetly verying {current_user}")
    verified_users.append(current_user)
print("the following users are confirmed")
for verified_user in verified_users:
    print(verified_user)

#to remove a item from the list considering it is appearing many times using while loop 

pets = ['cat','dog','cat','cow']
print("list of the pets is as follows")
print(pets)
to_be_removed = input("what u want to remove from the above list ")

while to_be_removed in pets:
    pets.remove(to_be_removed)
print(pets)