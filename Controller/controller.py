import tkinter as tk  # python 3

from Model import model
from View import view
from Model import task
from View import addTask
from View.editTask import EditTask
from View.popup import Popup


class Controller:
    def __init__(self):
        self.mRoot = tk.Tk()
        self.mModel = model.Model()
        self.mView = view.View(self.mRoot)
        self.mView.mTaskList.mBtnAddTask.config(command=self.add_task)
        self.mView.mTaskList.mTvTaskList.bind("<Double-1>", self.on_task_double_click)

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
            self.mView.mTaskList.mTvTaskList.insert("", "end", values=(t.mTitle, t.mMode, t.mSeverity, t.mInProgress,
                                                                       t.mInitialDate, t.mDueDate))

    def submit_task(self):
        # empty title constraint
        if self.mAddTask.mVarTitle.get().strip() == "":
            temp_root = tk.Tk()
            Popup(temp_root, "No empty titles allowed!")
        else:
            # unique constraint
            unique_flag = True
            for t in self.mModel.mTaskList:
                if t.mTitle == self.mAddTask.mVarTitle.get():
                    temp_root = tk.Tk()
                    Popup(temp_root, "No duplicate titles allowed!")
                    unique_flag = False
            if unique_flag:
                #add task
                t = task.Task(self.mAddTask.mVarTitle.get(), self.mAddTask.mTextDescription.get("1.0", "end"),
                              self.mAddTask.mVarMode.get(), self.mAddTask.mVarAssignees.get(),
                              self.mAddTask.mScaleSeverity.get(), self.mAddTask.mVarInProgress.get(),
                              self.mAddTask.mDEInitial.get(), self.mAddTask.mDEEstimated.get())
                self.mModel.mTaskList.append(t)
                self.task_list_update()
                self.mAddTask.mTk.destroy()

    def edit_task(self):
        #unique constraint
        flag = True
        flag2 = True
        for t in self.mModel.mTaskList:
            if t.mTitle == self.mEditTask.mVarTitle.get():
                if not flag:
                    temp_root = tk.Tk()
                    Popup(temp_root, "No duplicate titles allowed!")
                    flag2 = False
                    break
                flag = False
        if flag2:
            #remove old task
            for t in self.mModel.mTaskList:
                if t.mTitle == self.mEditTask.mOldTitle:
                    self.mModel.mTaskList.remove(t)
                    break
            #add task
            t = task.Task(self.mEditTask.mVarTitle.get(), self.mEditTask.mTextDescription.get("1.0", "end"),
                          self.mEditTask.mVarMode.get(), self.mEditTask.mVarAssignees.get(),
                          self.mEditTask.mScaleSeverity.get(), self.mEditTask.mVarInProgress.get(),
                          self.mEditTask.mDEInitial.get(), self.mEditTask.mDEEstimated.get())
            self.mModel.mTaskList.append(t)
            self.task_list_update()
            self.mEditTask.mTk.destroy()

    def on_task_double_click(self, instance):
        if len(self.mView.mTaskList.mTvTaskList.selection()) > 0:
            temp_root = tk.Tk()
            item = self.mView.mTaskList.mTvTaskList.selection()[0]
            #get task
            for t in self.mModel.mTaskList:
                if t.mTitle == self.mView.mTaskList.mTvTaskList.item(item, "values")[0]:
                    task = t
                    break
            #TODO if there is an error, catch it
            self.mEditTask = EditTask(temp_root, task)
            self.mEditTask.mBtnSubmit.config(command=self.edit_task)
