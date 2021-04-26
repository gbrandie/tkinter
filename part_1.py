import tkinter as tk
win = tk.Tk() # создание главного окна
win.mainloop() # загрузка главного окна и переход в режим ожидания
#мы можем менять размеры окна мышкой, но пока что ничего более мы не описали
#mainloop должен быть в самом конце как я понял
win.title('Мой первый проект') # название заголовка (изначально tk)
win.geometry("500x600+100+200") # стартовое разрешение, плюсами указывается расположение окна от левого верхнего угла
win.resizable(True,True) # возможность изменять размер мышкой по ширине и высоте
win.minsize(300,400) # минимальный размер в пикселях окошка по ширине и высоте (если конечно разрешено это делать)
# photo = tk.PhotoImage(file='fun.png')
#win.iconphoto(False, photo) установка логотипа
win.config(bg='red') #цвет фона от англ бэкграунд