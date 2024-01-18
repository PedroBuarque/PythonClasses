"""
Ask for the user to type his name
Ask for the user to type his age

If name and age were typed:
    Shows:
    Your name is {name}
    Your name backwards is {your name backwards}
    Your name has (or does not has) spaces
    Your name has {n} letters
    The first letter from your name is {letter}
    The last letter from your name is {letter}
if nothing was typed in name or age:
    shows:
    "Sorry, you left the fields empty"
"""

name = input('Type your name: ')
age = input('Type your age: ')

last_letter = len(name)

if name and age:
    print(f'Your name is {name}')
    print(f'Your name backwards is {name[::-1]}')
    if ' ' in name:
        print('Your name has spaces')
        print(f'Your name has {len(name) - 1} letters')
    else:
        print('Your name does not contains spaces')
        print(f'Your name has {len(name)} letters')
    print(f'The first letter in your name is {name[0]}')
    print(f'The last letter in your name is {name[len(name) - 1]}')
else:
    print('Sorry, you left empty fields')