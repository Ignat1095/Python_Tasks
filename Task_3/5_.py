# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def nega_fib(n):
    if n in (-1, 1, 2):
        return 1
    elif n == -2:
        return -1
    elif n <= 0:
        return nega_fib(n + 2) - nega_fib(n + 1) # ^ Отрицательная формула
    elif n > 0:
        return nega_fib(n - 1) + nega_fib(n - 2) # ^ Положительная формула

my_list = []

k = int(input("input integer: "))
for i in range(-k,k+1):
    my_list.append(nega_fib(i))

print(my_list)

# def fib(n): # ^ Положительный фиббоначи
#     if n in (-1, 1, 2):
#         return 1
#     elif n == -2:
#         return -1
#     else:
#         return fib(n - 1) + fib(n - 2)
# my_list = []

# k = int(input("input integer: "))
# for i in range(1,k+1):
#     my_list.append(fib(i))

# print(my_list)
