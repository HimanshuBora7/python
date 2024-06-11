#Cities: Make a dictionary called cities. Use the names of three cities as 
#keys in your dictionary. Create a dictionary of information about each city and 
#include the country that the city is in, its approximate population, and one fact 
#about that city. The keys for each city’s dictionary should be something like 
#country, population, and fact. Print the name of each city and all of the infor
#mation you have stored about it.

cities={"Mumbai":{"country":"INDIA","population":"1.6cr","facts":"financial capital"},
        "paris":{"country":"FRAnce","population":"4.6cr","facts":"French revolution"},
        
        }

for key,value in cities.items():
    print(key,value)
age = int (input("wnter ur age "))
age+=10
print(age)

car = input("what kind of car u want? ")

print(f"let me c if I can find u a {car} ")