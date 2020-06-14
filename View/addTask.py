import tkinter as tk  # python 3
from tkinter import ttk
from View import view
from Model import task

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

    def __init__(self, view, model):
        self.model = model
        self.view = view

    def add_task(self):
        self.tk = tk.Tk()
        self.var_in_progress = tk.StringVar(self.tk)
        self.scale_severity = tk.Scale(self.tk, from_=1.0, to=10.0, tickinterval=1, orient="horizontal")
        self.var_assignees = tk.StringVar(self.tk)
        self.var_mode = tk.StringVar(self.tk)
        self.text_description = tk.Text(self.tk, height=10, width=20)
        self.entry_title = ttk.Entry(self.tk, font=NORM_FONT)
        self.tk.wm_title("Adding Task...")
        label_title = ttk.Label(self.tk, text="Title", font=NORM_FONT)
        label_title.pack(side="top", fill="x", pady=5, padx=5)
        self.entry_title.pack(side="top", fill="x", padx=10)
        label_description = ttk.Label(self.tk, text="Description", font=NORM_FONT)
        label_description.pack(side="top", fill="x", pady=5, padx=5)
        self.text_description.pack(side="top", fill="x", padx=10)
        label_mode = ttk.Label(self.tk, text="Mode", font=NORM_FONT)
        label_mode.pack(side="top", fill="x", pady=5, padx=5)
        self.var_mode.set(MODES[0])  # initialize
        for text in MODES:
            b = tk.Radiobutton(self.tk, text=text, indicatoron=0, width=25, val=text, variable=self.var_mode)
            b.pack(anchor=tk.W, fill="x", pady=2, padx=10)
        label_assignees = ttk.Label(self.tk, text="Assignees", font=NORM_FONT)
        label_assignees.pack(side="top", fill="x", pady=5, padx=5)
        self.var_assignees.set(GROUP[0])
        cb_assignees = ttk.Combobox(self.tk, values=GROUP, state="readonly")
        cb_assignees.set(GROUP[0])
        cb_assignees.pack(fill="x", padx=5)
        # opt = tk.OptionMenu(frame, v2, *GROUP)
        # opt
        # # opt.config(font=('Helvetica', 12))
        # opt.pack(fill="x", padx=5)
        label_severity = ttk.Label(self.tk, text="Severity", font=NORM_FONT)
        label_severity.pack(side="top", fill="x", pady=(5, 0), padx=5)
        # v4 = tk.StringVar(frame)
        # v4.set(1)
        # entry3 = ttk.Entry(frame, variable=v4, font=NORM_FONT)
        # entry3.pack(side="top", fill="x", padx=5)
        self.scale_severity.pack(side="top", fill="x", padx=10)
        self.var_in_progress.set("Yes")  # initialize
        label_in_progress = ttk.Label(self.tk, text="In Progress", font=NORM_FONT)
        label_in_progress.pack(side="top", fill="x", pady=5, padx=5)
        # TODO only if TESTING or TODO not Backlog
        frame_in_progress = ttk.Frame(self.tk)
        rb_yes = tk.Radiobutton(frame_in_progress, text="Yes", indicatoron=0, width=30, val="Yes",
                                variable=self.var_in_progress)
        rb_yes.pack(side="left", fill="x", pady=(2, 8), padx=10)
        rb_no = tk.Radiobutton(frame_in_progress, text="No", indicatoron=0, width=30, val="No",
                               variable=self.var_in_progress)
        rb_no.pack(side="right", fill="x", pady=(2, 8), padx=10)
        frame_in_progress.pack(side="top", fill="x")
        separator = ttk.Separator(self.tk, orient="horizontal")
        separator.pack(side="top", fill="x", padx=5)
        frame_command = ttk.Frame(self.tk)
        button_submit = ttk.Button(frame_command, text="Submit", command=self.submit_task)
        button_submit.pack(side="left", expand=True, fill='both', padx=5, pady=5)
        button_cancel = ttk.Button(frame_command, text="Cancel", command=self.tk.destroy)
        button_cancel.pack(side="right", expand=True, fill='both', padx=5, pady=5)
        frame_command.pack(side="top", fill="x")
        view.center(self.tk)

    def submit_task(self):
        t = task.Task(self.entry_title.get(), self.text_description.get("1.0", "end"), self.var_mode.get()
                      , self.var_assignees.get(), self.scale_severity.get(), self.var_in_progress.get())
        self.model.task_list.append(t)
        self.view.task_list_update()
        # self.view.list_box.insert("", "end"
        #                           , values=(self.entry_title.get(), self.var_mode.get()
        #                                     , self.scale_severity.get(), self.var_in_progress.get()))
        self.tk.destroy()
