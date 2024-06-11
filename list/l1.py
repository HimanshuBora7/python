motorcycle = ['honda','yamaha','ducati','suzuki']

#ways to insert element 

#1.Append method (it appends at the last of the element)
print(motorcycle)
motorcycle.append("maruti")
print(motorcycle)
#2.to add element at particular location we use insert method
motorcycle.insert(3,"martin baker")
print(motorcycle)


#ways to delete the items from the list 

#1.to delete from an element from a specific location we use del statement 

del motorcycle[3]
print(motorcycle)

#2.If we want to use the removed value we have pop method by default it removes the last element from the list
deleted_motorcycle = motorcycle.pop()
print(f"last deleted motorcycle is {deleted_motorcycle}")

#3 to delete a element from a specified location and to use its value we can use pop(position) method 

most_expensive = motorcycle.pop(3)

print(f"excluding the most expensive bike {most_expensive} from the list")
print(motorcycle)

#4REmoving an item by value

motorcycle.remove("ducati")
print(motorcycle)