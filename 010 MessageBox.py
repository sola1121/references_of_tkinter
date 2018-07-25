# coding: utf-8

import tkinter
from tkinter import messagebox

reback = ''

main_screen = tkinter.Tk()
main_screen.title('消息窗口')
main_screen.geometry('300x300+650+200')

def click():
    """messagebox 都是有返回值的，为字符串或布尔值"""
    global reback
    # messagebox.showinfo(title='showinfo', message='用于显示提示信息')
    # messagebox.showwarning(title='showwarning', message='用于显示警告信息')
    # messagebox.showerror(title='showerror', message='用于显示错误信息')
    # reback = messagebox.askquestion(title='askquestion', message='进行提问') # return 'yes', 'no'
    # reback = messagebox.askyesno(title='askyesno', message='询问True或False')  # return 'True', 'False'
    # reback = messagebox.askokcancel(title='askokcancel', message='询问ok或cancel')
    # reback = messagebox.askretrycancel(title='askretrycancel', message='询问retry或cancel')
    reback = messagebox.askyesnocancel(title='askyesnocancel', message='询问yes，no，或cancel')
    label.config(text=reback)

label = tkinter.Label(main_screen, text='', width=15, height=1, bg='red')
label.pack()

button = tkinter.Button(main_screen, text='MsgBox', command=click)
button.pack()


main_screen.mainloop()