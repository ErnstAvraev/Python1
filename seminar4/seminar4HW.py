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


# Задача FOOTBALL необязательная. Напишите программу, которая принимает на
# стандартный вход список игр футбольных команд с результатом матча и выводит на
# стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

# n = int(input("Введите количество результатов: "))
# dictionary = dict()
# for i in range(n):
#     temp = input(
#         "Введите название команды и количество забитых мячей через пробел: ").split()
#     for i in range(len(temp)-1):
#         dictionary[temp[i+1]] = temp[i]
# print(dictionary)
# fixDict = dict()
# count = 0
# win = 0
# draw = 0
# lose = 0
# score = 0
# temp = 0
# temp1 = 0
# for k, v in dictionary.items():
#     temp = dictionary.values()
#     temp1 = dictionary.keys()
#     for v in dictionary:
#         if temp == dictionary[v]:
#             count += 1
#     for k,v in dictionary.items():
#         if k > temp1:
#             lose += 1
#         elif int(k) < temp1:
#             win += 1
#         elif int(k) == temp1:
#             draw += 1
#     if win >= 1:
#         score = win*3
#     elif draw >= 1:
#         score = score+draw
#     fixDict[v] = count, win, draw, lose, score
#     count = 0
#     win = 0
#     draw = 0
#     lose = 0
#     score = 0
# print(fixDict)
# # TeamData = dict(input("Введите команды и количество очков через ;  "))
# # print(TeamData)

n = int(input('kolichestvo igr: '))
x_list = [input('kom1;gol1;kom2;gol2: ').split(';') for x in range(n)]
print(x_list)
vs = [(x[0], x[2]) for x in x_list]
print(vs)
import itertools
clubs = set(itertools.chain.from_iterable(vs))
print(clubs)
res = {club:[0, 0, 0, 0, 0] for club in clubs}
print(res)
for kom1, gol1, kom2, gol2 in x_list:
    res[kom1][0] += 1
    res[kom2][0] += 1
    if int(gol1) > int(gol2):
        res[kom1][1] += 1
        res[kom1][4] += 3
        res[kom2][3] += 1
    elif int(gol1) < int(gol2):
        res[kom2][1] += 1
        res[kom2][4] += 3
        res[kom1][3] += 1
    elif int(gol1) == int(gol2):
        res[kom1][2] += 1
        res[kom1][4] += 1
        res[kom2][2] += 1
        res[kom2][4] += 1
for club in clubs:
    print('{}:{}'.format(club, ' '.join(map(str, res[club]))))