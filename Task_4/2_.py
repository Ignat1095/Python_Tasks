# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N. (делят число нацело)

# пример:    10 --> 2*5 or 5*2
number = int(input("input an integer: "))
a = b = 0
for a in range(100):
    for b in range(a+1):
        while number == a * b:
            print(number, "=", b, "*", a)
            a += 1
