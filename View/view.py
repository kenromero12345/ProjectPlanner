import tkinter as tk  # python 3
from tkinter import ttk
from View import addTask

cols = ("Title", "Mode", "Severity", "In Progress")


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


class View:
    def __init__(self, root, model):
        frame = tk.Frame(root)
        self.model = model
        self.addTask = addTask.AddTask(self, model)
        add_task_btn = tk.Button(frame, text="Add Task", command=self.addTask.add_task)
        add_task_btn.pack(side="top", expand=True, fill='both', padx=5, pady=5)
        self.tv_task_list = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            self.tv_task_list.heading(col, text=col)
        self.tv_task_list.column("In Progress", minwidth=80, width=80, stretch=False)
        self.tv_task_list.column("Severity", minwidth=60, width=60, stretch=False)
        self.tv_task_list.column("Mode", minwidth=80, width=80, stretch=False)
        self.tv_task_list.column("Title", minwidth=300, width=500, stretch=False)
        self.tv_task_list.pack(side="top", expand=True, fill='both', padx=5, pady=5)
        frame.pack()
        center(root)

    def task_list_update(self):
        self.tv_task_list.delete(*self.tv_task_list.get_children())
        for t in self.model.task_list:
            self.tv_task_list.insert("", "end", values=(t.title, t.mode, t.severity, t.in_progress))
        # self.task_list.insert("", "end"
        #                           , values=(self.entry_title.get(), self.var_mode.get()
        #                                     , self.scale_severity.get(), self.var_in_progress.get()))