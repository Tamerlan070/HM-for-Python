# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import randint, random
import random

print("Введите кол-во вещественных чисел: ")
count = int(input())
lst = []
min = 0
max = 0

for i in range (count):
    lst.append (random.uniform(0, 20))

print (lst)

for k in lst:
    if (k - int(k)) <= min:
        min = k - int(k)
    if (k - int(k)) >= max:
        max = k - int(k) 


print (max - min)
