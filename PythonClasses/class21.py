"""
Basic String formatting

s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(character)(><^)(amount)
> - Left
< - Right
^ - Center
Signal - + or -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variable = 'ABC'
print(f'{variable}')
print(f'{variable:0>10}') #fill the variable with 10 times the digit 0 to the left
print(f'{variable:<10}') #fill the variable with 10 times the digit ' ' to the right
print(f'{1000.4554645:.3f}') #prints the number with 3 decimal spaces
print(f'The hexadecimal from 1500 is {1500:08X}') #prints the hexadecimal for the number 1500