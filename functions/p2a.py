# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
#Write a function called send_messages() that prints each text message and 
#moves each message to a new list called sent_messages as it’s printed. After 
#calling the function, print both of your lists to make sure the messages were 
#moved correctly.

message=['yo','sup','hell yeah']
x=[]
x=message[:]
def show_message(msg):
    for mes in msg:
        print(mes)
show_message(message)
sent_message=[]
def send_message(meesagee,sent_messagee):
 while meesagee:
    current = meesagee.pop()
    print(f"current message : {current}")
    sent_messagee.append(current)

send_message(x,sent_message)
print("//checking both the list//")
print(x)
print(sent_message)

# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the 
#function send_messages() with a copy of the list of messages. After calling the 
#function, print both of your lists to show that the original list has retained its 
#messages.

print("**")
print(x)
print('**')

send_message(x,sent_message)

print("//checking if our original list is maintained or not ")
print(message)
print(sent_message)