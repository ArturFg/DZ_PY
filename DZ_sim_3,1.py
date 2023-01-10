# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []
storage = int(input('Set the size of the array: '))
odd = 0
for i in range(storage):
    my_list.append(random.randint(1, 9))
print(my_list)
for i in range(storage):
    if i % 2 != 0:
        odd += my_list[i]
print(f'Sum of odd element -> {odd}.')



