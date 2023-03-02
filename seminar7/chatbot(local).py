from random import *
films = []
films.append("Матрица")
films.append("Солярис")
films.append("Властелин колец")
films.append("Техасская резня бензопилой")
films.append("Санта Барбара")
while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("бот фильмотека начал свою работу")
    else:
        print("Неопознаная команда. Просьба изучить мануал через /help")