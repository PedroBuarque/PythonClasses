#Precedence
# 1. (n + n)
# 2. **
# 3. * // %
# 4. + -
calculation_1 = 1 + 1 ** 5 + 5 # 7
print(calculation_1)

calculation_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) #1024
print(calculation_2)