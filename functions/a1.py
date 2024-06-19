#passing arbiatery number of arguments to a function 

def build_profile(first,last,**user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info
    """building a dictionary which takes evrything"""

user_profile=build_profile("albert",'kumar ',education='princeton',field='physcics')

print(user_profile)
print(help(user_profile))