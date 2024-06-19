#passsing a list to a function to make its working more efficient
def greet(names):
  """ this function gets list as its argument and this function aims to print individual grettings to each of the person mentioned in passed list """
  for name in names:
    msg = (f"Hello, {name.title()} !")
    print(msg)

usernames=['thor','odin','ragnar']

greet(usernames)

