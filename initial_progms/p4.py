#wap to compare three numbers and print the largest one 

a = int(input("enter the first number\n"))
b = int(input("enter the second number\n"))
c = int(input("enter the third number\n"))
print("%d is greater among the entered values (%d %d %d)"%(a,a,b,c)) if( a > b and a > c) else (print("%d is greater than among the entered values(%d %d %d)"%(b,a,b,c) if ( b > c and b> a) else (print("%d is greates among the entered values (%d %d %d )"%(c,a,b,c)))))

#bitwise left shift operater

e = 5<<3
print(e)
#bithwise right shift operater
f = 13>>3
print(f)