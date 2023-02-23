# задача RLE. Реализуйте RLE алгоритм: реализуйте модуль сжатия и врсстановления данных
# например декодирование

from random import randint

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return (res)

# word = input(': ')
# print(coding(word))  # кодирование введенных данных
# # print(decoding(word))  # декодирование введенных данных
# print(decoding(coding(word)))  # раскодирование ранее закодированных

# # Задача 22:
# # Даны два неупорядоченных набора целых чисел (может быть, с
# # повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# # встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# # элементов второго множества. Затем пользователь вводит сами элементы множеств.

# lst_1 = [randint(0,20) for i in range(randint(1,10))]
# lst_2 = [randint(0,20) for i in range(randint(1,10))]
# print(lst_1,lst_2)
# print(list(sorted(set(lst_2).intersection(set(lst_1)))))

# # Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# # Она растет на круглой грядке, причем кусты высажены только по окружности.
# # Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет
# # N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# # выросло различное число ягод – на i-ом кусте выросло a
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# # Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# # Собирающий модуль за один заход, находясь непосредственно перед некоторым
# # кустом, собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может
# # собрать за один заход собирающий модуль, находясь перед некоторым кустом
# # заданной во входном файле грядки.

# n = int(input("input quantity of bushes: "))
# m = int(input('input № of bush: '))
# bushes = [randint(0,100) for i in range(n)]
# print(bushes)
# berries = 0
# for i in range(len(bushes)-1):
#     if i == (m-1):
#         berries = bushes[i]+bushes[i-1]+bushes[i+1]
#     elif m == 1:
#         berries = bushes[0]+ bushes[1]+bushes[-1]
#     elif m == len(bushes):
#         berries = bushes[-2]+bushes[-1]+bushes[0]
# print(berries)