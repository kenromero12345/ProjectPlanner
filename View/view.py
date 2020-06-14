import tkinter as tk  # python 3
from tkinter import ttk

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


class View:
    def __init__(self, root, model):
        self.frame = tk.Frame(root)
        self.model = model
        addTaskBtn = tk.Button(self.frame, text="Add Task", command=self.addTask)
        addTaskBtn.pack(expand=True, fill='both', padx=5, pady=5)
        self.frame.pack()
        self.center(root)

    def addTask(self):
        frame = tk.Tk()
        frame.wm_title("Adding Task...")
        label = ttk.Label(frame, text="Title", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=5, padx=5)
        entry = ttk.Entry(frame, font=NORM_FONT)
        entry.pack(side="top", fill="x", padx=10)
        label2 = ttk.Label(frame, text="Description", font=NORM_FONT)
        label2.pack(side="top", fill="x", pady=5, padx=5)
        entry2 = tk.Text(frame, height=10, width=20)
        entry2.pack(side="top", fill="x", padx=10)
        label4 = ttk.Label(frame, text="Mode", font=NORM_FONT)
        label4.pack(side="top", fill="x", pady=5, padx=5)
        v = tk.StringVar(frame)
        v.set(MODES[0])  # initialize
        for text in MODES:
            b = tk.Radiobutton(frame, text=text, indicatoron=0, width=25, val=text, variable=v)
            b.pack(anchor=tk.W, fill="x", pady=2, padx=10)
        label3 = ttk.Label(frame, text="Assignees", font=NORM_FONT)
        label3.pack(side="top", fill="x", pady=5, padx=5)
        v2 = tk.StringVar(frame)
        v2.set(GROUP[0])
        cb = ttk.Combobox(frame, values=GROUP, state="readonly")
        cb.set(GROUP[0])
        cb.pack(fill="x", padx=5)
        # opt = tk.OptionMenu(frame, v2, *GROUP)
        # opt
        # # opt.config(font=('Helvetica', 12))
        # opt.pack(fill="x", padx=5)
        label5 = ttk.Label(frame, text="Severity", font=NORM_FONT)
        label5.pack(side="top", fill="x", pady=(5, 0), padx=5)
        # v4 = tk.StringVar(frame)
        # v4.set(1)
        # entry3 = ttk.Entry(frame, variable=v4, font=NORM_FONT)
        # entry3.pack(side="top", fill="x", padx=5)
        s = tk.Scale(frame, from_=1.0, to=10.0, tickinterval=1, orient="horizontal")
        s.pack(side="top", fill="x", padx=10)
        v3 = tk.StringVar(frame)
        v3.set("Yes")  # initialize
        label4 = ttk.Label(frame, text="In Progress", font=NORM_FONT)
        label4.pack(side="top", fill="x", pady=5, padx=5)
        #TODO only if TESTING or TODO not Backlog
        frame2 = ttk.Frame(frame)
        b3 = tk.Radiobutton(frame2, text="Yes", indicatoron=0, width=30, val="Yes", variable=v3)
        b3.pack(side="left", fill="x", pady=(2, 8), padx=10)
        b4 = tk.Radiobutton(frame2, text="No", indicatoron=0, width=30, val="No", variable=v3)
        b4.pack(side="right", fill="x", pady=(2, 8), padx=10)
        frame2.pack(side="top", fill="x")
        s = ttk.Separator(frame, orient="horizontal")
        s.pack(side="top", fill="x", padx=5)
        frame3 = ttk.Frame(frame)
        b1 = ttk.Button(frame3, text="Submit", command=frame.destroy)
        b1.pack(side="left", expand=True, fill='both', padx=5, pady=5)
        b2 = ttk.Button(frame3, text="Cancel", command=frame.destroy)
        b2.pack(side="right", expand=True, fill='both', padx=5, pady=5)
        frame3.pack(side="top", fill="x")
        self.center(frame)

    def center(self, win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))