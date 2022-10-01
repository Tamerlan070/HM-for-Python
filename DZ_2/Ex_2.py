# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def factorial(num):
    result = 1
    for i in range (1, num+1):
        result = result*i
    return result


def sequence (number):
    result_list = []
    for i in range (1, number+1):
        result_list.append(factorial(i))
    return result_list

N = int(input())
print (sequence(N))
