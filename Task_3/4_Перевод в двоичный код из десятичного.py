# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101

# number = int(input("Введите число"))
number = 61
count = ""
while number > 0:
    count = str(number % 2) + count
    number = number // 2
print(count)


n = bin(61)  # ^ Встроенная  функция
print(n[2:])


def bin(x):  # ^ Через функцию
    count = ""
    while x > 0:
        count = str(x % 2) + count
        x = x // 2
    return count
print(bin(61))
