#working with list 

dogs =["loki",1,"leopard"]

#we can use 'in' method to check if the desired content is in list or not 
print(1 in dogs)
#we can also define an empty list 


#printing a value from the list

print(dogs[2])
#we can same notation to update an object in the list
dogs[2] = 'german shepard'

print(dogs[2])

#we can use append method to add new object in the list 
dogs.append("street")

#we can also use extend method to add numeber of objects to our list 
dogs.extend(["husky","rotviller"]) 

#we can replace append with += also
dogs+=(['uiop','007'])

#removing an item using remove method

dogs.remove("uiop")

#we can remove using pop method also ,last object will be popped 

dogs.pop()

#we can use slicing also to print whole list 

print(dogs[:])
 
