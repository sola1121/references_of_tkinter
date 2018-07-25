# coding: utf-8

import tkinter
import sys
import os

# 报substring not found 的错误
# 存在的改进方向：不知道用何种方式打开磁力链接

from tkinter import messagebox

magnet_whole = ''
magnet_str = "magnet:?xt=urn:btih:"

main_window = tkinter.Tk()
main_window.title('magnetOpen')
main_window.geometry('500x100')
main_window.resizable(0, 0)

var_str = tkinter.StringVar()
var_str.set('')

var_ck = tkinter.IntVar()

label = tkinter.Label(main_window, text=magnet_str).place(x=20, y=5)

entry = tkinter.Entry(main_window, textvariable=var_str, width=50).place(x=22, y=35)

def click():
    global magnet_whole
    global magnet_str
    try:
        magnet_hash = str(var_str.get())
        if var_ck.get() == 1:
            var_str.set('')
        if magnet_hash.index("magnet:?xt=urn:btih:") > -1:
            magnet_whole = magnet_hash
        else:
            magnet_whole = magnet_str + str(magnet_hash)
            print(magnet_whole)
    except:
        info = sys.exc_info()
        info_list = list(info)
        messagebox.showerror(title='Error', message=info_list[1])

bnt = tkinter.Button(main_window, text='确认链接', width=9, command=click).place(x=400, y=30)

ck = tkinter.Checkbutton(main_window, text='自动清除', variable=var_ck, onvalue=1, offvalue=0).place(x=395, y=65)

main_window.mainloop()