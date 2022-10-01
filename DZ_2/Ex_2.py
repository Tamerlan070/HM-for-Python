# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
print ("Введите число N: ")
N = int(input())
factorial = list() # задали пустой список 
for i in range (0, N):
    N = N -1
    factorial.append(N*(N-1))
    

print (factorial)