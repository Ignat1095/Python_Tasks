# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N. (делят число нацело)

from os import sep


number = int(input("Введите целое число: "))
n = number
i = 2
my_list = list()

while i <= n:
    if n % i == 0:
        my_list.append(i)
        n //= i
        i = 2
    else:
        i += 1

print("Простые множители: ", number, '=', end=" ")
print(*my_list, sep="*")

exit()
number = int(input("input an integer: "))  # ^ Целые числа
a = b = 0
for a in range(number//2+1):
    for b in range(a+1):
        while number == a * b:
            print(number, "=", a, "*", b)
            a += 1
