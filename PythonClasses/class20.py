#Basic String Interpolation
#s -> string
#d and i -> int
#f -> float
#x and X -> Hexadecimal (ABCDEF0123456789)

name = 'Pedro'
price = 100.985
variable = '%s, the price is R$%.2f' % (name, price)
print(variable)
print('The hexadecimal from %d is %04X' % (1500, 1500))
