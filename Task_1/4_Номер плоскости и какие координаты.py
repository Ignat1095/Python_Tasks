# 1. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def quart_input():
    try:
        quarter = int(input("Введите номер четверти: "))
        if 0 < quarter <= 4:
            return quarter
        else:
            print("Введите ЦЕЛОЕ число от 1 до 4")
            quart_input()
    except (ValueError, TypeError):
        print("Введите число от 1 до 4")
        quart_input()


def range_coord(value):
    if value == 1:
        print("Возможные координаты точки( X>0 , Y>0 )")
    elif value == 2:
        print("Возможные координаты точки( X<0 , Y>0 )")
    elif value == 3:
        print("Возможные координаты точки( X<0 , Y<0 )")
    elif value == 4:
        print("Возможные координаты точки( X>0 , Y<0 )")


value = quart_input()
range_coord(value)
