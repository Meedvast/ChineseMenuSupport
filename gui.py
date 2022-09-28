import tkinter as tk
from tkinter import filedialog
import xletLocation


def select_src_path():
    selected_folder = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
    var_event.set(selected_folder)


def select_dest_path():
    selected_folder = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
    var_event1.set(selected_folder)


def start():
    xletLocation.replace_xlet(entry_src.get(), entry_dest.get())


if __name__ == '__main__':
    window = tk.Tk()
    window.title('派拉蒙中文菜单辅助工具')  # 设置窗口的标题
    window_width = 400
    window_height = 150
    window_width_x = (window.winfo_screenwidth() - window_width) / 2
    window_height_y = (window.winfo_screenheight() - window_height) / 2
    window.geometry("%dx%d+%d+%d" % (window_width, window_height, window_width_x, window_height_y))

    # 建立内容文本框
    var_event = tk.StringVar()
    entry_src = tk.Entry(window, textvariable=var_event)
    entry_src.place(x=120, y=10, anchor='nw')

    var_event1 = tk.StringVar()
    entry_dest = tk.Entry(window, textvariable=var_event1)
    entry_dest.place(x=120, y=60, anchor='nw')

    # 建立标签
    label_src = tk.Label(window, text='输入文件夹', width=15)
    label_src.place(x=10, y=10)

    label_src = tk.Label(window, text='输出文件夹', width=15)
    label_src.place(x=10, y=60)

    # 建立点击事件内容
    button_src = tk.Button(window, text='选择输入文件夹', command=lambda: select_src_path())
    button_src.place(x=280, y=5)
    button_src = tk.Button(window, text='选择输出文件夹', command=lambda: select_dest_path())
    button_src.place(x=280, y=55)
    button_start = tk.Button(window, text='生成', command=lambda: start(), width=15)
    button_start.place(x=120, y=100)
    window.mainloop()
