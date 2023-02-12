# # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# # решкой, а некоторые – гербом. Определите минимальное число
# # монеток, которые нужно перевернуть, чтобы все монетки были
# # повернуты вверх одной и той же стороной. Выведите минимальное
# # количество монет, которые нужно перевернуть.
# # 5 -> 1 0 1 1 0 2

# import time
# from random import randint
# n = int(input("Введите количество монет: "))
# coins = []
# count0 = 0
# count1 = 0
# for i in range(n):
#     coins.append(randint(0, 1))
# print(coins)
# for i in range(len(coins)):
#     if coins[i] == 1:
#         count1 += 1
#     elif coins[i] == 0:
#         count0 += 1
# if count0 > count1:
#     print(count1)
# else:
#     print(count0)

# # Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# # школьница. Петя помогает Кате по математике. Он задумывает два
# # натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# # этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# # произведение P. Помогите Кате отгадать задуманные Петей числа.
# # 4 4 -> 2 2 5 6 -> 2 3

# s = int(input("Введите s: "))
# p = int(input("Введите p: "))
# for i in range(0, 1000):
#     for j in range(0, 1000):
#         if i+j == s and i*j == p:
#             print(f'x = {i}, y = {j}')

# # Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# # не превосходящие числа N.
# # 10 -> 1 2 4 8

# n = int(input("Введите число: "))
# power = []
# for i in range(n):
#     if 2**i <= n:
#         power.append(2**i)
# print(power)

# # Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения
# # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) . Но теперь количество
# # предикатов не три, а генерируется случайным образом от 5 до 25, сами значения
# # предикатов случайные, проверяем это утверждение 100 раз, с помощью модуля time
# # выводим на экран , сколько времени отработала программа. В конце вывести результат
# # проверки истинности этого утверждения.

# start = time.time()
# predicates = []
# input = randint(5, 25)
# for i in range(input):
#     predicates.append(randint(0, 1000))
# for j in range(100):
#     left = not (predicates or predicates or predicates)
#     right = not predicates and not predicates and not predicates
#     result = left == right
# if result == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")
# end = time.time()
# print(f'Программа отработала = {end-start} сек.')

# # задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи,
# # в том числе для отрицательных индексов.
# # *Пример:*
# # - для k = 8 список будет выглядеть так:
# # [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# def fib(num):
#     if num == 0:
#         return 0
#     elif num in [1, 2]:
#         return 1
#     else:
#         return fib(num-1)+fib(num-2)


# def negaFib(num):
#     return ((-1)**(num+1))*fib(num)


# num = int(input("Введите порядковый номер числа = "))
# fibArr1 = []
# fibArr2 = []
# for e in range(1, num+1):
#     fibArr1.append(negaFib(e))
# for a in range(0, num+1):
#     fibArr2.append(fib(a))
# fibArr1.reverse()
# fullArr = fibArr1+fibArr2

# print(fullArr)

# # Задача 5 - HARD необязательная
# # Напишите программу, которая принимает на вход координаты двух точек и находит
# # расстояние между ними в N-мерном пространстве. Сначала задается N с клавиатуры,
# # потом задаются координаты точек.

# n = int(input("Введите количество измерений n = "))
# dotA = []
# dotB = []
# mult = 0
# for i in range(n):
#     dotA.append(int(input("Введите координаты точки А: ")))
# for j in range(n):
#     dotB.append(int(input("Введите координаты точки B: ")))
# for k in range(n):
#     mult += (dotA[k]-dotB[i])**2
# result = mult*0.5
# print(result)
