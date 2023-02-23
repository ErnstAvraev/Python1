# sp = [i for i in range(11)]
# print(sp)

# print(sp[-1])

# print(sp[1:3]) # срез

# sp2 = sp[:] # копирование списка

# sp[0] = 999

# print(sp2[3:])
# print(sp2[3::2])

# # Задача No25. Решение в группах
# # Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз
# # каждый символ уже встречался. Количество повторов добавляется к символам
# # с помощью постфикса формата _n.
# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# # Для решения данной задачи используйте функцию .split()

# stroka = input("input: ")
# sp = stroka.split()
# print(sp)
# score = 0
# many_letters = set()
# for i in stroka:
#     many_letters.add(i)
# print(many_letters)
# for i in many_letters:
#     for j in range(len(sp)):
#         if i == sp[j]:
#             score += 1
#             if score >= 2:
#                 sp[j] = sp[j]+'_'+str(score-1)
#     score = 0
# print(' '.join(sp))

# # Задача No27. Общее обсуждение
# # Пользователь вводит текст(строка). Словом считается последовательность
# # непробельных символов идущих подряд, слова разделены одним или большим числом
# # пробелов или символами конца строки.Определите, сколько различных слов содержится
# # в этом тексте.
# # Input: She sells sea shells on the sea shore;The shells that she sells are sea
# # shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the
# # shells are sea shore shells.
# # Output: 19

# stroka = "She sells sea shells on the sea shore;The shells that she sells are sea \
# shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the \
# shells are sea shore shells."
# signs = ['.', ',', ';']
# for z in signs:
#     stroka = stroka.replace(z, ' ')
# lst = set(stroka.lower().split())
# print(len(lst))

# stroka = str(input(": ")).replace('.',' ').replace(',',' ').replace(';',' ').lower()
# stroka = "She sells sea shells on the sea shore;The shells that she sells are sea \
# shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the \
# shells are sea shore shells.".replace('.',' ').replace(',',' ').replace(';',' ').lower()
# # lst = set(stroka.split())
# print(len(lst))
# print(len(set(stroka.split())))

# # Задача No29.
# # Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# # “Задана последовательность неотрицательных целых чисел. Требуется определить 
# # значение наибольшего элемента последовательности, которая завершается первым 
# # встретившимся нулем (число 0 не входит в последовательность)”. 
# # Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца 
# # сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и 
# # выиграл спор. За помощью товарищи обратились к Вам, студентам.

# # Ваня: 
# n = int(input())
# max_number = n
# while n != 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)

# # Петя:
# n = int(input())
# max_number = n
# while n > 0:
#     n = int(input())
#     if max_number < n:
#         max_number = n
# print(max_number)