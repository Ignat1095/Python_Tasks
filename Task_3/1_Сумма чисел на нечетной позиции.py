# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


my_list = [1, 2.2, 3, 4, 5.1, 6, 7, 8, 9, 0]
summ = [my_list[i] for i in range(len(my_list)) if not i % 2]
print(summ)
print(sum(summ))


exit()
sum = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for digit in my_list[1::2]:
    if digit != 0:
        print(digit, end=" + ")
    else:
        print(digit, end="")
    sum += digit
print(" =", sum)


# ^ Второй вариант
my_list = [2, 3, 5, 9, 3]
odd = my_list[1::2]
print(odd, end=" ")
print("=", sum(odd))
