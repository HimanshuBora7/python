from functools import reduce #to use reduce function 
#using map(),filter(),reduce()

#using map()

numbers = [1,2,3]

def double(a):
    return a*2

result = map(double,numbers)

print(list(result))

#another way of doing the same piece of code using lamda function 

num = [4,5,6]

res = map(lambda a:a*3,num)

print(list(res))

#using fliter()

numb = [1,2,3,4,5,6,7,8,9,]

resu = filter(lambda n:n%2 != 0,numb) #odd numbers will be printed 

print(list(resu))

#using reduce method 

expenses = [("dinner",80),("car repair",1000)]

sum = reduce(lambda a,b:a[1] + b[1],expenses)

print(sum)