from tkinter.filedialog import asksaveasfilename, askopenfilename
import pickle
from pathlib import Path
import os

files = [('All Files', '*.*'),
         ('Python Files', '*.py'),
         ('Text Document', '*.txt')]


class Model:

    def __init__(self):
        self.mTaskList = []
        self.mSavedPath = None

    def sort_by_title(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mTitle)

    def sort_by_mode(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mMode)

    def sort_by_in_progress(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mInProgress)

    def sort_by_initial_date(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mInitialDate)

    def sort_by_due_date(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mDueDate)

    def sort_by_severity(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mSeverity)

    def load_task_list(self):
        file = askopenfilename(filetypes=files, defaultextension=files)
        if not file:  # askopenfilename return `None` if dialog closed with "cancel".
            return
        self.load(file)

    def load(self, file):
        self.mTaskList = pickle.load(open(file, "rb"))

    def load_path(self, file):
        self.mSavedPath = pickle.load(open(file, "rb"))

    def save_as_task_list(self):
        file = asksaveasfilename(filetypes=files, defaultextension=files)
        if not file:  # asksaveasfilename return `None` if dialog closed with "cancel".
            return
        self.save(file)
        self.mSavedPath = file
        self.save_path(str(Path(os.getcwd()).parent) + "\\auto_save_path.txt")

    def save_task_list(self):
        self.save(self.mSavedPath)

    def save(self, file):
        pickle.dump(self.mTaskList, open(file, "wb"))

    def save_path(self, file):
        pickle.dump(self.mSavedPath, open(file, "wb"))
