# coding: utf-8


import tkinter

main_screen = tkinter.Tk()
main_screen.title('框架')
main_screen.geometry('400x300')

main_frame = tkinter.Frame(main_screen)
frame_left = tkinter.Frame(main_frame)
frame_left.pack(side='left')
frame_right = tkinter.Frame(main_frame)
frame_right.pack(side='right')
main_frame.pack()

label_left = tkinter.Label(frame_left, text='THE LEFT FRAME111111111111111', bg='red')
label_left.pack()

label_right = tkinter.Label(frame_right, text='THE RIGHT FRAME', bg='blue')
label_right.pack()

main_screen.mainloop()