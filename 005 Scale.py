# coding: utf-8

import tkinter

main_screen = tkinter.Tk()
main_screen.title('尺度')
main_screen.geometry('400x200')

label = tkinter.Label(main_screen, bg='yellow', width=20, height=1)
label.pack()

def scale_value(v):
    label.config(text='You moved to ' + v)


scale = tkinter.Scale\
    (main_screen, label='try move', from_=10, to=50, orien=tkinter.HORIZONTAL,
     length=200, showvalue=True, tickinterval=10, resolution=0.1, command=scale_value)

# label 标签名字
# showvalue   True False   是否在尺度条上显示选择的value
# tickinterval 记号间距
# resolution 精度值
# orient 尺度的方向
# length 定义像素长度px

scale.pack()

main_screen.mainloop()