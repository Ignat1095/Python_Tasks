# 2. Напишите программу, которая принимает на вход координаты точки(X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Нашел оригинальное решение!
# def quarter(x, y):
#     ans = [['I', 'II'], ['IV', 'III']]
#     print(ans[y < 0][x < 0], ' четверть')
# quarter(2, -3) # IV четверть


def input_coord(x):
    a = [0]*x
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                number / number  # На 0 делить нельзя
                a[i] = number
                is_OK = True
            except ZeroDivisionError:
                print("Координата не должна лежать на осях Х или У")
            except ValueError:
                print("Введите число")
    return a


def check_coord(XY):

    if XY[0] > 0 and XY[1] > 0:
        quarter = 1
    elif XY[0] < 0 and XY[1] > 0:
        quarter = 2
    elif XY[0] < 0 and XY[1] < 0:
        quarter = 3
    elif XY[0] > 0 and XY[1] < 0:
        quarter = 4
    print(f"Точка находится в {quarter} четверти плоскости")


coord = input_coord(2)
check_coord(coord)
