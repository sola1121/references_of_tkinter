# coding: utf-8

import tkinter

main_screen = tkinter.Tk()
main_screen.title('放置位置')
main_screen.geometry('600x400+500+250')

label1 = tkinter.Label(main_screen, text='top', bg='red').pack(side='top')
label2 = tkinter.Label(main_screen, text='left', bg='red').pack(side='left')
label3 = tkinter.Label(main_screen, text='right', bg='red').pack(side='right')
label4 = tkinter.Label(main_screen, text='bottom', bg='red').pack(side='bottom')

"""
for x in range(4):
    for y in range(3):
        tkinter.Label(main_screen, text=1).grid(row=x, column=y, padx=10, pady=10)
"""

tkinter.Label(main_screen, text='place(300, 200)', bg='Black').place(x=300,y=200,anchor='nw')

main_screen.mainloop()