# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


a = list(map(int, input()))
print(sum(a))

exit()

number = (input("input mumber: "))
sum = 0
for i in number:
    sum += int(i)
print("sum = ", sum)


# def sum(n): # Рекурсией
#     if n < 10:
#         return n
#     return n % 10 + sum(n // 10)
# print(sum(int(input("number = "))))
