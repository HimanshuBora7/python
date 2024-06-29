#getting sqaure of a number by oo approcach

class Number:

    def __init__(self, value):
        self.value=value

    def getsqaure(self):
        x=(int(self.value) * int( self.value))
        return x
    def find_sqaure(self):
        y = self.getsqaure()
        return y

num=Number(input("enter the number of which u wanna get sqaure "))
print(f"sqaure of {num.value} is {num.find_sqaure()}")