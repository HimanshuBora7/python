#making some arguments optional 

def get_formatted_name(first_name,last_name,middle_name=None):
    if middle_name :
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

name = get_formatted_name('john','lee')
print(name.title())
name = get_formatted_name("mukesh","singh",'kumar')
print(name.title())

#returing a dictionary from the function 
def build_person(first_name,last_name):
    """ this function returns a dictionary which consist of the information about the person """
    person={'first name':first_name,'last name':last_name}
    return person

first=input("enter the first name ")
last=input("enter the last name ")

person=build_person(first,last)
for x,y in person.items():
    print(x,y)
print(help(build_person))
print(person)
