#String formatation -> f-strings

name = 'Pedro' + ' ' + 'Buarque'
height = 1.75
weight = 76
cmi = weight / (height ** 2)

line_1 = f'{name} has the height of {height:.2f} meters'
line_2 = f'his weight is {weight} kilograms and his MCI is: {cmi:.2f}'
print(line_1)
print(line_2)