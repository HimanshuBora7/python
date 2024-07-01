def factorial(n):
    """ this piece of code finds factorial of a 
number using recursion """
    if n==1 :
        return 1
    return n * factorial(n-1)
x = int (input("enter the number of which u wanna find factorial: "))
print(f"the factorial of the entered number {x} is {factorial(x)}")
