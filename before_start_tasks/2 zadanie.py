import math
tip=str(input("Введите название фигуры ="))
if tip=="круг":
    r=float(input("Введите радиус r ="))
    s=math.pi*(r**2)
print(s)