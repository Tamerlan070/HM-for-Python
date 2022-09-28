from cmath import sqrt
from lib2to3.pytree import convert


print ("Введите координату точки А: ")
a = map(int,input().split())
a = int(a)
print ("Введите координату точки B: ")
b = map (int,input().split())
b = int(b)
result = sqrt(((b [1] - a [1])**2) + ((b[0] - a [0])**2))
print (result)