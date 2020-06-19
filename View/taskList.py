import tkinter as tk
from tkinter import ttk

cols = ("Title", "Mode", "Severity", "In Progress", "Initial Date", "Due Date", "Bug", "Bonus", "Done")


class TaskList:
    def __init__(self, frame):
        top_frame = tk.Frame(frame)

        self.mBtnAddTask = tk.Button(top_frame, text="Add Task")
        self.mBtnAddTask.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        self.mBtnUpdateMember = tk.Button(top_frame, text="Update Member")
        self.mBtnUpdateMember.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        self.mBtnFilter = tk.Button(top_frame, text="Filter")
        self.mBtnFilter.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        self.mBtnResetFilter = tk.Button(top_frame, text="Reset Filter")
        self.mBtnResetFilter.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        self.mLblFilter = tk.Label(top_frame, text="Filter: OFF")
        self.mLblFilter.pack(side="left", expand=True, fill='both', padx=5, pady=5)

        top_frame.pack(side="top", expand=True, fill='both')

        self.mTvTaskList = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            self.mTvTaskList.heading(col, text=col)

        for col in cols:
            self.mTvTaskList.column(col, minwidth=70, width=70, stretch=False)

        self.mTvTaskList.column("Title", minwidth=300, width=500, stretch=False)

        self.mTvTaskList.pack(side="top", expand=True, fill='both', padx=5, pady=5)
