# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#  Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


def input_coord(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Координата {xy[i]} = "))
                a.append(number)
                is_OK = True
            except (ValueError, TypeError):
                print("Ты ошибся. Вводить надо числа!")
    return a


def _length(a, b):
    length_segment = round(sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2), 2)
    return length_segment


print("Введите координаты точки А")
A = input_coord(2)
print("Введите координаты точки В")
B = input_coord(2)

print(f"Длинна отрезка = {_length(A, B)}")
