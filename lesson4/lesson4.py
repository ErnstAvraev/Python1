# def f(x):
#     return x*x
# a = f
# print(f(5))
# print(a(5))
# print(type(f))
# print(type(a))

# def calc1(a,b):
#     return a+b


# def calc2(a,b):
#     return a*b


# def math(op, x, y):
#     print(op(x, y))


# math(calc1, 5,45)
# math(calc2, 5,45)

# # lambda

# def math(op, x, y):
#     print(op(x, y))


# def calc1(a, b): return a+b


# math(calc1, 5, 45)
# math(lambda a, b: a+b, 5, 45) # lambda

# sp = [1, 2, 3, 5, 8, 15, 23, 38]

# res = []
# for i in sp:
#     if i%2 == 0:
#         res.append((i,i**2))

# print(res)

# def select(f,col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res= where(lambda x: x%2==0, res)
# print(res)
# res = list(select(lambda x:(x, x**2), res))
# print(res)

# # map

# list_1 = [x for x in range(1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# лист строк в лист чисел с помощью map

# data = '15 156 96 3 5 52 5'
# # print(data)
# # data= data.split()
# # print(data)
# # data = list(map(int, data))
# # print(data)
# data = list(map(int, data.split()))
# print(data)

# # filter

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# # zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)

# users2 = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids2 = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data2 = list(zip(users, ids, salary))
# print(data2)  # zip() пробегает по минимальному входящему набору

# # enumerate
# # функция возвращает кортежи из индекса и элементов входных данных
# users = ['user1', 'user2', 'user3']
# data3 = list(enumerate(users))
# print(data3)

# #                                   файлы

# # a - открытие для добавления данных(append)
# # позволяет дописывать что-то в имеющийся файл
# # если файла нет, то он его создаст и запишет

# # r - открытие для чтения данных(read)
# # позволяет читать данные из файла
# # если вы попробуете считать данные из файла, которого не существует,
# # программа выдаст ошибку

# # w - открытие для записи данных(write)
# # позволяет записывать данные и создавать файл, если его не существует
# # (перезаписывает файл)

# # w+ - позволяет открывать файл для записи и читать из него,
# #  если файла не существует, он его создаст

# # r+ - позволяет открывать файл для чтения и дописывать в него,
# # если файла не существует, программа выдаст ошибку

# # colors = ['red', 'green', 'blue']
# # data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# # data.writelines(colors) # разделителей не будет
# # data.close()

# # with open('file.txt', 'w') as data: # перезапись файла
# #     data.write('line1\n') # с новой строки \n
# #     data.write('line3\n')

# # print(56)

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()
# import os
# print(os.getcwd())
# print(os.path.abspath('file.txt'))

#                                   модуль os

# нужно импортировать os
# os.chdir(path) - смена текущей директории
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
# os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# os.path - является вложенным модулем в модуль os и реализует некоторые функции 
# работы с путями, такие как:
# os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py)) # 'main.py
# os.path.abspath(path) - возвращает нормалтзованный абсолютный путь
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'

# shutil
# модуль shutil  содержит набор функций высокого уровня для обработки файлов,
# нрупп файлов и папок. В частности доступные здесь функции позволяют копировать, 
# перемещать и удалять файлы из папки. Частотиспользуется вместе с модулем os.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать
# в свою программу:
# import shutil
# Базовые функции:
# shutil.copyfile(src,dst) - копирует содержимое(но не метаданные)файла src в файл dst
# shutil.copy(src,dlt) - копирует содержимое файла scr в файл или папку dst
# shutil.rmtree(path) - удаляет текущую директорию и все поддиректории; path должен
# указывать на директорию, а не на символическую ссылку

