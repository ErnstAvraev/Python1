# # # посчитать сумму всех чисел от 1 до n, вводимое пользователем
# def summa1(num):
#     sum = 0
#     for i in range(num+1):
#         sum += i
#     return sum


# def summa2(num):
#     sum = 0
#     while True:
#         if num == 0:
#             break
#         sum += num
#         num -= 1
#     return sum


# def summa_rec(num):
#     if num == 0:
#         return 0
#     return num + summa_rec(num-1)

# # 5 + (4 + (3 + (2 + (1 + 0))))

# n = int(input("Input n = "))
# # sum = 0
# # for i in range(n+1):
# #     sum+=i
# # print(sum)

# print(summa1(n))
# print(summa2(n))
# print(summa_rec(n))

# # Задача No31. Общее обсуждение
# # Последовательностью Фибоначчи называется последовательность чисел a0, a1, ...,
# # an, ..., где
# # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи
# # Input: 7 Output: 21

# def fib(num):
#     if num in [1, 2]:
#         return num-1
#     return fib(num-1)+fib(num-2)


# n = int(input('n = '))

# print(fib(n))

# # Задача No33. Решение в группах
# # Хакер Василий получил доступ к классному журналу и хочет заменить все свои
# # минимальные оценки на максимальные. Напишите программу, которая заменяет
# # оценки Василия, но наоборот: все максимальные – на минимальные.
# # Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# from random import randint as rnd


# def max_val(array):
#     if len(array) > 1:
#         max = max_val(array[1:])
#         if array[0] < max:
#             return max
#         else:
#             return array[0]
#     if len(array) == 1:
#         return array[0]


# def min_val(array):
#     if len(array) > 1:
#         min = min_val(array[1:])
#         if array[0] > min:
#             return min
#         else:
#             return array[0]
#     if len(array) == 1:
#         return array[0]


# def change_marks(max, min, i):
#     if i == len(arr_grades):
#         return arr_grades
#     else:
#         if max == arr_grades[i]:
#             arr_grades[i] = min
#     return change_marks(max, min, i+1)


# volume = int(input("задайте количество оценок: "))
# arr_grades = [rnd(1, 5) for _ in range(volume)]
# print(arr_grades)
# max_grade = max_val(arr_grades)
# min_grade = min_val(arr_grades)
# i = 0
# print(change_marks(max_grade,min_grade,i))


# # Задача No35. Решение в группах
# # Напишите функцию, которая принимает одно число и проверяет, является ли оно
# # простым
# # Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само
# # число)
# # Input: 5 Output: yes

# def ord_num(n, m):
#     if m == 1:
#         return True
#     elif m == 0:
#         return False
#     elif n % m == 0:
#         return False
#     return True and ord_num(n, m-1)


# n = int(input("n = "))
# print("\n", ord_num(n, n-1))


# # Задача No37. Решение в группах
# # Дано натуральное число N и последовательность из N элементов. Требуется
# # вывести эту последовательность в обратном порядке.
# # Примечание. В программе запрещается объявлять массивы и использовать циклы
# # (даже для ввода и вывода).
# # Input: 2 -> 3 4 Output: 4 3

# n = int(input('Введите N: '))

# def addWord(ind, str):
#     if (ind >= n):
#         return str
#     str += input(f'Введите {ind+1}-ый символ: ')
#     return addWord(ind +1, str)

# def revertStr(ind, inputStr, resultStr):
#     if (ind < 0):
#         return resultStr
#     resultStr += inputStr[ind]
#     return revertStr(ind -1, inputStr, resultStr)

# inputStr = addWord(0, "")
# torevertStr = revertStr(len(inputStr) -1, inputStr, "")
# print(inputStr)
# print(torevertStr)