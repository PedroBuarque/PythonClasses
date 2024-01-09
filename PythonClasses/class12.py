#String formatation -> .format()

a = 'A'
b = 'B'
c = 1.1
format = 'a={} b={} c={:.2f}'.format(a, b, c)
format2 = 'b={1} a={0} c={2:.2f}'.format(a, b, c)
format3 = 'b={name2} c={name3:.2f} c={name1}'.format(name1 = a, name2 =b, name3 = c)

print(format)
print(format2)
print(format3)