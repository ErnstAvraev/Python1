from random import *
import json
films = []


def save():
    with open("films.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(films, ensure_ascii=False))
        print("Наша фильмотека была успешно сохранена в файле films.json")


def load():
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека успешно загружена!")


try:
    with open("films.json", "r", encoding="utf-8") as fh:
        films = json.load(fh)
    print("Фильмотека успешно загружена!")
except:
    films.append("матрица")
    films.append("солярис")
    films.append("властелин колец")
    films.append("техасская резня бензопилой")
    films.append("санта барбара")


while True:
    command = input("Введите команду: ")
    if command == "/start":
        print("Бот фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот остановил свою работу. Заходите еще, будем рады!)")
        break
    elif command == "/all":
        print("Вот текущий список фильмов")
        print(films)
    elif command == "/add":
        f = input("Введите название фильма: ").lower()
        films.append(f)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command == "/help":
        print("/start - запустить бота\n"
              "/stop - остановить работу бота\n"
              "/all - показать всю фильмотеку\n"
              "/add - добавить фильм в фильмотеку\n"
              "/delete - удалить фильм из фильмотеки\n"
              "/random - выбрать случайный фильм\n"
              "/save - сохранить изменения в фильмотеке\n"
              "/load - загрузить значения из фильмотеки")
    elif command == "/delete":
        f = input("Введите название фильма, который хотите удалить: ").lower()
        '''
        if f in films:
            films.remove(f)
            print("Фильм был успешно удален!")
        else:
            print("Данного фильма нет в фильмотеке!")
        '''
        try:
            films.remove(f)
            print("Фильм был успешно удален!")
        except:
            print("Данного фильма нет в фильмотеке!")
    elif command == "/random":
        # rnd = randint(0, len(films)-1)
        # print("Слепой жребий показал вам фильм - " + films[rnd])
        print("Слепой жребий показал вам фильм - " + choice(films))
    elif command == "/save":
        save()
    elif command == "/load":
        with open("films.json", "r", encoding="utf-8") as fh:
            films = json.load(fh)
        print("Фильмотека успешно загружена!")

    else:
        print("Неопознаная команда. Просьба изучить мануал через /help")
