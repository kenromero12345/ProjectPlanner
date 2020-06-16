import tkinter as tk  # python 3
from View import taskList


class View:
    def __init__(self, root):
        # initialize var
        self.mMenuFile = None
        self.mMenuHelp = None

        frame = tk.Frame(root)
        self.menu_bar(root)
        # self.model = model
        self.mTaskList = taskList.TaskList(frame)
        frame.pack()
        center(root)

    def menu_bar(self, root):
        menu = tk.Menu(root)
        self.mMenuFile = tk.Menu(menu, tearoff=0)
        self.mMenuFile.add_command(label="New Project...")
        self.mMenuFile.add_command(label="New Task...")
        self.mMenuFile.add_command(label="Open...")
        self.mMenuFile.add_command(label="Save...")
        self.mMenuFile.add_command(label="Save As...")
        self.mMenuFile.add_separator()
        self.mMenuFile.add_command(label="Exit")
        menu.add_cascade(label="File", menu=self.mMenuFile)
        self.mMenuHelp = tk.Menu(menu, tearoff=0)
        self.mMenuHelp.add_command(label="Help")
        self.mMenuHelp.add_command(label="About")
        menu.add_cascade(label="Help", menu=self.mMenuHelp)
        root.config(menu=menu)


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
