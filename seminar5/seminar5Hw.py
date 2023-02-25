# # Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# # и возводит число А в целую степень B с помощью рекурсии.
# # A = 3; B = 5 -> 243 (35) A = 2; B = 3 -> 8

# def power(n,m):
#     if m == 0:
#         return 1
#     if m < 0:
#         return 1 / power(n, -m)
#     if m % 2 == 0:
#         return power(n, m // 2) * power(n, m // 2)
#     else:
#         return power(n, m - 1) * n


# a = int(input("input a = "))
# b = int(input("input power b = "))
# print(power(a,b))


# # Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# # целых неотрицательных чисел. Из всех арифметических операций допускаются
# # только +1 и -1. Также нельзя использовать циклы.
# # 2 2
# # 4

# def summa(n, m):
#     if m == 0:
#         return 1
#     return n + summa(n-(n-1), m-1)


# a = int(input("a = "))
# b = int(input("b = "))
# print(summa(a, b))
