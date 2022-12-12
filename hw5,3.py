# Создайте программу для игры в ""Крестики-нолики"".

n = 3
m = 3
a = [["[ ]"] * m for i in range(n)]

a[int(input(f"введите номер строки -> "))-1][int(input(f"введите номер столбца -> "))-1] = " X "

for row in a:
    print(' '.join([str(elem) for elem in row]))


for i in range(9):
    if i % 2 == 0:
        a[int(input(f"введите номер строки -> "))-1][int(input(f"введите номер столбца -> "))-1] = " X "
        if " X " in a[0][0] and " X " in a[0][1] " X " a[0][2] : 
            print(f"Игрок X победил!!!")
            break
        elif a[1][0] == a[1][1] and a[1][0] == a[0][2]:
            print(f"Игрок X победил!!!")
            break
        elif a[2][0] == a[2][1] and a[2][0] == a[2][2]:
            print(f"Игрок X победил!!!")
            break
        elif a[0][0] == a[1][0] and a[0][0] == a[2][0]:
            print(f"Игрок X победил!!!")
            break
        elif a[0][1] == a[1][1] and a[0][1] == a[2][1]:
            print(f"Игрок X победил!!!")
            break
        elif a[0][2] == a[1][2] and a[0][2] == a[2][2]:
            print(f"Игрок X победил!!!")
            break
        elif a[0][0] == a[1][1] and a[0][0] == a[2][2]:
            print(f"Игрок X победил!!!")
            break
        elif a[0][2] == a[1][1] and a[0][0] == a[2][2]:
            print(f"Игрок X победил!!!")
            break
        print(f"Переход хода")    

