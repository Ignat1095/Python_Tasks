# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from cmath import pi
d = int(input("d = "))
if d >= 0:
    True
    answer = round(pi, d)
    print(answer)
else:
    print("enter an integer!")
