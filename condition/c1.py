#5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif
#else chain.
#•	If the alien is green, print a message that the player earned 5 points.
#•	If the alien is yellow, print a message that the player earned 10 points.
# •	If the alien is red, print a message that the player earned 15 points.
# •	Write three versions of this program, making sure each message is printed 
#for the appropriate color alien.

alien_colour = input("enter the colour of the alien:\n")

if alien_colour.lower() == 'green':
    print("u earned 5 points")
elif alien_colour.lower() == 'yellow':
    print("u earned 10 points")
elif alien_colour.lower() == 'red':
    print("u earned 15 points")
else:
    print("point for this particular is not found , fck off ")
