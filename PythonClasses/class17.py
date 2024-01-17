#Logic operators 2
#or -> Any condition that is True evaluetes the expression as True. Which means if any value is considered True, all the expression will be True.

login_logout = input('Log [In] Log [Out]: [In/Out] ')
typed_password = input('Password: ')

correct_password = '123456'
if (login_logout == 'In' or login_logout == 'in') and typed_password == correct_password:
    print('You logged in to the system')
elif (login_logout == 'In' or login_logout == 'in') and typed_password != correct_password:
    print('Your password is incorrect')
elif (login_logout == 'Out' or login_logout == 'out') and typed_password == correct_password:
    print('You logged out from the system')
else:
    print('You logged out from the system')