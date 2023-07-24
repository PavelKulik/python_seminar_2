count_number = int(input("Введите количество монет: "))
coin_tails = 0
coin_eagle = 0

for i in range(0, count_number, 1):
    coin = int(input(f"Введите {i + 1} сторону монеты: герб(1) или решка(0): "))
    if coin == 0:
        coin_tails += 1
    elif coin == 1:
        coin_eagle += 1
    else:
        print("Введино неверное значение!")
        break

if coin_eagle > coin_tails:
    print(f"Перевернуть {coin_tails} решок")
elif coin_eagle < coin_tails:
    print(f"Перевернуть {coin_eagle} гербов")
else:
    print(f"Гербов и решок одинаково\n гербов: {coin_eagle} == решок: {coin_tails}")