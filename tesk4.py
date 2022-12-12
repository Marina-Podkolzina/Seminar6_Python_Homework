#Напишите программу, которая принимает на вход число N и
#выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# Первоначальное решение:
# print('Введите число')
# n = int (input())
# list = [0]*n
# f = 1
# i = 1
# while i<=n:
#     f = f*i
#     list[i-1] = f
#     i += 1
# print (list)    

#Решение с функцией Lambda:

from math import factorial

n = int(input('Введите число: '))
f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)