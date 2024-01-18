"""
String Slicing

0 1 2 3 4 5 6 7 8 9 10
Hello world
-11 10 9 8 7 6 5 4 3 2 1

Slicing [s:e:p] [::]

obs.: The function len returns the amount of characters of the str
"""

variable = 'Hello World'
print(variable[6]) #returns the letter 'W'
print(variable[-5]) #returns the letter 'W'
print(variable[4:]) #slices the string starting from the letter 'O' until the end of the string
print(variable[4:8]) #slices the string starting from the letter 'O' until the letter 'R'
print(variable[:8]) #slices the string starting from the beggining of the string until the letter 'R'
print((len(variable))) #returns the amount of characters on the string
print(variable[0:len(variable):2]) #returns the string but jumping 2 characters until the end of the string