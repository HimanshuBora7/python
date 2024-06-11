 #Let’s make a polling program in which each pass through the loop 
#prompts for the participant’s name and response. We’ll store the data we 
#gather in a dictionary, because we want to connect each response with a 
#particular user:

respose={}
polling = True

while polling:
    name = input("enter ur name ")
    reply = input("which country u wanna visit ? ")
    respose[name]=reply
    con = input("do u wanna retake poll for another person (yes/no)? ")
    if con == "no":
        polling=False
print("----polling--result----")
for x,y in respose.items():
    print(f"{x} wanna visit {y}")