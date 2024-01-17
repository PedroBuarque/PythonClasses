#Logic operators 1
#and -> all the conditions must be True

login_logout = input('Log [In] Log [Out]: [In/Out] ')
typed_password = input('Password: ')

correct_password = '123456'
if login_logout == 'In' and typed_password == correct_password:
    print('You logged in to the system')
elif login_logout == 'In' and typed_password != correct_password:
    print('Your password is incorrect')
else:
    print('You logged out from the system')