# Задача №1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def FractionalConversion (num):
    value = num
    while value - int(value)!= 0:
        tail = num * 10
        num = tail
        value = tail
    num = int(abs(num))
    return(num)

def SizeVon (num):
    si = 1
    while num >= 9:
        num //= 10
        si += si
    return si

def SumNum (num, check):
    sum = 0
    for i in range(check):
        preserva = num
        division = preserva // 10
        remainder = num % 10
        sum = sum + remainder
        num = division
    return sum 
number = float(input('Введите вещественное число, чтобы определить сумму его цыфр: ')) # Почемуто, когда я вписываю цыфр больше пяти то выдаёт ошибку, говоря что: "не может преобразовать строку в число с плавующей запятой" Обесните пожалуйста что не так?
real = number

number = FractionalConversion (number)
size = SizeVon (number)
answer = int(SumNum(number, size))

print(f'Сумма цыфр числа {real} = {answer}.')
