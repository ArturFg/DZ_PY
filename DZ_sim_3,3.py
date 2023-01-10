# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []

for _ in range(5):
    index = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), 2))

print(my_list)
m_ax = 0
m_in = my_list[0]

for i in range(len(my_list)):
    f = int(my_list[i])
    r = my_list[i]
    r -= f
    if r > m_ax:
        m_ax = r
    if r < m_in:
        m_in = r

difference = m_ax - m_in
print(round(m_ax, 2))
print(m_in)
print(round(difference, 3))
