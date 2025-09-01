# checking username 
# we take usernames from the user and check if it exists in our database 
# if it exists we do not allow it 

newuser = [];




while True:
 username = input("Enter ur username: ").strip()

 if any(existing_user.lower() == username.lower for existing_user in newuser):
  print(f"Error: Username '{username}' is already taken ")
 else:
  newuser.append(username)
  print(f"Success: Username '{username}' added successfully")

