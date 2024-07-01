#making simple rock paper scissor game

#importing library to make decision of computer random 

#import library shld be written on top 

import random

#defining functions 

def get_choice():
 player_choice = input("enter ur choice rock,paper,scissors\n")
 
 #options of computer choice will be stored in a list as list is a way to store multiple things in a single variable 
 #then we will randomize the choice of computer using random function 

 options = ["rock","paper","scissors"]
 
 computer_choice = random.choice(options)
 #using dictionary
 
 choice = {"player":player_choice,"computer":computer_choice}
 return choice

#defining a function to check who is the winner

def check_win(player,computer):
 print(f"u chose {player} and computer chose {computer}")

 if player ==  computer:
  return "its a tie"

 elif player == "rock" :
   if computer == "scissors":
     return "woah u smashed scissor with rock,u won"
   if computer == "paper":
     return "sadly u lost agaist a bot" 

 elif player == "paper" :
   if computer == "scissors":
     return "sedly u lost against a bot"
   if computer == "rock":
     return "woah u won " 

 elif player == "scissors" :
   if computer == "rock":
     return "u lost against a bot"
   if computer == "paper":
     return "woah u won "

choices = get_choice() 
result = check_win(choices["player"],choices["computer"])
print(result)