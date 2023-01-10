# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

my_list = []
storage = int(input('Set the size of the array: '))

for i in range(storage):
    my_list.append(random.randint(1, 9))

print(my_list)

if storage % 2 != 0:
    divide_by_two = (storage // 2) + 1
else:
    divide_by_two = (storage // 2)

to_decrease = storage - 1
new_list = []


for i in range(divide_by_two):
    f = 0
    f = my_list[i] * my_list[to_decrease]
    new_list.append(f)
    to_decrease -= 1

print(new_list)




