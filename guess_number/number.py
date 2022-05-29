#! /usr/bin/env python

import tkinter.messagebox
from random import randint
from tkinter import *


def game_exit():
    choice = tkinter.messagebox.askyesno('Выход', 'Вы действительно хотите выйти?')
    if choice:
        root.destroy()


def game_info():
    tkinter.messagebox.showinfo('О программе', '"Угадай число"\nПростая программа, написана на Python.'
                                               '\n Ваша задача за наименьшее количество ходов отгадать '
                                               'число, загаданное вашим железным другом.\nЖелаем удачи!')


def game_start(*args):
    number_user = str(user_number.get())
    # counter += 1
    if number_user.isdigit():
        if 0 < int(number_user) < 101:
            number_user = int(number_user)
            if number_user < number_rand:
                answer.set(f'Ваше число меньше загаданного, попробуйте еще разок')
            elif number_user > number_rand:
                answer.set(f'Ваше число больше загаданного, попробуйте еще разок')
            else:
                # if counter % 100 // 10 == 1 or counter % 10 in (0, 5, 6, 7, 8, 9):
                #     ending = 'ов'
                # elif counter % 10 in (2, 3, 4):
                #     ending = 'а'
                # else:
                #     ending = ''
                # answer.set(f'Поздравляем! Вы отгадали число за {counter} ход{ending}.')
                answer.set(f'Поздравляем! Вы отгадали число.')
    else:
        answer.set(f'А может быть все-таки введем целое число от 1 до 100?')


root = Tk()
root.title('Угадай число')
root.geometry(f'700x300')
root.resizable(False, False)
root.tk.call('wm', 'iconphoto', root, PhotoImage(file='resources/numbers.png'))
# ====================
# menu_bar = Menu(root, activebackground='#6094cf', activeforeground='#f5f6f7', bg='#dee0e2', border=0,
#                 font=('Droid Sans', 12))

# file_menu = Menu(menu_bar, activebackground='#6094cf', activeforeground='#f5f6f7', bg='#dee0e2', borderwidth=1,
#                  tearoff=0, font=('Droid Sans', 12))
# file_menu.add_command(label='Новая игра', command=game_start)
# # file_menu.add_separator()
# file_menu.add_command(label='Инфо', command=game_info)
# file_menu.add_separator()
# file_menu.add_command(label='Выйти', command=game_exit)
# menu_bar.add_cascade(label='Игра', menu=file_menu)
# root.configure(menu=menu_bar)

main_frame = Frame(root, bg='#eff0f1')
main_frame.pack(padx=1, pady=1, expand=1, fill=BOTH)

greetings = Frame(main_frame, bg='#eff0f1')
greetings.pack(ipady=10, expand=0, fill=X)
Label(greetings, text='Добро пожаловать в игру\n"Угадай число"', font=('Droid Sans', 16), bg='#eff0f1').pack()
Label(greetings, height=1, bg='#eff0f1').pack()
Label(greetings, text='Загадано число от 1 до 100.\n Ваша задача за наименьшее количество ходов отгадать это число.',
      font=('Droid Sans', 12), bg='#eff0f1').pack()

user_frame = Frame(main_frame, bg='#eff0f1', width=50)
user_frame.pack(pady=10, anchor=CENTER)
Label(user_frame, width=30, bg='#eff0f1', text='Введите свой вариант числа:', font=('Droid Sans', 12)).grid(row=0,
                                                                                                            column=0)

user_number = StringVar()
user_number = tkinter.Entry(user_frame, textvariable=user_number, width=4, font=('Droid Sans', 14), )
user_number.grid(row=0, column=1)

Label(user_frame, width=4, bg='#eff0f1').grid(row=0, column=2)
Button(user_frame, width=10, height=1, text='Проверить', font=('Droid Sans', 12), command=game_start).grid(row=0,
                                                                                                           column=3)

resolution = Frame(main_frame, bg='#eff0f1')
resolution.pack(pady=30, anchor=N, expand=1, fill=X)

answer = StringVar()
tkinter.Label(resolution, textvariable=answer, font=('Droid Sans', 14), background='#eff0f1').pack(anchor=CENTER)

number_rand = randint(1, 100)

user_number.focus()
root.bind("<Return>", game_start)

root.mainloop()
