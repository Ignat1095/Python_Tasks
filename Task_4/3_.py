# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся
# элементов исходной последовательности.
my_list = [1, 2, 2, 1, 3, 4, 5, 6, "aa", "a", "aa", 7]
print(my_list)


n = set(my_list)  # ^ Через встроеную функцию
print(n)


# unique = [] # ^ Через for
# for i in my_list:
#     if my_list in unique:
#         continue
#     else:
#         unique.append(i)
# print(unique)


def get_unique_numbers(numb):  # ^ Через функцию с for
    unique2 = []
    for i in numb:
        if i in unique2:
            continue
        else:
            unique2.append(i)
    return unique2


print(get_unique_numbers(my_list))
