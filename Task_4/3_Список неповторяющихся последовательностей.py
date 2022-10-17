# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся
# элементов исходной последовательности.
from itertools import count


my_list = [1, 2, 3, 2, 1, 3, "aa", "Aa", "aa", 7]
print(my_list)


# n = set(my_list)  # ^ Через встроеную функцию
# print(n)


unique = []  # ^ Через for и .count()
for i in my_list:
    if my_list.count(i) == 1:
        unique.append(i)
print(unique)

exit()


def get_unique_numbers(numb):  # ^ Через функцию с for
    unique2 = []
    for i in numb:
        if i in unique2:
            continue
        else:
            unique2.append(i)
    return unique2


print(get_unique_numbers(my_list))
