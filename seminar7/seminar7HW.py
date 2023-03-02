# # Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# # разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# # Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (
# # т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может
# # состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# # Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с
# # клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# # если с ритмом все не в порядке
# # Ввод:                                  Вывод:
# # пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

# rhymes = str(input("Введите строку: "))
# vowels = ['а', 'у', 'э', 'ы', 'о', 'я', 'ю', 'е', 'и', 'ё']
# sylables = list(map(str,filter(lambda x: x in vowels, rhymes)))
# if len(sylables)%2 == 0:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# # Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# # которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# # столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые
# # должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с
# # нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два
# # аргумента, как, например, у операции умножения.
# # Ввод: Вывод:
# # 12
# # print_operation_table(lambda x, y: x * y)
# # 3456
# # 2 4 6 8 10 12
# # 3 6 9 12 15 18
# # 4 8 12 16 20 24
# # 5 10 15 20 25 30 6 12 18 24 30 36
# # print_operation_table(lambda x, y: x * y, num_rows,num_colums)
# # print_operation_table(operation, num_rows=6, num_columns=6)

# def print_operation_table(operation, rows, columns):
#     for i in range(1, rows+1):
#         print()
#         for j in range(1, columns+1):
#             print(operation(i,j), end= ' ')


# num_rows = int(input("input number of rows: "))
# num_columns = int(input("input numbers of columns: "))
# operation = lambda x,y : x*y
# print_operation_table(operation,num_rows,num_columns)

from random import *
import json

# films = []
# names = []

# def save():
#     with open("list_of_names.json", "w", encoding="utf-8") as n:
#         n.write(json.dumps(names, ensure_ascii=False))



# with open("list_of_names.json", "r", encoding="utf-8") as n:
#     names = json.load(n)
#     print("Бот начал работу. Поприветствуйте бота)")
# while True:
#     text = input(": ").lower()
#     if text == "привет" or text == "здравствуйте" or text == "здравствуй":
#         print("Здравствуйте! Меня ховут Чатик) Как вас зовут?")
#         name = input(': ')
#         if name in names:
#             print("Мы уже знакомы)")
#         else:
#             print(f'Приятно познакомиться {name}!')
#             names.append(name)
#             save()
#     elif text == "как дела?":
#         print("Как всегда отлично! Работаю без сучка, без задоринки)")
#         print("Как ваши дела?")
#         hru = input(": ").lower()
#         if hru == "отлично" or hru == "хорошо" or hru == "шикарно":
#             print("Я очень рад за вас!")
#             print("Раскажите как прошел ваш день?")
#             how_day = str(input(": ").lower())
#             if len(how_day) > 20:
#                 print("Какой насыщенный день!)")
#             else:
#                 print("Рад за вас)")
#         elif hru == "плохо" or hru == "ужасно" or hru == "не очень":
#             print("Мне очень жаль(\n"
#                 "Чем я могу вам помочь?\n"
#                 "Могу ли я предложить вам фильм, чтобы вас развеселить?")
#             question1 = input(": ").lower()
#             if question1 == "да" or "пожалуй":
#                 with open("films.json", "r", encoding="utf-8") as fh:
#                     films = json.load(fh)
#                     print("Слепой жребий показал вам фильм - " + choice(films))
#     elif text == "посоветуй фильм":
#         with open("films.json", "r", encoding="utf-8") as fh:
#                     films = json.load(fh)
#                     print("Слепой жребий показал вам фильм - " + choice(films))
#     elif text == "спасибо":
#         print("Всегда рад помочь!)")
#     elif text =="/help":
#         print("привет - запускает бот\n"
#               "пока - останавливает бот\n"
#               "как дела? - поинтересуется вашими делами)\n"
#               "посоветуй фильм - порекоментует фильм\n"
#               "спасибо - благодарность)")
#     elif text == "пока":
#         print("Пока, до скорой встречи)")
#         save()
#         break
#     else:
#         print("Неопознаная команда. Просьба изучить мануал через /help")
