# coding: utf-8

import  tkinter

main_screen = tkinter.Tk()
main_screen.title('帆布')
main_screen.geometry('300x200')

canvas = tkinter.Canvas(main_screen, bg='blue', width=300, height=150, )
image_file = tkinter.PhotoImage(file='images/anchor.gif')
image = canvas.create_image(150, 75, anchor='center', image=image_file)

# 坐标
x0, x1, y0, y1 =  70, 120, 30, 40
# 线
line = canvas.create_line(x0-70, y0-30, x1, y1)
# 画一个圆
oval = canvas.create_oval(50, 50, 80, 80, fill='red')
# 长宽为30的矩形
rect = canvas.create_rectangle(250, 10, 280, 40)
# 画一个扇形, start开始的角度 extent结束的角度
arc = canvas.create_arc(10, 10, 60, 60, start=30, extent=270)
canvas.pack()

def move_rect():
    canvas.move(rect, 0, 2)   # 使用帆布的move函数移动canvas对象


button = tkinter.Button(main_screen, text='move', width=8, height=1, command=move_rect)
button.pack()

main_screen.mainloop()


