#Logic operators 3
#not -> Used to invert the expressions
#not True = False
#not False = True

senha = input('Senha: ')

if not senha:
    print('You didnt typed your password')
elif senha != '123456':
    print('This password is incorrect')
elif senha == '123456':
    print('You logged in')