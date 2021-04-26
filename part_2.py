import tkinter as tk
win = tk.Tk() #виджет label
win.geometry("200x300+100+200")
win.title('privet')
label_1 = tk.Label(win, text='hello',
                   bg = 'red',fg = 'white')
#первый аргумент - в каком окне будет, второй аргумент - сам текст
label_1.pack() #расположить элемент на экран
# аргументы внутри label, fg - фон шрифта, font=('Arial',20,'bold)
#padx = 10 отступ по иксу pady отступ лэйбла по y
#width - ширина лэйбла по количеству знаков
#height - высота лэйбла по количеству знаков
# по умолчанию текст выставляется по центру
# anchor = 'n' - прикрепить текст внутри лейбла по стороне света
# padx pady делает отступ от стороны света anchor
# relief = tk.RAISED - установка границы, bd - размер границы
# justify - выравнивание текста от границы (как в ворде)
#tk.LEFT, tk.CENTER итд













win.mainloop()