#Задача. Написать программу,которая 
# будет принимать число N и выводить числа от -N до N.

# Первоначальное решение:
# n = int(input('Введите число: '))
# a= []
# b = ' '
# for i in range (-n, n+1):
#     a.append(i)
#     b+=f'{i}'
# print(b)

#Решение с функцией map:

n = int(input('Введите число: '))
print (" ".join(map(str, range(-n, n+ 1))))
