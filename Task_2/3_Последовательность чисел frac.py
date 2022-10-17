# Задайте список из n чисел последовательности
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = (int(input("n = ")))

summ = 0
for i in range(1, n + 1):
    lst = [round(float(((1 + 1/i)**i)), 2)]
    summ += sum(lst)
    print(i, ":", lst, end=" ")
print('\n'"Сумма = ", summ)

# 2 вариант
# lst = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 2)}')
