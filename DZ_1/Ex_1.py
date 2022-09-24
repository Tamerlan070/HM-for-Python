print ("Введиите число дня недели")
day = int(input())
if 1 <= day <=5:
    print ("Будний день")
elif 6 <= day <= 7:
        print ("Выходной день")
if day > 7:
    print ("Неверная цифра")
