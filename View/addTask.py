import tkinter as tk  # python 3
from tkinter import ttk
from View import view
from tkcalendar import DateEntry

NORM_FONT = ("Verdana", 10)
MODES = [
    "Backlog",
    "Todo",
    "Testing"
]
GROUP = [
    "Me",
    "Someone"
]


class AddTask:

    def __init__(self, t):
        self.mTk = t
        self.mTk.resizable(0,0)
        self.mVarInProgress = tk.StringVar(self.mTk)
        self.mScaleSeverity = tk.Scale(self.mTk, from_=1.0, to=10.0, tickinterval=1, orient="horizontal")
        self.mVarAssignees = tk.StringVar(self.mTk)
        self.mVarMode = tk.StringVar(self.mTk)
        self.mTextDescription = tk.Text(self.mTk, height=10, width=20)
        self.mVarTitle = tk.StringVar(self.mTk)
        self.mVarTitle.set("")
        mEntryTitle = ttk.Entry(self.mTk, font=NORM_FONT, textvariable=self.mVarTitle)
        self.mTk.wm_title("Adding Task...")
        label_title = ttk.Label(self.mTk, text="Title", font=NORM_FONT)
        label_title.pack(side="top", fill="x", pady=5, padx=5)
        mEntryTitle.pack(side="top", fill="x", padx=10)
        label_description = ttk.Label(self.mTk, text="Description", font=NORM_FONT)
        label_description.pack(side="top", fill="x", pady=5, padx=5)
        self.mTextDescription.pack(side="top", fill="x", padx=10)
        label_mode = ttk.Label(self.mTk, text="Mode", font=NORM_FONT)
        label_mode.pack(side="top", fill="x", pady=5, padx=5)
        self.mVarMode.set(MODES[0])  # initialize
        for text in MODES:
            b = tk.Radiobutton(self.mTk, text=text, indicatoron=0, width=25, val=text, variable=self.mVarMode)
            b.pack(anchor=tk.W, fill="x", pady=2, padx=10)
        frame_label_date = ttk.Frame(self.mTk)
        label_initial_date = ttk.Label(frame_label_date, text="Initial Date", font=NORM_FONT)
        label_initial_date.pack(side="left", fill="x", pady=5, padx=5)
        label_due_date = ttk.Label(frame_label_date, text="Due Date", font=NORM_FONT)
        label_due_date.pack(side="right", fill="x", pady=5, padx=5)
        frame_label_date.pack(side="top", fill="x")
        frame_date = ttk.Frame(self.mTk)
        self.mDEInitial = DateEntry(frame_date, width=12, background='blue', foreground='white', borderwidth=2)
        self.mDEInitial.pack(side="left", expand=True, fill='both', pady=5, padx=5)
        self.mDEEstimated = DateEntry(frame_date, width=12, background='blue', foreground='white', borderwidth=2)
        self.mDEEstimated.pack(side="right", expand=True, fill='both', pady=5, padx=5)
        frame_date.pack(side="top", fill="x")
        # opt = tk.OptionMenu(frame, v2, *GROUP)
        # opt
        # # opt.config(font=('Helvetica', 12))
        # opt.pack(fill="x", padx=5)
        label_severity = ttk.Label(self.mTk, text="Severity", font=NORM_FONT)
        label_severity.pack(side="top", fill="x", pady=(5, 0), padx=5)
        # v4 = tk.StringVar(frame)
        # v4.set(1)
        # entry3 = ttk.Entry(frame, variable=v4, font=NORM_FONT)
        # entry3.pack(side="top", fill="x", padx=5)
        self.mScaleSeverity.pack(side="top", fill="x", padx=10)
        self.mVarInProgress.set("Yes")  # initialize
        label_assignees = ttk.Label(self.mTk, text="Assignees", font=NORM_FONT)
        label_assignees.pack(side="top", fill="x", pady=5, padx=5)
        self.mVarAssignees.set(GROUP[0])
        cb_assignees = ttk.Combobox(self.mTk, values=GROUP, state="readonly", textvariable=self.mVarAssignees)
        # cb_assignees.set(GROUP[0])
        cb_assignees.pack(fill="x", padx=5)
        label_in_progress = ttk.Label(self.mTk, text="In Progress", font=NORM_FONT)
        label_in_progress.pack(side="top", fill="x", pady=5, padx=5)
        # TODO only if TESTING or TODO not Backlog
        frame_in_progress = ttk.Frame(self.mTk)
        rb_yes = tk.Radiobutton(frame_in_progress, text="Yes", indicatoron=0, width=30, val="Yes",
                                variable=self.mVarInProgress)
        rb_yes.pack(side="left", fill="x", pady=(2, 8), padx=(10, 5))
        rb_no = tk.Radiobutton(frame_in_progress, text="No", indicatoron=0, width=30, val="No",
                               variable=self.mVarInProgress)
        rb_no.pack(side="right", fill="x", pady=(2, 8), padx=(5, 10))
        frame_in_progress.pack(side="top", fill="x")
        separator = ttk.Separator(self.mTk, orient="horizontal")
        separator.pack(side="top", fill="x", padx=5)
        self.mFrameCommand = ttk.Frame(self.mTk)
        self.mBtnSubmit = ttk.Button(self.mFrameCommand, text="Submit")
        self.mBtnSubmit.pack(side="left", expand=True, fill='both', padx=5, pady=5)
        button_cancel = ttk.Button(self.mFrameCommand, text="Cancel", command=self.mTk.destroy)
        button_cancel.pack(side="right", expand=True, fill='both', padx=5, pady=5)
        self.mFrameCommand.pack(side="top", fill="x")
        view.center(self.mTk)
