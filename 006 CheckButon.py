# coding: utf-8

import tkinter

main_screen = tkinter.Tk()
main_screen.title('勾选项')
main_screen.geometry('200x100')

varInt1 = tkinter.IntVar()
varInt2 = tkinter.IntVar()


label = tkinter.Label(main_screen, bg='yellow', width=15, height=1)
label.pack()


def check_value():
    if varInt1.get() == 1 and varInt2.get() == 1:
        label.config(text='I love both.')
    elif varInt1.get() == 0 and varInt2.get() == 1:
        label.config(text='I love C++ only.')
    elif varInt1.get() == 0 and varInt2.get() == 0:
        label.config(text='I hate them.')
    elif varInt1.get() == 1 and varInt2.get() ==0:
        label.config(text='I love Python only.')


ckButton1 = tkinter.Checkbutton\
    (main_screen, text='Python', variable=varInt1, onvalue=1, offvalue=0, command=check_value)
ckButton1.pack()
ckButton2 = tkinter.Checkbutton\
    (main_screen, text='C++', variable=varInt2, onvalue=1, offvalue=0, command=check_value)
ckButton2.pack()

# onvalue 选中时赋予variable变量的值
# offvalue 未选中时赋予variable变量的值


main_screen.mainloop()



