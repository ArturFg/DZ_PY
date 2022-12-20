# Задача №2
# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

print('Введите число: ')
n = int(input()) # Я почемуто не могу в input писать слова.
arryi = []
size = 1
sum = 0
for i in range(n):
    si = size
    si = float((1 + 1/si)**si)
    arryi.append(round(si, 2))
    sum = sum + si
    size = size + 1
print(f'n = {n} -> {arryi}')
print(f'Сумма чисела массива = {round(sum, 2)}')