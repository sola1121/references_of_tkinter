# coding: utf-8

import tkinter

from tkinter import *

on_hit = False

main_screen = tkinter.Tk()
main_screen.title('标签和按钮')
main_screen.geometry('600x400+500+250')  # 界面大小与位置

varStr = tkinter.StringVar()   # 在界面创建后创建在main_screen上的变量

label = tkinter.Label(main_screen, textvariable=varStr, bg='green',font=('Arial',12), width = 15, height = 2)  # 标签
label.pack()

def hit_me():
    global on_hit   # 定义全局变量
    if on_hit == False:
        on_hit = True
        varStr.set('you hit me!')   # 在显示框内赋值，用set
    else:
        on_hit = False
        varStr.set('')

button = tkinter.Button(main_screen, text='hit me', width=15, height=2, command=hit_me)   # 按钮
button.pack()

button.config(state='active')

Button(main_screen,text = 'FLAT',relief=FLAT).pack()
Button(main_screen,text = 'GROOVE',relief=GROOVE).pack()
Button(main_screen,text = 'RAISED',relief=RAISED).pack()
Button(main_screen,text = 'RIDGE',relief=RIDGE).pack()
Button(main_screen,text = 'SOLID',relief=SOLID).pack()
Button(main_screen,text = 'SUNKEN',relief=SUNKEN).pack()


main_screen.mainloop()
