#print patterns in python 

#this is a basic template for printing a square with n number of columns n rows
for i in range(5):
    for j in range(5):
     print("*",end=" ")
    print()
print("///////////////")
#now we will slightly modify this code to print a increasing triangle 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * * 

for i in range(5):
    for j in range(i+1):
      print("*",end=' ')
    print()

#now we will print triangle in decreasing order or decreasing triangle 
# * * * * * * 
# * * * * *
# * * * *
# * * *
# * *
# *
print("/////////////////////")
for i in range(5):
   for j in range(5-i):
    print("*",end=" ")
   print()
print("..........")
#print right sided triangle 
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# 
for i in range(6):
   a=6-i
   for j in range(1):         
    print(" "*a +"*"*i,end='')
   print()




      