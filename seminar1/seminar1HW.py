# #                     Задача 2:
# # Найдите сумму цифр трехзначного числа.

# number = int(input('Введите 3х значное число: '))
# sum = 0
# count = 0
# while number % 10 != 0:
#     sum = sum+number % 10
#     number = number//10
#     count += 1
# if count == 3:
#     print(sum)
# else:
#     print("Введено не 3х значное число!")

# #                     Задача 4:
# # Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали
# # S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и
# # Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше
# # журавликов, чем Петя и Сережа вместе?‹

# s = int(input('Введите количество журавликов: '))
# amount = s/6
# sergPetya = amount
# katya = amount*4
# print(f'Сережа и Петя собрали по {sergPetya} журавликов, Катя собрала {katya} журавликов')

# #                     Задача 6:
# # Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за
# # проезд и получали билет с номером. Счастливым билетом называют такой билет с
# # шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется
# # написать программу, которая проверяет счастливость билета.

# number = int(input('Введите 6-ти значный номер билета: '))
# count = 0
# sum1 = 0
# sum2 = 0
# while count != 3:
#     sum1 = sum1+number % 10
#     number = number//10
#     count += 1
# while number % 10 != 0:
#     sum2 = sum2+number % 10
#     number = number//10
# if sum1 == sum2:
#     print("Билет счастливый, поздравляю!")
# else:
#     print("Билет не является счастливым(")

# #                     Задача 8:
# # Требуется определить, можно ли от шоколадки размером n × m долек
# # отломить k долек, если разрешается сделать один разлом по прямой между дольками
# # (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите n: '))
# m = int(input('Введите m: '))
# k = int(input('Введите k: '))

# if k>n*m or k==n*m:
#     print("NO")
# elif k%m == 0 or k%n == 0:
#     print("YES")
# else:
#     print("NO")

# #                     Задача 2:
# # HARD необязательная, идет за 3 обязательных Найдите сумму цифр любого
# # вещественного или целого числа. Можно использовать decimal. Через строку решать
# # нельзя.

# from decimal import Decimal
# try:
#     number = Decimal(input('Введите любое число: '))
#     sum = 0
#     sum1 = 0
#     sum2 = 0
#     numFloat = 0
#     numInt = 0
#     # проверка на целое или вещественное число
#     if number - int(number) == 0:
#         while number % 10 != 0:                                     # число целое
#             sum = sum+number % 10
#             number = number//10
#         print(sum)
#     else:                                                           # число вещественное
#         # находим дробную часть
#         numFloat = number-int(number)
#         # находим целую часть
#         numInt = int(number)
#         # находим сумму целой части
#         while numInt % 10 != 0:
#             sum1 = sum1+numInt % 10
#             numInt = numInt//10
#         # находим сумму дробной части
#         while numFloat % 1 != 0:
#             sum2 = sum2+int(numFloat*10)
#             numFloat = numFloat*10 - int(numFloat*10)
#         print(sum1+sum2)
# except:
#     print("Введите корректное число!")
