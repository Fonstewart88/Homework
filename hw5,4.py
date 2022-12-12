# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

    

txt = 'ЯЯЯЯЯ ллюююбббблллллюююю       ДДДДДДДДжжжжжжжжжаааааааавввввввууууууаааааббббввв\
      аааббббвввввииииии       ППППППППиииииииииттттттттооооооон'
lst1 = list(map(str,txt))
txt1 = []
count = 1
for i in range(len(lst1)):
    if i + 1 == len(lst1):
        txt1.append(count)
        txt1.append(lst1[i])

    elif lst1[i] == lst1[i+1]:
        count +=1
    else:
        txt1.append(count)
        txt1.append(lst1[i])
        count = 1
txt1 = ''.join(map(str,txt1))
print(txt1)

lst2 = []
for i in range(len(txt1)):
    if i % 2 == 0:
        for j in range(int(txt1[i])):
            lst2.append(txt1[i+1])

txt2 = ''.join(lst2)
print(txt2)