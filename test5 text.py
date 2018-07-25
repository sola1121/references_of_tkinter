import tkinter

root = tkinter.Tk()
root.title("text 控件测试")
root.geometry("400x300+800+400")

var_str1 = tkinter.StringVar()
var_str2 = tkinter.StringVar()

def insert_into():
    text2.insert(tkinter.END, var_str2.get())

btn = tkinter.Button(root, text="insert", command=insert_into)
btn.pack(side="right")

text1 = tkinter.Text(root, width=10, height=5)
text1.pack(side="top")
text2 = tkinter.Text(root, width=10, height=2)
text2.place(x=10, y=100)




root.mainloop()
