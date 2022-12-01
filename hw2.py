# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# def sumNums(num):
#     sum = 0
#     for i in str(x):
#         if i != ".":
#             sum += int(i)
#     return sum

# x = float(input(f'Введите число -> '))
# print(f'Сумма цифр = {sumNums(x)}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def mag(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mag(n - 1)


# N = int(input(f'Введите число -> '))

# list = []
# for i in range(1, N + 1):
#     list.append(mag(i))

# print(f"Произведения чисел от 1 до {N}:  {list}")

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# n = int(input(f'Введите число -> '))

# list = []
# for i in range (1, n + 1):
#     list.append(round((1+1/i)**i, 2))
# print(f" Для n = {n} {list} сумма {round(sum(list), 2)}")


# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

# def sum(list1, list2):
#     s = 0
#     for i in range(len(list2)):
#         s += (list1[int(list2[i])])
#     return s


# N = int(input(f'Введите число -> '))
# list = []
# help = -N
# for i in range(N*2+1):
#     list.append(help)
#     help += 1
# index = input(f'Введите числа через пробел от 0 до {N * 2} -> ')
# index_list = index.split(" ")
# print(index_list)
# print(sum(list, index_list))

# Реализуйте алгоритм перемешивания списка.
import random


l = input(f'Введите числа через пробел -> ')
numbers1 = l.split(" ")
numbers2 = []
for i in range(len(numbers1)):
    h = i
    numbers2.append(h)
random.shuffle(numbers2)
numbers3 = []
for e in range(len(numbers1)):
    numbers3.append(0)
a = 0
while a < len(numbers1):
        n = numbers2[a]
        print(numbers1[int(n)])
        numbers3[a] = numbers1[int(n)]
        a += 1

print(f"  {numbers1} --> {numbers3} ")
