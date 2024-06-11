#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
#text of a message that should be printed on the shirt. The function should print 
#a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
#function a second time using keyword arguments.

def make_shirt(size='large',text='I lob pyhton '):
  print(f"the size of the shirt ordered by you is {size} and the text to be printed on the shirt is '{text}'")


#calling function using positional argument
make_shirt('M',"lived another day ")
#calling function using keyword argument
make_shirt(text="chilling",size="Xl")
#Make a large shirt and a medium shirt with the default message
make_shirt('L')
make_shirt("M")
make_shirt("s","screw the world")