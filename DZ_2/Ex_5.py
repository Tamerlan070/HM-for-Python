#  Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random. 
print ("Введите числа через пробел: ")
array = input()
lst = array.split(" ") # 
for i in range len(lst)
    lst[-1], lst[i] = lst[i], lst[-1]
print (lst)


