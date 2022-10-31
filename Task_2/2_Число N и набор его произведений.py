# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
while True:
    number = [abs(int(input()))]  # int(input('Enter number: '))

    x = list(map(lambda num: 1 if num == 1 else num*(num-1), number))

    print(*number, *x)

exit()

x = (lambda num: 1 if num == 1 else num*x(num-1))

number = int(input('Enter number: '))

print(number, x(number))


a = "456"
b = map(int, a)
print(sum(b))


number = int(input("number = "))
sum = 1
for i in range(1, number + 1):
    sum *= i
    print(sum, end=" ")
