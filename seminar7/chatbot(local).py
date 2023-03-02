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
        print("Бот фильмотека начал свою работу")
    elif command == "/stop":
        print("Бот остановил свою работу. Заходите еще, будем рады!)")
        break
    else:
        print("Неопознаная команда. Просьба изучить мануал через /help")