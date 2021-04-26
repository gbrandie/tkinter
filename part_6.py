import tkinter as tk
import tkcalendar as tkcal
win = tk.Tk() #в
win.geometry("600x400+100+200")
win.title('privet')
cal = tkcal.Calendar(win)
cal.pack()
win.mainloop()