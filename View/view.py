import tkinter as tk  # python 3
from tkinter import ttk
from View import taskList


class View:
    def __init__(self, root):
        frame = tk.Frame(root)
        # self.model = model
        self.mTaskList = taskList.TaskList(frame)
        frame.pack()
        center(root)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
