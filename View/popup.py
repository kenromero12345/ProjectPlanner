from tkinter import ttk
from View import view


class Popup:
    def __init__(self, t, msg):
        t.wm_title("Popup")
        label = ttk.Label(t, text=msg)
        label.pack(side="top", fill="x", pady=10)
        ttk.Button(t, text="Okay", command=t.destroy)
        view.center(t)