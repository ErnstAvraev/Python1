# print(5)
# print(5, 8, 6, sep=',')

# n = 5


# n = None

# n = 'fdff'
# n1 = "vvssfxs"
# print(n)

# m = 5
# m = 'fdfd\'asd'
# print(type(m))
# print(m)

# print(5)
# print(5)
# # print(5, 8)
# '''
# print(5)
# print(5, 9)
# '''

# a = 5
# b = 5.89
# c = 'hello'

# print(a, '-', b, '-', c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))


# print('введите первое число: ')
# a = int(input())

# b = int(input("введите второе число: "))
# print(a, ' + ', b, ' = ', a + b)

# c = 5.98
# print(c)
# print(type(c))
# n = int(c)
# print(type(n))
# print(n)

# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))

# a = 5.9768
# b = 7.987609
# print(round(a*b,2))

# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter = iter - 4
# iter *= 5  # iter = iter * 5
# iter /= 6  # iter = iter / 6
# iter //= 5  # iter = iter // 5
# iter %= 5  # iter = iter % 5
# iter **= 5  # iter = iter ** 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# # if, elif, else

# username = input('Введите имя: ')
# temp = username.lower()
# if temp == 'маша':
#     print('Ура, это же МАША!')
# elif temp == 'марина':
#     print('Я так ждал вас Марина!')
# elif temp == 'ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# while, while-else

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break
#     i += 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# Метод флажка

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         flag = False  # если остаток при делении числа n на i равен 0
#         print(i)
#     elif i > n//2:  # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1


# for, range


# a = 'qwerty'

# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(len(text))  # количество символов в строке
# print('еще' in text)  # проверка есть ли значение в строке
# print(text.lower())  # все в нижнем регистре
# print(text.upper())  # все в верхнем регистре
# print(text.replace('еще', 'ЕЩЕ'))  # замена

# # Срезы

# text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(text[0]) # С
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # СъЕШЬ еще этих МяГкИх французских булок
# print(text[:2]) # Съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ЕШЬ еще
# print(text[6:-18]) # еще этих МяГкИх
# print(text[0:len(text):6]) # Сеикакл
# print(text[::6]) # Сеикакл
# text = text[2:9] + text[-5] + text[:2]
# print(text)