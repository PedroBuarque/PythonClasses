"""
Make a program that asks for the user his first name. If the name has 4 letters or less prints "You have a short name"; 
if it has between 5 and 6 letters, prints "You have a normal name";
if it has more than 6 letters prints "You have a big name".
"""

input = input("Type your name: ")
name_range = len(input)

if name_range <= 4:
    print("You have a short name")
elif name_range >= 5 and name_range < 7:
    print("You have a normal name")
elif name_range > 6:
    print("You have a big name")