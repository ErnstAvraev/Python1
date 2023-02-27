# lambda - для создания анонимных маленьких функций
# map - применяет функцию к списку или словарю, возвращает измененный обьект
# filter - применяет логическую функцию к списку или словарю, возвращает элементы,
# которые удовлетворяют условие
# zip - создает кортежи из элементов словарей или списков
# list comprehension - удобная генерация списков

# #                                       lambda

# add = lambda x, y : x * 80 * y

# print(add(2, 3)) # результат 480

# #                                       map

# def multiply(x):
#     return x * 2


# print(list(map(multiply, [1, 2, 3, 4]))) # вернет [2, 4, 6, 8]

# #                                       filter

# dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

# # вернет  [{'name' : 'python', 'points' : 10}]
# res = list(filter(lambda x: x['points'] == 'python', dict_a))

# print(res)

# dict_b = [i for i in range(10)]
# res = list(filter(lambda x: x % 2 == 0, dict_b))
# print(dict_b)
# print(res)

# #                                       zip

# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']
# for i, j in zip(a, b):
#     print(i, j)

# #                                         enumerate

# spisok = [16, 46, 26, 36]
# for i in enumerate(spisok):
#     print(i)

# #                                         list comprehension

# squares = [x**2 for x in range(10)]

# odds = [x for x in range(10) if x % 2 != 0]

# sp = [x - 10 for x in squares]

# print(squares)
# print(odds)
# print(sp)


# # Задача No47
# # У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы
# #  используется множество раз и вы не хотите ничего сломать):
# # transformation = <???>
# # values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# # transormed_values = list(map(transformation, values))
# # Единственный способ вашего взаимодействия с этим кодом - посредством задания функции
# # transformation.
# # Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список
# # значений, а нужно получить его как есть.
# # Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией
# # values.
# # Ввод:
# # values = [1, 23, 42, ‘asdfg’]
# # transformed_values = list(map(trasformation, values)) if values == transformed_values:
# # print(‘ok’) else:
# # print(‘fail’)
# # Вывод:
# # ok

# from math import pi
# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda x: x, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')

# # values = [1, 23, 42, 'asdfg']
# # transformation = lambda x : x
# # transformed_values = list(map(transformation, values))
# # res = list(filter(lambda x: x[0] == x[1], zip(values, transformed_values)))
# # if res == transformed_values:
# #     print('ok')
# # else:
# #     print('fail')

# # Задача No49. Решение в группах
# # Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# # орбита которой имеет самую большую площадь. Напишите функцию
# # find_farthest_orbit(list_of_orbits), которая среди списка орбит планет найдет ту, по
# # которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что
# # у вашей звезды таких планет нет, зато искусственные спутники были были запущены на круговые
# # орбиты. Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты
# # самой далекой планеты. Каждая орбита представляет из себя кортеж из пары чисел - полуосей
# # ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей
# # эллипса. При решении задачи используйте списочные выражения. Подсказка: проще всего будет
# # найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и
# # сам эллипс, имеющий такую площадь. Гарантируется, что самая далекая планета ровно одна
# # Ввод:
# # orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# # print(*find_farthest_orbit(orbits))
# # Вывод:
# # 2.5 10

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# square_ellips = [pi*ell[0]*ell[1] for ell in orbits]
# find_farthest_orbit = lambda x : x.index(max(x))
# print(square_ellips)
# print(find_farthest_orbit(square_ellips))
# # >>> lst = [1, 3, 6, 8, 3, 23, 6, 8, 5, 3, 45, 6, 8, 5, 3]
# # >>> print(lst.index(max(lst)))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def orbita(array):
#     maxi_orbit = 0
#     for i in range(len(array)):
#         for j in range(0,2):
#             if j == 0:
#                 x = array[i][j]
#             y = array[i][j]
#             if x != y:
#                 S = lambda x,y: 3.14 * x * y
#                 if maxi_orbit < S(x,y):
#                     maxi_orbit = S(x,y)
#                     orb = i
#     return orb
# print(orbits[orbita(orbits)])


# # Задача No51. Решение в группах
# # Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют 
# # одинаковое значение некоторой характеристики, и возвращают True, если это так. Если 
# # значение характеристики для разных объектов отличается - то False. Для пустого набора 
# # объектов, функция должна возвращать True. Аргумент characteristic - это функция, которая 
# # принимает объект и вычисляет его характеристику.
# # Ввод: 
# # values = [0, 2, 10, 6] 
# # if same_by(lambda x: x % 2, values):
# #   print(‘same’) 
# # else:
# #   print(‘different’)
# # Вывод: same

# def same_by(characteristic, objects):
#     s = set([characteristic(x) for x in objects])
#     if len(s) == 1:
#         return True
#     else:
#         return False


# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#   print('same') 
# else:
#   print('different')