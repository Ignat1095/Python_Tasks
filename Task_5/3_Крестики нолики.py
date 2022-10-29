# Создайте программу для игры в ""Крестики-нолики"".
from tabulate import tabulate


# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# X = "X"
# O = "O"

b = [["." for i in range(3)] for j in range(3)]
b[1] = "123"

print(tabulate(b, tablefmt="heavy_grid"))
