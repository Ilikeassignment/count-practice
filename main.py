# !/usr/bin/env python3
# -*- coding: utf-8 -*- #

# @DateTime : 2024/06/23 10:39:56
# @Author   : 涂梓宸
# @Contact  : turtle2024@yeah.net
# @File     : main.py
# @Version  : v1.9.15.20240621_alpha

import tkinter
import _tkinter
from tkinter import messagebox, colorchooser
import random
import tkinter.messagebox
import tkinter.simpledialog
import json


def root_window(): # 根窗口/主窗口
    global root

    # 窗口设置

    root = tkinter.Tk()
    root.title("计算练习")
    
    # 设置窗口图标
    
    try:
        root.iconbitmap('logo.ico')
    except _tkinter.TclError:
        tkinter.messagebox.showerror("错误", "_tkinter.TclError：缺失”logo.dll“")   
        root.quit()     # 退出程序
        root.destroy() 
        exit(0)

    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    width = 240
    height = 150
    left = (screenwidth - width) / 2
    top = (screenheight - height) / 2

    root.geometry("%dx%d+%d+%d" % (width, height, left, top))
    root.resizable(0, 0)

    # 读取设置文件

    while True:
        try:
            with (open("settings.json", "r") as read_color_setting_file):
                color_setting = json.load(read_color_setting_file)
                read_window_color = color_setting["window_color"]
            root.config(bg=f"{read_window_color}")
            break
        except FileNotFoundError:
            break
    
    # 添加按钮控件

    tkinter.Button(root, text="初级(只有加减法)", command=low).place(x=0, y=0)
    tkinter.Button(root, text="中级(加减乘除法)", command=medium).place(x=0, y=60)
    tkinter.Button(root, text="高级(乘除法较多)", command=tall).place(x=0, y=120) 
    tkinter.Button(root, text="退出", command=exit_ctp).place(x=205, y=0)
    tkinter.Button(root, text="设置", command=settings).place(x=205, y=60)
    tkinter.Button(root, text="关于", command=concerning).place(x=205, y=120)


def low(): # 初级
    root.withdraw() # 隐藏根窗口

    # 输入“最大数值”和“题目数量”

    max_value = tkinter.simpledialog.askinteger(title="计算练习(初级)", prompt="最大数值：", initialvalue=100)
    if None == max_value:
        root.deiconify()
        return

    max_topic = tkinter.simpledialog.askinteger(title="计算练习(初级)", prompt="题目数量：", initialvalue=10)
    if None == max_topic:
        root.deiconify()
        return

    correct = 0
    error = 0
    topic = 0
    correct_digit = 0
    symbol = 0

    while topic != max_topic:
        symbol_digit = random.randint(1, 2)

        digit1 = random.randint(0, max_value)
        digit2 = random.randint(0, max_value)

        if symbol_digit == 2:
            if digit2 > digit1:
                digit2 = random.randint(0, digit1)

        if symbol_digit == 1:
            symbol = '+'

        elif symbol_digit == 2:
            symbol = '-'

        if symbol_digit == 1:
            correct_digit = digit1 + digit2

        elif symbol_digit == 2:
            correct_digit = digit1 - digit2

        input_digit = tkinter.simpledialog.askfloat(title="计算练习(初级)", prompt=f"题目：{digit1}{symbol}{digit2}=", initialvalue=0.0)
        if None == input_digit:
            root.destroy()
            return

        if input_digit and input_digit == correct_digit:
            messagebox.showinfo(title="计算练习(初级)", message="正确")
            correct = correct + 1

        if input_digit != correct_digit:
            messagebox.showinfo("计算练习(初级)", "错误")
            error = error + 1

        topic = topic + 1

    messagebox.showinfo("计算练习(初级)", "结束,正确：" + str(correct) + "错误：" + str(error))

    root.deiconify()


def medium(): #中级
    root.withdraw() # 隐藏根窗口

    # 输入“最大数值”和“题目数量”

    messagebox.showinfo("计算练习(中级)", "注意‘%’表示除法，‘*’表示乘法！")
    max_value = tkinter.simpledialog.askinteger(title="计算练习(初级)", prompt="最大数值：", initialvalue=100)
    if None == max_value:
        root.destroy()
        return

    max_topic = tkinter.simpledialog.askinteger(title="计算练习(初级)", prompt="题目数量：", initialvalue=10)
    if None == max_topic:
        root.destroy()
        return

    correct = 0
    error = 0
    topic = 0
    correct_digit = 0
    symbol = 0

    while topic != max_topic:
        symbol_digit = random.randint(1, 4)

        digit1 = random.randint(0, max_value)
        digit2 = random.randint(0, max_value)

        if symbol_digit == 4:
            if digit2 == 0:
                digit2 = random.randint(1, max_value)

        if symbol_digit == 2:
            if digit2 > digit1:
                digit2 = random.randint(0, digit1)

        if symbol_digit == 1:
            symbol = '+'

        elif symbol_digit == 2:
            symbol = '-'

        elif symbol_digit == 3:
            symbol = 'x'

        elif symbol_digit == 4:
            symbol = '%'

        if symbol_digit == 1:
            correct_digit = digit1 + digit2

        elif symbol_digit == 2:
            correct_digit = digit1 - digit2

        elif symbol_digit == 3:
            correct_digit = digit1 * digit2

        elif symbol_digit == 4:
            correct_digit = digit1 / digit2
            length = len(str(correct_digit))

            if length >= 10:
                correct_digit = '%.2f' % correct_digit
                messagebox.showinfo("计算练习(中级)", "下一题保留2位小数")
                correct_digit = float(correct_digit)

        input_digit = tkinter.simpledialog.askfloat(title="计算练习(中级)", prompt=f"题目：{digit1}{symbol}{digit2}=", initialvalue=0.0)
        
        if None == input_digit:
            root.destroy()
            return

        if input_digit == correct_digit:
            messagebox.showinfo("计算练习(中级)", "正确")
            correct = correct + 1

        if input_digit != correct_digit:
            messagebox.showinfo("计算练习(中级)", "错误")
            error = error + 1

        topic = topic + 1

    messagebox.showinfo("计算练习(中级)", "结束,正确：" + str(correct) + "错误：" + str(error))

    root.deiconify()


