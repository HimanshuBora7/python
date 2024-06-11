#4.3 counting to twenty 
#Use a for loop to print the numbers from 1 to 20,inclusive
for number in range(1,21):
    print(number)

#4-5. Summing a Million: Make a list of the numbers from one to one million, 
#and then use min() and max() to make sure your list actually starts at one and 
#ends at one million. Also, use the sum() function to see how quickly Python can 
#add a million numbers.

numbeers =[]
for number in range(1,100):
    numbeers.append(number)
print(numbeers)
print(min(numbeers))
print(max(numbeers))
print(sum(numbeers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a 
#list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_number=[]

for number in range(1,21,2):
 odd_number.append(number)

for num in odd_number:
 print(num)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
#print the numbers in your list.

three=[]
for tree in range(3,31,3):
   three.append(tree)

print(three)

#4-8. Cubes: A number raised to the third power is called a cube. For example, 
#the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
#is, the cube of each integer from 1 through 10), and use a for loop to print out 
#the value of each cube

cubes = []
for ice_cube in range(1,11):
   cubes.append(ice_cube**3)

for x in range(1,11):
   print(f"cube of {x} is {cubes[x-1]}") # wah kya code likha hai wah 

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
#first 10 cubes

cube = [value **3 for value in range(1,11)]
print(cube)

