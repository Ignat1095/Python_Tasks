# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


# print(f"Всего {candys} конфет")

from random import shuffle


print("\nНажми [ 1 ], если хочешь играть против компьютера")
players = [i for i in range(int(input("Сколько будет игроков? ")))]


for i in players:
    print(f"Имя {i+1} игрока:", end=" ")
    players[i] = input().capitalize()

if len(players) == 1:  # ^ Добавил бота в игру
    players += ["Bot"]

print("\nПутем несложной жеребьевки получаем следующую очередность хода ;D")
shuffle(players)
print(" "*10, "Играет:", *players, "\n")


max_count = len(players)
candys = 100
print("Всего конфет: ", candys)


count = 0  # Очередность ходов
candys_max = 28  # Максимальное конфет за раз


while candys > candys_max:
    print(f"Ходит {players[count]}", end="")
    if players[count] == "Bot":
        if candys < candys_max*2+1:  # Условие,что бот ходит от 1 до 28  за раз
            i = candys-candys_max-1
            if i <= 0:
                i = 1  # Мин ход 1
        else:
            i = candys_max
        print(f" --> {i}")

    else:
        i = int(input(", сколько конфет возьмешь? --> "))
        while i not in range(1, candys_max+1):
            print("Давай по честному! Можешь взять максимум 28 шт")
            i = int(input("Сколько конфет возьмешь? "))

    candys -= i
    if candys > candys_max:
        print("\nКонфет осталось:", candys,)

    if count == max_count-1:  # перевод очередности в рачало
        count = 0
    else:
        count += 1


else:
    print(f"\nОсталось всего {candys} конфет!")
    print(
        f"Победил [{players[count]}], т.к. он забирает последние конфеты!")
