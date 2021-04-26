import tkinter as tk

def add_label():
    label = tk.Label(win, text='new')
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f'Счетчик {count}' # при каждом нажатии счетчик будет увеличиваться на единицу.
win = tk.Tk() #виджет button
win.geometry("200x300+100+200")
win.title('privet')
btn1 = tk.Button(win,text='knopka',
                 command = функция)
#1 аргумент в каком окне, далее текст, уже два эти аргумента сделают
#кнопку, далее сложнее
btn1.pack() # чтобы появилась кнопка
#в command передается функция, которая запускает функции, которую мы переводим
btn2 = tk.Button(win,text='knopka',
                 command = add_label) #будет добавлять label
btn2.pack()

btn3 = tk.Button(win,text =f'Счетчик {count}')
# у кнопки также множество аргументов:
# bg = 'red'
#можем зажать на контрол, нажать на Button и мы провалимся во внутренние
# аргументы, которые можем применять к кнопке
# например activebackground = 'blue' - изменение цвета кнопки после нажатия
# state = tk.DISABLED, выключает активность кнопки, можно сделать кнопку которая будет выключать все сразу(попробовать дома)


# функция, которая выключает все кнопки
def fstat():
    bstat = btn4['state']
    if bstat == 'normal':
        bstat = 'disabled'
    elif bstat == 'disabled':
        bstat = 'normal'
    btn1['state'] = btn2['state'] = btn3['state'] = btn4['state'] = bstat
    btn5['text'] = f'button stat {bstat}'

#------------
btn5 = tk.Button(win, text=f'buttons is normal',
                 command=fstat
                 )
#------------
btn5.pack()
win.mainloop()