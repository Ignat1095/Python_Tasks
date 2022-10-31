# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.012]
print(my_list)
round_list = []

my_list2 = list((map(lambda x: round(x-int(x), 3), my_list)))

print(my_list2)
print(f'***** diff(max-min) = {max(my_list2)-min(my_list2)}')


exit()

for i in my_list:
    value_list = round(i - int(i), 2)
    round_list.append(value_list)

print("round_list =", round_list)
print(f'diff(max-min) = {max(round_list)-min(round_list)}')
