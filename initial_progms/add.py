#user friendly program to add two numbers
a = int (input("enter the first number"))
b = int (input("enter the second number"))
c = a+b
print("addition of two number is",c)
c = a*b
print("multiplication of two number is", c)
c = a/b
print("division of %d and %d is %f"%(a,b,c))
print(type(c))
#to know data type of any variable there is a function type to know
print(type(a))
#simple division in python returns float value 
d =15/2
print(d)
#so to get only integer part of the answer we use floor division operator
e = 15//2
print(e)
