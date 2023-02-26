# # Задача No39. Решение в группах
# # Даны два массива чисел. Требуется вывести те элементы первого массива
# # (в том порядке, в каком они идут в первом массиве), которых нет во
# # втором массиве. Пользователь вводит число N - количество элементов в
# # первом массиве, затем N чисел - элементы массива. Затем число M - количество
# # элементов во втором массиве. Затем элементы второго массива
# # Ввод:
# # 7
# # 3 1 3 4 2 4 12
# # 6
# # 4 15 43 1 15 1
# # Вывод:
# # 3 3 2 12
# # (каждое число вводится с новой строки)
from random import randint as rnd


# def compare(arr1, arr2, arr3=[]):
#     for i in arr1:
#         if i not in arr2:
#             arr3.append(i)
#     print(arr3)


# arr1 = [rnd(0, 10) for i in range(rnd(5, 10))]
# arr2 = [rnd(0, 10) for i in range(rnd(5, 10))]
# print(arr1, "\n", arr2)
# compare(arr1,arr2)

# # Задача No41. Решение в группах
# # Дан массив, состоящий из целых чисел. Напишите программу, которая в данном
# # массиве определит количество элементов, у которых два соседних и, при этом,
# # оба соседних элемента меньше данного. Сначала вводится число N — количество
# # элементов в массиве Далее записаны N чисел — элементы массива.
# # Массив состоит из целых чисел.
# # Ввод: Ввод:
# # 55
# # 1 2 3 4 5 15151
# # Вывод: Вывод:
# # 0           2

# def if_less(sp):
#     count = 0
#     for _ in range(1, len(sp)-1):
#         if sp[_-1] < sp[_] and sp[_] > sp[_+1]:
#             count += 1
#     print(count)

# for _ in range(4):
#     sp = [rnd(0, 10) for i in range(rnd(5, 10))]
#     print(sp)
#     for _ in range(4):
#         if_less(sp)


# # Задача No43. Решение в группах
# # Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# # Считается, что любые два элемента, равные друг другу образуют одну пару,
# # которую необходимо посчитать. Вводится список чисел. Все числа списка находятся
# # на разных строках.
# # Ввод: Вывод:
# # 1232 3 2


# def pairs(arr):
#     count = 0
#     temp = set(arr)
#     arr_temp = []
#     for i in (temp):
#         for j in range(0,len(arr)):
#             if i == arr[j]:
#                 count+=1
#         arr_temp.append(count)
#         count = 0
#     count2 = 0
#     for i in range(len(arr_temp)):
#         count2 = count2+arr_temp[i]//2
#     print(count2)

# # sp = list(map(int, input("Введите числа списка через пробел: ").split())) # сбор списка при вводе
# sp = [(rnd(1, 10)) for _ in range(10)]
# print(sp)
# pairs(sp)


# # Решение Ангелины
# def pair(lst):
#     count = 0
#     myset = set(lst)
#     for i in myset:
#         x = lst.count(i)
#         count+=x//2
#     print(count)
# n = int(input("n = "))
# lst1 = [rnd(1,9) for _ in range(n)]
# print(lst1)
# pair(lst1)

# # Решение Игоря

# def find_pairs_in_list (users_list):
#     count = 0
#     for i in range(len(users_list)):
#         for j in range(i+1,len(users_list)):
#             if users_list[i] == users_list[j] and users_list[j] != '' and users_list[i] != '':
#                 count+=1
#                 users_list[j] = ''
#                 users_list[i] = ''
#     return count

# from random import randint as rnd
# users_len_list = int(input("Введите предполагаемую длину массива \n"))
# users_list = []
# for i in range(users_len_list):
#     users_list.append(rnd(1,10))

# print(users_list)
# res = find_pairs_in_list(users_list)
# print (res)

# # Задача No45. Решение в группах
# # Два различных натуральных числа n и m называются дружественными, если сумма
# # делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# # Например, 220 и 284 – дружественные числа. По данному числу k выведите все
# # пары дружественных чисел, каждое из которых не превосходит k. Программа получает
# #  на вход одно натуральное число k, не превосходящее 105. Программа должна
# #  вывести все пары дружественных чисел, каждое из которых не превосходит k.
# #  Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара
# #  должна быть выведена только один раз (перестановка чисел новую пару не дает).
# # Ввод: Вывод:
# # 300 220 284

# def getSum(value):
#     res = 1
#     for i in range(2, int(value**0.5)+1):
#         if value % i == 0:
#             res += i + value // i
#     return res


# n = int(input("n = "))
# for i in range(10, n):
#     sum1 = getSum(i)
#     sum2 = getSum(sum1)
#     if sum2 == i and sum1 != sum2:
#         print(i, sum1)
