first_value = input('Type a value: ')
second_value = input('Type another value: ')

int_first_value = int(first_value)
int_second_value = int(second_value)

if int_first_value > int_second_value:
    print(f'The first_value={int_first_value} is greater than the second_value={int_second_value}')
elif int_first_value < int_second_value:
    print(f'The second_value = {int_second_value} is greater than the first_value = {int_first_value}')
elif int_first_value == int_second_value:
    print(f'The two values are equals')