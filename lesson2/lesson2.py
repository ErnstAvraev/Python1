#                     # списки
# list_1 = []
# list_2 = list()
# list_3 = [7, 9, 11, 13, 15, 17]
# print(list_3)
# print(*list_3)

# for i in list_3:
#     print(i)
# print(list_3[0])

# list_4 = [1, 5]
# print(list_4)
# list_4.append(8)
# print(list_4)
# list_4.append(85)
# print(list_4)

# list_5 = []
# print(list_5)
# for i in range(5):
#     list_5.append(i)
#     print(list_5)

# # удаление последнего элемента списка
# list_6 = [12, 7, -1, 21, 0]
# a = list_6.pop()
# print(a)
# print(list_6.pop())  # 0
# print(list_6)  # [12,7,-1,21]
# print(list_6.pop())  # 21
# print(list_6)  # [12,7,-1]
# print(list_6.pop())  # -1
# print(list_6)  # [12,7]

# # удаление конкретного элемента списка
# list_7 = [12, 7, -1, 21, 0]
# print(list_7.pop(0))  # 12
# print(list_7)  # [7,-1,21,0]

# # добавление элемента на нужную позицию
# list_8 = [12, 7, -1, 21, 0]
# print(list_8.insert(2, 11))
# print(list_8) # [12,7,11,-1,21,0]

#                         # Срезы в списках
# list_9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_9[0])                        # 1
# print(list_9[1])                        # 2
# print(list_9[len(list_9)-1])            # 10
# print(list_9[-5])                       # 6
# print(list_9[:])                        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_9[:2])                       # [1, 2]
# print(list_9[len(list_9)-2:])           # [9, 10]
# print(list_9[2:9])                      # [3, 4, 5, 6, 7, 8, 9]
# print(list_9[6:-18])                    # []
# print(list_9[0:len(list_9):6])          # [1, 7] шаг
# print(list_9[::6])                      # [1, 7]

# # кортежи

# t = ()
# print(type(t))
# t = (1, )  # в конце ставить запятую
# print(type(t))

# v = [1, 8, 9]
# print(v)
# print(type(v))
# v = tuple(v)
# print(type(v))
# print(v)

# # a,b = 1, 2
# # a = b = 1 # множественное присваивание
# a, b, c = v
# print(a, b, c)

# t = (1, 2, 3, 5,)

# for i in range(len(t)):
#     print(t[i])

# t = (1, 2, 3, 5,)
# # t[0] = 2  # с кортежем не получится присвоить новое значение
# a = [1, 2, 3, 5]
# a[0] = 2 # со списком такое можно сделать
# print(a)

# # Словари

# d = {}
# d = dict()

# d['q'] = 'qwerty' # присвоение ключа и значения
# print(d)
# d['w'] = 'werty'
# print(d)
# print(d['q']) # вывод значение по ключу

# dictionary = {}
# dictionary = {'up':'|', 'left':'<-', 'down':"v", 'right':'->'}
# print(dictionary)
# print(dictionary['left']) # <-
# # типы ключей могут отличаться
# dictionary['left'] = '<<-'
# print(dictionary['left']) # <<-
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary:
#     print('{}:{}'.format(item,dictionary[item]))
# for (k,v) in dictionary.items():
#     print(k,v)
# up: |
# down: v
# right: ->
# dictionary[895] = 98998
# print(dictionary)
# print(dictionary.items())

# # Множества

# colors = {'red', 'green', 'blue'}
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors)  # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors)  # {'gray', 'red', 'green', 'blue'}
# colors.remove('red')
# print(colors)  # {'gray', 'green', 'blue'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red')  # ok для избежания ошибки сверху
# print(colors)  # {'gray', 'green', 'blue'}
# colors.clear()  # { }
# print(colors)  # set()

# q = set()  # еще один способ создания множества

# a = {1, 2, 3, 5, 8}
# b = {3, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8} копия
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21} объединение(уникальные значения)
# i = a.intersection(b)  # i = {8, 2, 5} пересечение множеств
# # dl = {1, 3} разность множеств, из а вычитаем одинаковые значения b
# dl = a.difference(b)
# # dr = {13, 21} разность множеств, из b вычитаем одинаковые значения а
# dr = b.difference(a)
# # {1, 21, 3, 13} все идет по порядку, в скобках первое действие
# q = a.union(b).difference(a.intersection(b))

#                         # замороженное множество

# a = {1, 8, 6}
# b = frozenset(a)  # не можем изменять
# print(b)
# from random import randint

# #                         # List Comprehension

# # list_1 = [exp for item in iterable]
# list_1 = [i for i in range(1, 10)]  # создание списка
# print(list_1)
# list_2 = [i for i in range(1, 10) if i % 2 == 0]  # с условием
# print(list_2)
# list_3 = [(i, i) for i in range(1, 10) if i % 2 == 0] # с созданием пар(кортежей)
# print(list_3)
# list_4 = [i*2 for i in range(10) if i%2==0] # можно делить, умножать, прибавлять, вычитать
# print(list_4)
# list_5 = [randint(1,10) for i in range(10)]
# print(list_5)

#                         # Профилирование и отладка

# # SyntaxError(Синтаксическая ошибка)
# number_first = 5
# number_second = 7
# if number_first>number_second # !!!!
#     print(number_first)
# # Отсутствует :

# number_first = 5
# number_second = 7
# if number_first>number_second: # решение ошибки поставили :
#     print(number_first)

# # IndentationError(Ошибка отступов)
# number_first = 5
# number_second = 7
# if number_first>number_second: # !!!!
# print(number_first)
# # Отсутствие отступов

# number_first = 5
# number_second = 7
# if number_first>number_second: # решение ошибки, поставили отступ
#   print(number_first)

# # TypeError(Типовая ошибка)
# text = 'Python'
# number = 5
# print(text+number)
# # Нельзя складывать строки и числа

# text = 'Python'
# number = '5' # перевели инт в строку
# print(text+number)

# # ZeroDivisionError
# number_first = 5
# number_second = 0
# print(number_first/number_second)
# # Делить на 0 нельзя

# number_first = 5
# number_second = 1 # поменять значение
# print(number_first/number_second)

# # KeyError(Ошибка ключа)
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа нет

# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[2]) # либо добавить нужное значение в словарьБ либо вывести существуещее значение

# # NameError(Ошибка имени переменной)
# name = 'Ivan'
# print(names)
# # Переменной names не существует

# name = 'Ivan'
# print(name) # убрать опечатку

# # ValueError(Ошибка значения)
# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые числа

# text = '555' # написать цифры
# print(int(text))