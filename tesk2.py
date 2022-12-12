# Задача.Написать программу которая 
# принимает 5 чисел и ищет максимальное.

# Первоначальное решение:

# a= input().split()
# print(a)
# max = a[0]
# for i in range(5):
#     if int(a[i])> max:
#         max = int(a[i])
# print (max)     


#Решение с функцией map:
list=(map(int,input().split()))
print(max(list))


