#Working with the basics of conditionals
#if/elif/else

condition = input("Do you wanna 'login' or 'logout'?")

if condition == 'login':
    print('You logged into the system')
elif condition == 'logout':
    print('You logged out from the system')
else:
    print("You didn't type any of the available options")