# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print ("Введитке координату точки Х: ")
x = int(input())
print ("Введитке координату точки Y: ")
y = int(input())
x != 0
y != 0
if x>0 and y > 0:
    print ("Первая четверть")
if x > 0 and y <0: 
    print ("Четвертая четверть")
if x < 0 and y > 0:
    print ("Вторая четверть")
if x <0 and y < 0:
    print ("Третья четверть")
