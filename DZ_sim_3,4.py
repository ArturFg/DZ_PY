# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal = int(input('Write down the decimal number: '))
my_list = []

if decimal % 2 == 0:
    while decimal != 0:
        remainder = decimal % 2
        decimal //= 2
        my_list.append(remainder)
    #my_list.append(decimal)
else:
    while decimal != 1:
        remainder = decimal % 2
        decimal //= 2
        my_list.append(remainder)
    #my_list.append(decimal)

print(my_list)

new_list = []
r = len(new_list)

for i in range(len(my_list) + 1):
    new_list.append(my_list[r])
    r -= 1
print(*new_list)

# Я не понел как мне сделать просто двухзначное число, а не лист.
# Так же иногда массив переворачивается правельно, а иногда нет. Я непонел с чем связана эта ошибка.

