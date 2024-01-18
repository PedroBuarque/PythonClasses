"""
Introduction to the basics of try/except

try -> tries to execute the code
except -> a error ocurred when trying to execute the code

"""
number_str = input('I will double the number that you type here: ') 

try:
    print(f'STR: {number_str}')
    number_int= int(number_str)
    print(f'INT: {number_int}')
    print(f'The double of {number_str} is {number_int * 2}')
except:
    print('Thats not a number')

#if the user types something different from a number, instead of poping a exception it will go to the except part of the code