def tall(): #高级
    root.withdraw() # 隐藏根窗口

    # 输入“最大数值”和“题目数量”

    messagebox.showinfo("计算练习(高级)", "注意‘/’表示除法，‘*’表示乘法！")
    max_value = tkinter.simpledialog.askinteger(title="计算练习(初级)", prompt="最大数值：", initialvalue=100)
    if None == max_value:
        root.destroy()
        return

    max_topic = tkinter.simpledialog.askinteger(title="计算练习(初级)", prompt="题目数量：", initialvalue=10)
    if None == max_topic:
        root.destroy()
        return

    correct = 0
    error = 0
    topic = 0
    correct_digit = 0
    symbol = 0

    while topic != max_topic:
        symbol_digit = random.randint(1, 8)

        digit1 = random.randint(0, max_value)
        digit2 = random.randint(0, max_value)

        if symbol_digit == 3 and 4 and 5:
            if digit2 == 0:
                digit2 = random.randint(1, max_value)

        if symbol_digit == 2:
            if digit2 > digit1:
                digit2 = random.randint(0, digit1)

        if symbol_digit == 1:
            symbol = '+'

        elif symbol_digit == 2:
            symbol = '-'

        elif symbol_digit == 3 or 4 or 5:
            symbol = 'x'

        elif symbol_digit == 6 or 7 or 8:
            symbol = '%'

        if symbol_digit == 1:
            correct_digit = digit1 + digit2

        elif symbol_digit == 2:
            correct_digit = digit1 - digit2

        elif symbol_digit == 3:
            correct_digit = digit1 * digit2

        elif symbol_digit == 4:
            correct_digit = digit1 * digit2

        elif symbol_digit == 5:
            correct_digit = digit1 * digit2

        elif symbol_digit == 6 or 7 or 8:
            correct_digit = digit1 / digit2
            length = len(str(correct_digit))

            if length >= 10:
                correct_digit = '%.2f' % correct_digit
                messagebox.showinfo("计算练习(高级)", "下一题保留2位小数")
                correct_digit = float(correct_digit)

        input_digit = tkinter.simpledialog.askfloat(title="计算练习(高级)", prompt=f"题目：{digit1}{symbol}{digit2}=", initialvalue=0.0)
        
        if None == input_digit:
            root.destroy()
            return

        if input_digit and input_digit == correct_digit:
            messagebox.showinfo("计算练习(高级)", "正确")
            correct = correct + 1

        if input_digit != correct_digit:
            messagebox.showinfo("计算练习(高级)", "错误")
            error = error + 1

        topic = topic + 1

    messagebox.showinfo("计算练习(高级)", "结束,正确：" + str(correct) + "错误：" + str(error))

    root.deiconify()


def exit_ctp():
    root.withdraw()

    true_or_false_exit = messagebox.askyesno("计算练习", "确认要退出吗？")
    if not true_or_false_exit:
        root.deiconify()
        return
    else:
        root.quit()
        root.destroy()
        exit(0)


def settings():
    root.withdraw()

    window_color = tkinter.colorchooser.askcolor(title="设置窗口颜色")
    window_color = window_color[1]
    if None == window_color:
        root.deiconify()
        return

    root.config(bg=f"{window_color}")
    # print(window_color) 输出十六进制颜色代码，测试使用

    write_window_color = {"name": "settings", "window_color": f"{window_color}"}

    with open('settings.json', 'w') as write_color_setting_file:
        json.dump(write_window_color, write_color_setting_file)

    tkinter.messagebox.showinfo("计算练习", "设置成功")

    root.deiconify()

def concerning():
    root.withdraw()

    messagebox.showinfo("关于计算练习", "作者：涂梓宸\n版本：v1.9.15.20240623_alpha\n特别鸣谢：无")

    root.deiconify()

# mian

if __name__ == '__main__':
    root_window()
    root.mainloop()
