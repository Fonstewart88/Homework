# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_lst)

lst = list(map(int, input("Введите числа через пробел:\n").split()))
mult_lst(lst)

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input(f'Введите число -> '))
lst = [(1+1/i)**i for i in range(1,n+1)]
print(f" Для n = {n} {list} сумма {round(sum(list), 2)}")



# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

lst = list(map(float, input(f'Введите числа через пробел -> ').split()))
new_lst = [i%1 for i in lst]
print(round(max(new_lst) - min(new_lst),2))