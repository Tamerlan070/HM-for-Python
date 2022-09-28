# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print ("Введите номер четверти: ")
quarter = int(input())
if quarter == 1:
    print ("x > 0 and y > 0")
if quarter == 2:
    print ("x < 0 and y > 0")
if quarter == 3:
    print ("x < 0 and y < 0")
if quarter == 4:
    print ("x > 0 and y < 0")
if  quarter < 0 or quarter > 4:
    print ("Ошибка")
