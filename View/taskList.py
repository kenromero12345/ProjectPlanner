import tkinter as tk  # python 3
from tkinter import ttk
from View import addTask

cols = ("Title", "Mode", "Severity", "In Progress")


class TaskList:
    def __init__(self, frame):
        self.mBtnAddTask = tk.Button(frame, text="Add Task")
        self.mBtnAddTask.pack(side="top", expand=True, fill='both', padx=5, pady=5)
        self.mTvTaskList = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            self.mTvTaskList.heading(col, text=col)
        self.mTvTaskList.column("In Progress", minwidth=80, width=80, stretch=False)
        self.mTvTaskList.column("Severity", minwidth=60, width=60, stretch=False)
        self.mTvTaskList.column("Mode", minwidth=60, width=60, stretch=False)
        self.mTvTaskList.column("Title", minwidth=300, width=500, stretch=False)
        self.mTvTaskList.pack(side="top", expand=True, fill='both', padx=5, pady=5)


