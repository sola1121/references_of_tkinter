# coding: utf-8

import tkinter

i = 0

main_screen = tkinter.Tk()
main_screen.title('菜单')
main_screen.geometry('300x200')

label = tkinter.Label(main_screen, text='', width=30, height=1)
label.pack()

def do_job():
    global i
    label.config(text='do ' + str(i))
    i += 1

menu_bar = tkinter.Menu(main_screen)

filemenu = tkinter.Menu(menu_bar, tearoff=0)   # tearoff 能否被分开
menu_bar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()   # 添加分开的线
filemenu.add_command(label='Exit', command=main_screen.quit)   # 点退出

editmenu = tkinter.Menu(menu_bar, tearoff=0)   # tearoff 能否被分开
menu_bar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Paste', command=do_job)
editmenu.add_separator()   # 添加分开的线

submenu = tkinter.Menu(editmenu)
editmenu.add_cascade(label='Help', menu=submenu, underline=0)
submenu.add_command(label='detail', command=do_job)


main_screen.config(menu=menu_bar)

main_screen.mainloop()