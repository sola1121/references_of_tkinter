# coding: utf-8

import tkinter

main_screen = tkinter.Tk()
main_screen.title('选择按钮')
main_screen.geometry('300x200')

varStr = tkinter.StringVar()

label = tkinter.Label(main_screen,textvariable=varStr, bg='yellow', width=15, height=1)
label.pack()

def option_select():
    label.config(text=varStr)    # 使用label的配置参数函数重新为text赋值


# variable是改变的变量,value是这变量的新值
radiobutton1 = tkinter.Radiobutton\
    (main_screen, text='Option1', variable=varStr, value='1 has be selected', command=option_select)
radiobutton1.pack()
radiobutton2 = tkinter.Radiobutton\
    (main_screen, text='Option2', variable=varStr, value='2 has be selected', command=option_select)
radiobutton2.pack()
radiobutton3 = tkinter.Radiobutton\
    (main_screen, text='Option3', variable=varStr, value='3 has be selected', command=option_select)
radiobutton3.pack()


button = tkinter.Button(main_screen, text='nothing will happen', height=1)
button.pack()


main_screen.mainloop()