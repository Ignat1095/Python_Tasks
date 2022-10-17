# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в
# файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или
# x² + 5 = 0 или
# 10*x² = 0

from random import randint
k = int(4)


def mnogochlen(k):
    answer = list()
    while k >= 0:
        c = randint(1, 9)

        if k > 0:
            answer.append(f'{c}x^{k}')
        elif k == 0:
            answer.append(c)

        flag = randint(0, 1)
        if flag == 1:
            answer.append('+')
        else:
            answer.append('-')

        k -= 1

    answer.pop(-1)
    answer.append('=0')
    return answer


# mnogochlen(k)

txt = open("4_1.txt", 'w')
txt.write(''.join(map(str, mnogochlen(k))))
txt.close()

txt = open("4_2.txt", 'w')
txt.write(''.join(map(str, mnogochlen(k))))
txt.close()
