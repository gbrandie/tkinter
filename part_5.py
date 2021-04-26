import tkinter as tk # в данной части поговорим про метод Entry
# он нужен для создания полей ввода

def delete_entry():
    name.delete(0)#удаляет по индексу
    name.delete(1,5)#удаляет диапазон
    name.delete(1,'end') #от 1 до конца

def tkinsert():
    name.insert(0,'hello') #вставляет на позицию строку
win = tk.Tk() #в
win.geometry("200x300+100+200")
win.title('privet')
name = tk.Entry(win)
name.grid(row=0,column = 1)
tk.Label(win,text='Имя').grid(row=0,column=0,stick = 'w')
tk.Button(win,text='getinfo',command=name.get())
win.grid_columnconfigure(0,minsize=50)
win.grid_columnconfigure(1,minsize=100)
win.mainloop()
#cоздать функцию вывод .get в command у баттона
#создать функцию удаления
#аргумент show='*' при создании entry скрывает написанные символы
#сделать конпку submit которая принтит все