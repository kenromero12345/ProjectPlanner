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

        bottom_frame= tk.Frame(frame)

        self.mTvTaskList = ttk.Treeview(bottom_frame, columns=cols, show='headings')
        for col in cols:
            self.mTvTaskList.heading(col, text=col, anchor="center")

        for col in cols:
            self.mTvTaskList.column(col, minwidth=66, width=66, stretch=False, anchor="center")

        self.mTvTaskList.column("Title", minwidth=300, width=500, stretch=False, anchor="w")

        scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=self.mTvTaskList.yview)

        self.mTvTaskList.configure(xscrollcommand=scrollbar.set)

        self.mTvTaskList.pack(side="left", expand=True, fill='both', padx=(5, 0), pady=5)

        scrollbar.pack(side="right", expand=True, fill='both', padx=(0, 5), pady=5)

        bottom_frame.pack(side="top", expand=True, fill='both')

