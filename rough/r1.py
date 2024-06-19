#trying to copy a list by slicing method 

x=["lol","sup","hell yeah  "]
y=x[:]
print(x)
print(y)
print("removing some item from original list that is x")
x.pop()
print(f"x -> {x}")
print(f"y-> {y}")