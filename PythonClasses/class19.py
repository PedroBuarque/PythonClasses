#Operators in and not in
#Strings are iterables
#0 1 2 3 4 
#P e d r o
#-4 -3 -2 -1

#name = 'Pedro'
#print(name[3]) -> r
#print(name[-2]) -> r

#print('e' in name) -> True
#print('a' not in name) -> True
#print('a' in name) -> False
#print('e' not in name) -> False

name = input('Type your name: ')
find = input('Type what you want to find in you name: ')

if find in name:
    print(f'{find} is present in {name}')
else:
    print(f"{find} isn't present in {name}")
