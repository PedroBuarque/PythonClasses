"""
Make a program that asks for the user to type a integer 
inform the user if this integer is a pair or a odd number.
If the user does not type a Integer, inform that the number is not a integer
"""
input = input('Type a integer: ')

try:
    input_int = int(input)
    pair = input_int % 2 == 0
    if pair:
        print(f'The number {input_int} is a pair')
    else:
        print(f'The number {input_int} is a odd')
except:
    print("You didn't typed a integer")