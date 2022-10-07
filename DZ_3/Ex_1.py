# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах). 
from random import randint, random


print("Введите кол-во символов в списке: ")
count = int(input())
lst = []
for i in range (count):
    lst.append(randint(0, 1000))
print (lst)
# print (type(lst)) 

sum = 0
for k in range (1,len(lst)):
   if k % 2 != 0:
    sum += lst[k]
print (sum)


