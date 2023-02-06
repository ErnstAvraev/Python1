from random import randint
# x = randint(0, 100)
# # if x > 50:
# #     y = True
# # else:
# #     y = False
# y = True if x > 50 else False                 # тернарный оператор
# print(f'сгенерировано число {x}')
# print(y)

# i = 0
# sum = 0
# while i <= x:                                  # while
#     sum += i
#     i += 1
# print(sum)

# sum2 = 0
# for i in range(x+1):                             # for
#     sum2 += i
# print(sum2)

# for i in 4, 66, 88, True, "привет":
#     print(i)

# sp = ["dsfsdf", 88, 55, True]

# for k,v in enumerate(sp):
#     if v==55:
#         continue                                  # continue как пропуск одной итерации
#     print(k,v)


# Задача No9. Общее обсуждение
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while
# Input: 5
# Output: 120


# n = int(input("Введите целое, неотрицательное число: "))
# fact = 1
# i = 1
# if n<0:
#     print("Введите целое, неотрицательное число")
# else:
#     while i <= n:
#         fact *= i
#         i += 1
#     print(fact)


# Задача No11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно
# является, то есть выведите такое число n, что φ(n)=A. Если А не является числом
# Фибоначчи, выведите число -1.
# Input: 5 Output: 6

# A = int(input('number: '))
# a = 0
# b = 1
# c = 0
# f = 0
# while b <= A:
#     c = b
#     b = b+a
#     a = c
#     f += 1
# if A == b or A == a:
#     print(f)
# else:
#     print('-1')

# from math import inf
# a = int(input('number: '))
# fib = [0, 1]

# for i in range(1, a+1):
#     fib.append(fib[i]+fib[i-1])
# print(fib)

# if a in fib:
#     for i in range(len(fib)):
#         if a == fib[i]:
#             print(i+1)
# else:
#     print("-1")

# num = int(input(': '))
# first = 0
# second = 1
# counter = 2
# while second <= num:
#     if second == num:
#         print(counter)
#         break
#     first, second = second, first+second
#     counter+=1
# else:
#     print('-1')


# # Задача No13. Решение в группах
# # Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это
# # самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к
# # синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые
# # годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они
# # называют период, в который среднесуточная температура ежедневно превышала 0
# # градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# # Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# # В следующих строках располагается N целых чисел.
# # Каждое число – среднесуточная температура в соответствующий день.
# # Температуры – целые числа и лежат в диапазоне от –50 до 50
# # Input: 6 -> -20 30 -40 50 10 -10
# # Output: 2

# n = int(input("Введите количество дней: "))
# if 1 <= n <= 100:
#     temperature = []
#     counter = counterMax = 0

#     for i in range(0, n):
#         temperature.append(randint(-50, 50))
#     print(temperature)                                  # Мое решение
#     for i in range(len(temperature)):
#         if temperature[i] > 0:
#             counter += 1
#         else:
#             if counter > counterMax:
#                 counterMax = counter
#             counter = 0
#     print(counterMax)
# else:
#     print("Введите число от 1 до 100")

# Решение Игоря

# def Get_and_check_number():
#     flag = True
#     num = int(input("Введите кол-во дней: "))
#     while flag:
#         if num<1 or num>100:
#             print("error number")
#             num = int(input("Введите кол-во дней: "))
#         else:
#             flag = False
#     return num

# def createList(num):
#     listDayTemp = [0]*num
#     for count in range(num):
#         listDayTemp[count] = randint(-50, 50)
#     return listDayTemp

# def CheckWarmDays(list):
#     count = 0
#     for count in range(len(list)-1):
#         if list[count]>0 and list(count+1)>0:
#             count+=1
#         elif list
#             count = 0
#     print(count)

# day = Get_and_check_number()
# list = createList(day)
# print(list)
# CheckWarmDays(list)


# Решение Виталия

import random

# while True:
#     n = input('Введите число дней N или "q" для выхода:')
#     if n == 'q':
#         exit()

#     n = int(n)
#     temp_stat = []

#     for _ in range(n):
#         temp_stat.append(random.randint(-50, 50))

#     print(temp_stat)

#     count = max_count = 0

#     for temp in temp_stat:
#         if temp > 0:
#             count += 1
#             if max_count < count:
#                 max_count = count
#         else:
#             count = 0

#     print(max_count)


# # Задача No15. Решение в группах
# # 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# # а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для
# # тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# # самый легкий и самый тяжелый арбуз? Помогите ему!
# # Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N
# # чисел, записанных на новой строчке каждое. Здесь каждое число – это масса
# # соответствующего арбуза
# # Input: 5 -> 5 1 6 5 9 Output: 1 9

# n = int(input("Введите колтчество арбузов: "))
# sp = []
# for i in range(n):
#     sp.append(randint(1, 10))
# print(sp)
# min = sp[0]
# max = sp[0]
# for i in range(n):
#     if sp[i] > max:
#         max = sp[i]
#     if sp[i] < min:
#         min = sp[i]
# print(min, max)
