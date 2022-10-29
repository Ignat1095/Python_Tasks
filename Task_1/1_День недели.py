# 1.Наишите программу, которая принимает на вход цифру,
#   обознпачающую день недели, и проверяет, является ли этот день выходным.


def is_int(digit):
    digit = (input("input_text: "))
    try:
        int(digit)
        return int(digit)
    except ValueError:
        print('Это не число!')
        return is_int(digit)


def check_number(num):
    if 6 <= num <= 7:
        print("Выходной")
    elif 0 < num < 6:
        if num == 3:
            print("Среда, это маленькая пятница =D")
        else:
            print("Не выходной")
    else:
        print("Это не день недели!")


digit = is_int("Введите число")
check_number(digit)
