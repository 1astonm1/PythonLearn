# -*- coding:utf-8 -*-
import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title("my window")      # 标题名
window.geometry("200x200")  # 设置窗口大小 注意：这里是字母x不是*号

# label标签
lab = tk.Label(window, text='Hello World!', bg='green',font=('Arial', 12), width=15, height=2)
# 设置标签 文字，背景颜色，字体，长宽
lab.pack()
# 固定窗口位置

# button 按钮
b = tk.Button(window, text='hit me', width=15, height=2, command='hit_me')
# command 是点击按钮后执行的命令(调用函数)
b.pack()  # 固定位置


# 按钮命令
var = tk.StringVar()  # TK中用来显示变化的变量
on_hit = False  # 默认初始状态为 False

def hit_me():
    global on_hit
    if on_hit == False:     # 从 False 状态变成 True 状态
        on_hit = True
        var.set('you hit me')   # 设置标签的文字为 'you hit me'
    else:       # 从 True 状态变成 False 状态
        on_hit = False
        var.set('') # 设置 文字为空

# 点击显示的标签

lab2 = tk.Label(window, textvariable=var, width=12, height=2, bg='blue', font=('Arial', 12) )
lab2.pack()


window.mainloop()  # 相当于主函数， 只执行一次，放在最后