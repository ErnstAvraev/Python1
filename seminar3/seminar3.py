# sp = []
# sp.append(1234) # с конца
# sp.extend([888, True, 'Hi']) # добавление сразу нескольких значений
# sp.insert(0, 'Begin') # с начала
# sp2 = [1111, 7777]
# sp = sp+sp2
# a = sp.pop()  # можно написать индекс
# sp.remove('Hi')
# # del sp[0]
# print(sp)
# print(a)

# lst = [i for i in range(11) if i % 2 == 0] # list comprehension
# print(lst)
# for i,v in enumerate(lst):
#     print(i,v)
# for el in sp:


# sp = [0] * 10
# print(sp)
# print(len(sp))

# Кортежи
# kort = (1,5,8,9)
# print(kort[0])
# # kort[0] = 888 # нельзя изменять кортеж

# # словарь
# slov = {'Ivan': 876578, 'Sergei':[567843456,98763456]}
# print(slov.keys())
# print(slov.values())
# print(slov)
# for k,v in slov.items():
#     print(k,v)
# print(slov['Ivan'])
# slov['Fedor'] = 345679876 # добавляем напрямую
# print(slov)


# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6
from random import randint

# # с данными из задачи
# arr = [1, 1, 2, 0, -1, 3, 4, 4]
# arr = set(arr)
# print(arr)
# print(len(arr))

# # со случайными числами
# n = int(input('Input length of an array: '))
# arr1 = [randint(-10,10) for _ in range(n)]
# print(arr1)
# arr1 = set(arr1)
# print(arr1)
# print(len(arr1))


# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю
# последовательность (сдвиг - циклический) на K элементов вправо, K – положительное
# число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# n = int(input('Input length of an array(n): '))
# k = int(input('Input k: '))
# arr1 = [randint(-10,10) for _ in range(n)]
# print(arr1)
# for i in range(k):
#     # a = arr1.pop()
#     arr1.insert(0, arr1.pop())
# print(arr1)
# # удалить из списка все значения меньше 0
# for i in arr1:
#     if i < 0:
#         arr1.remove(i)
#         for i in arr1:
#             if i < 0:
#                 arr1.remove(i)
#                 for i in arr1:
#                     if i <0:
#                         arr1.remove(i)
#                         for i in arr1:
#                             if i < 0:
#                                 arr1.remove(i)
# print(arr1)


# Задача No21. Решение в группах
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#        {"VII": " S005 "}, {" V ": " S009 "}, {" VIII ": " S007 "}]
# lst = set()
# for dict in dic:
#     for v in dict.values():
#         lst.add(v.strip())
# print(lst)


# Задача No23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

# n = int(input('Введите длину списка n = '))
# sp = [randint(-10, 10) for i in range(n)]
# print(sp)
# count = 0
# for i in range(1, len(sp)):
#     if sp[i] > sp[i-1]:
#         count += 1
# print(count)
