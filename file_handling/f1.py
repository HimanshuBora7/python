#writing in a file
from datetime import datetime
filename = 'initial_line.txt'

with open(filename,'w') as file_object:
    file_object.write("I am learning programming")
    file_object.write("\ntill now I have completed C n now I am doing python ")

print(datetime.now())