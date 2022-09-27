# 1.Наишите программу, которая принимает на вход цифру,
#   обознпачающую день недели, и проверяет, является ли этот день выходным.

def Input_digit(input_text):
    is_OK = False
    while not is_OK:
        try:
            _digit = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print('Это не число!')
    return _digit


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


num = Input_digit("Введите число недели: ")
check_number(num)
