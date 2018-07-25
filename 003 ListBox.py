# coding: utf-8

import tkinter

main_screen = tkinter.Tk()
main_screen.title('列表部件')
main_screen.geometry('300x300')

varStr1 = tkinter.StringVar()  # 标签使用的变量
varStr2 =tkinter.StringVar()   # 初始插入列表中的变量
varStr2.set(('A','B','C','D'))

list_items = [1,2,3,4]  # 使用for插入的列表

label = tkinter.Label(main_screen, textvariable=varStr1, bg='yellow', height=1, width=15)  # 标签
label.pack()

def print_list():
    value = listbox.get(listbox.curselection())    # 得到光标选中值
    varStr1.set(value)


listbox = tkinter.Listbox(main_screen, listvariable=varStr2)

listbox.insert(0, 'zero')  # 在第0位插入zero
listbox.insert(5, 'will be deleted')
listbox.delete(5)  # 删除第5位插入

listbox.pack()

for item in list_items:
    # 使用insert将列表插入
    listbox.insert('end', item)

button = tkinter.Button(main_screen, text='print_list', width=15, height=1, command=print_list)
button.pack()


main_screen.mainloop()

