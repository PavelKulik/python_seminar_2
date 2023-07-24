print("X + Y = P\nX * Y = S")
p = int(input("Вветите число P: "))
s = int(input("Вветите число S: "))
x = 0
y = 0

dis = p ** 2 - 4 * (-1) * (-s)
if dis > 0:
    x = (-p + dis ** (0.5)) / (2 * (-1))
    y = (-p - dis ** (0.5)) / (2 * (-1))
elif dis == 0:
    x = -p / (2 * (-1))
    y = p - x
else:
    print("Нет корней уровнения")

print(f"X = {x}\nY = {y}")