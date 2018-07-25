# coding: utf-8

import tkinter

main_screen = tkinter.Tk()
main_screen.title('输入和文本')
main_screen.geometry('200x200')

entry = tkinter.Entry(main_screen, show='*')
entry.pack()

text = tkinter.Text(main_screen, height=2)
text.pack()

def insert_point():
    """插入到指针所在位置"""
    var = entry.get()
    print(var)
    text.insert('insert', var)

def insert_endline():
    """插入到文本尾"""
    var = entry.get()
    print(var)
    text.insert('end', var)

button1 = tkinter.Button(main_screen, text='insert point', command=insert_point)   # 按钮
button1.pack()

button2 = tkinter.Button(main_screen, text='insert endline', command=insert_endline)
button2.pack()

main_screen.mainloop()