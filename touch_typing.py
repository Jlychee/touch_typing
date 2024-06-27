# with open(r"C:\Users\Катя\PycharmProjects\pythonProject\db1.txt", 'w', encoding='UTF-8') as f:
#     data = open(r"C:\Users\Катя\PycharmProjects\pythonProject\db.txt", encoding='UTF-8').read().split('.')
#     for i in range(len(data) - 1):
#         data[i] = data[i].strip('\n')
#         if '!' in data[i]:
#             f.write(f"{data[i].split('!')[0]}!\n")
#             f.write(f'{data[i].split("!")[1]}.\n')
#         else:
#             f.write(f'{data[i].lstrip()}.\n')
#     f.write(f'{data[-1].lstrip()}.')

def add_pos_args(to_f):
    return lambda *args: to_f()


import random
import time

data = [i for i in open('db.txt', encoding='UTF-8').readlines()]
mistake = 0
t = time.time()

from tkinter import *

root = Tk()
root.config(background='#323437')
root.title('Typing Speed Test')
root.resizable(False, False)
root.geometry('1280x600+400+200')

@add_pos_args
def end():
    exit()

@add_pos_args
def end_of_input():
    global result, btn, btn_exit
    label.destroy()
    field.destroy()
    if mistake <= 2:
        msg = 'Отличный результат!! Так держать!!'
    elif 3 <= mistake <= 5:
        msg = 'Неплохо, но ты можешь лучше!'
    else:
        msg = 'Тренеруйся дальше, и все обязательно получиться!♥'

    msg_label = Label(root,
                      text=msg,
                      bg='#323437',
                      fg='#eeba00',
                      font=('VAG World Bold', '25', 'bold'),
                      height=1,
                      width=50,
                      )
    result = Label(root,
                   text=f'Количество ошибок: {mistake}\n'
                        f'Скорость печати: {(ln - mistake) / ((time.time() - t) / 60):.02f} зн/мин',
                   font=('VAG World Bold', '25', 'bold'),
                   bg='#323437',
                   fg='#eeba00',
                   height=2,
                   width=35
                   )
    btn = Button(root, text='Попробовать еще раз',
                 bg='#eeba00',
                 activebackground='#bb9200',
                 fg='#464646',
                 font=('AG World Bold', '30', 'bold'),
                 command=start,
                 )
    btn_exit = Button(root, text='Закончить',
                      bg='#eeba00',
                      activebackground='#bb9200',
                      fg='#464646',
                      font=('AG World Bold', '30', 'bold'),
                      command=end,
                      )

    msg_label.grid(row=0, column=0, padx=190, pady=[90, 0])
    result.grid(row=1, column=0, pady=[10, 10])
    btn.grid(row=2, column=0)
    btn_exit.grid(row=3, column=0)


def is_right(p):
    fl = True
    if fl:
        field['fg'] = '#d9d9d9'
    else:
        field['fg'] = 'red'
    i = len(p) - 1
    try:
        if p[-1] == original_text[i]:
            return True
        else:
            fl = False
            global mistake
            mistake += 1
            field['fg'] = 'red'
            return True
    except IndexError:
        return True


def start():
    global original_text, label, field, mistake, ln
    try:
        result.destroy()
        btn.destroy()
        btn_exit.destroy()
        mistake = 0
    except NameError:
        mistake = 0
    original_text = random.choice(data)
    ln = len(original_text) - original_text.count(' ')
    label = Label(text=original_text,
                  bg='#323437',
                  fg='#c2c2c2',
                  font=('VAG World Bold', '25', 'bold'),
                  wraplength=1260,
                  justify=CENTER
                  )
    field = Entry(bg='#323437',
                  cursor='xterm',
                  fg='#d9d9d9',
                  width=900,
                  font=('VAG World Bold', '25', 'bold'),
                  validate='key',
                  validatecommand=field_check,
                  )
    label.place(x=30, y=15)
    field.place(x=10, y=350, width=1260, height=100)
    field.bind('<Return>', end_of_input)
    field.focus_set()
    btn_start.destroy()


field_check = (root.register(is_right), "%P")

btn_start = Button(root, text='START',
                   bg='#eeba00',
                   activebackground='#bb9200',
                   activeforeground='#ababab',
                   fg='#ffffff',
                   font=('Espion Rounded', '30', 'bold'),
                   command=start,
                   )
btn_start.pack(expand=True)

root.mainloop()
