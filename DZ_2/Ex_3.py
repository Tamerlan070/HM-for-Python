# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
print ('Введите число n: ')
n = int(input())

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))