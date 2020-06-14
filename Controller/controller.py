import tkinter as Tk  # python 3

from Model import model
from View import view


class Controller:
    def __init__(self):
        self.root = Tk.Tk()
        self.model = model.Model()
        self.view = view.View(self.root, self.model)

    def run(self):
        self.root.title("Project Planner")
        self.root.deiconify()
        self.root.mainloop()
