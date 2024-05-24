def factorial(n):
    """ this piece of code finds factorial of a 
number using recursion """
    if n==1 :
        return 1
    return n * factorial(n-1)

print(factorial(3))
print(help(factorial))