# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# def sum(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print(f"Для списка {lst} cумма на нечётных индексах равна: {s}")

# lst = []
# l = input(f'Введите числа через пробел -> ')
# lst = list(map(int, l.split()))
# sum(lst)


# Задача №23: Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# def do_lst(lst):
#     if len(lst) % 2 != 0:
#         l = len(lst) // 2 + 1
#     else:
#         l = len(lst) // 2
#     new_lst = []    
#     for i in range(l):
#         new_lst.append(lst[i] * lst[len(lst) - i - 1])
#     print(new_lst)    

# lst = list(map(int, input(f'Введите числа через пробел -> ').split()))
# do_lst(lst)


# Задача №24: Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# lst = list(map(float, input(f'Введите числа через пробел -> ').split()))
# new_lst = []
# for i in range(len(lst)):
#     new_lst.append(lst[i]%1)
# print(round(max(new_lst) - min(new_lst),2))

# Задача №25: Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# x = int(input(f'Введите число -> '))
# n = x
# s = ""
# while n != 0:
#     s = str(n%2) + s
#     n //=2
# print(f'{x} -> {s}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input(f'Введите число -> '))
lst = []
for i in range(n):
    lst.append(fib(i + 1))
lst2 = []
for e in range(n):
    lst2.append((-1)**((e+1)+1) * lst[e])
lst2 = lst2[::-1]
lst2.append(0)
for a in range(n):
    lst2.append(lst[a])
    
print(f'{lst2}') 