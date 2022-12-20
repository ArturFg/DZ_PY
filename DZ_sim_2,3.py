# Задача №3
# Реализуйте алгоритм перемешивания списка

print('Впишите любые числа ниже.')
arryi = []
for i in range(5):
    arryi.append(int(input())) # Почемуто у меня неработает функция рандом. Поэтопу только так...
print(arryi)
s = arryi[0]
d = arryi[4]
arryi[0] = d
arryi[4] = s
s = arryi[1]
d = arryi[3]
arryi[1] = d
arryi[3] = s
s = arryi[2]
d = arryi[4]
arryi[2] = d
arryi[4] = s
print(arryi)