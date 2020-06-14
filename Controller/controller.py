import tkinter as tk  # python 3

from Model import model
from View import view
from Model import task
from View import addTask

class Controller:
    def __init__(self):
        self.mRoot = tk.Tk()
        self.mModel = model.Model()
        self.mView = view.View(self.mRoot)
        self.mView.mTaskList.mBtnAddTask.config(command=self.add_task)


    def run(self):
        self.mRoot.title("Project Planner")
        self.mRoot.deiconify()
        self.mRoot.mainloop()

    def add_task(self):
        temp_root = tk.Tk()
        self.mAddTask = addTask.AddTask(temp_root)
        self.mAddTask.mBtnSubmit.config(command=self.submit_task)

    def task_list_update(self):
        self.mView.mTaskList.mTvTaskList.delete(*self.mView.mTaskList.mTvTaskList.get_children())
        for t in self.mModel.mTaskList:
            self.mView.mTaskList.mTvTaskList.insert("", "end", values=(t.mTitle, t.mMode, t.mSeverity, t.mInProgress))
        # self.task_list.insert("", "end"
        #                           , values=(self.entry_title.get(), self.var_mode.get()
        #                                     , self.scale_severity.get(), self.var_in_progress.get()))

    def submit_task(self):
        t = task.Task(self.mAddTask.mEntryTitle.get(), self.mAddTask.mTextDescription.get("1.0", "end")
                      , self.mAddTask.mVarMode.get(), self.mAddTask.mVarAssignees.get()
                      , self.mAddTask.mScaleSeverity.get(), self.mAddTask.mVarInProgress.get())
        self.mModel.mTaskList.append(t)
        self.task_list_update()
        # self.view.list_box.insert("", "end"
        #                           , values=(self.entry_title.get(), self.var_mode.get()
        #                                     , self.scale_severity.get(), self.var_in_progress.get()))
        self.mAddTask.mTk.destroy()
