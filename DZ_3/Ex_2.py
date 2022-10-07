# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint


print ("Введите кол-во элемеетов в списке: ")
count = int(input())
lst = []
lst2 = []


for i in range (count):
    lst.append(randint(1,10))
print (lst)


for k in range (len(lst)):
    while k < len(lst)//2 and count > len(lst2)//2:
        count = count - 1
        a = lst[k] * lst[count]
        i += 1
        lst2.append(a)
print(lst2)
