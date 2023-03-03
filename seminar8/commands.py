import globals as g

g.input_str = ''

def help_output(help_dict):
    for k,v in help_dict.items():
        print('{0:8s}:{1}'.format(k,v))

def quit_mess():
    print('Бот завершил свою работу!')
    print("До новых встреч!")
    with open('phones.json','w') as f:
        f.write(g.input_str)
    exit()

def add():
    pass