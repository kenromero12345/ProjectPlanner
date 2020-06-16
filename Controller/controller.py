import _pickle
import os
import tkinter as tk
from os import path
from pathlib import Path
from tkinter import messagebox
from Model import model
from Model import task
from View import addTask
from View import view
from View.updateTask import UpdateTask

AUTO_SAVE_PATH_TXT = "\\auto_save_path.txt"
AUTO_SAVE_PROJECT_TXT = "\\auto_save_project.txt"


class Controller:
    def __init__(self):
        # initialize variables
        self.mAddTask = None
        self.mUpdateTask = None
        self.mTLColumnClicked = None
        self.mIsReverse = False
        self.mPath = Path(os.getcwd())
        self.mRoot = tk.Tk()
        self.mModel = model.Model()
        self.mView = view.View(self.mRoot)

        # menu bar command
        self.mView.mMenuFile.entryconfigure(0, command=self.new_project)
        self.mView.mMenuFile.entryconfigure(2, command=self.load_project)
        self.mView.mMenuFile.entryconfigure(3, command=self.save_project)
        self.mView.mMenuFile.entryconfigure(4, command=self.save_as_project)
        self.mView.mMenuFile.entryconfigure(1, command=self.add_task)
        self.mView.mMenuFile.entryconfigure(6, command=self.quit_and_save)
        self.mView.mMenuHelp.entryconfigure(0, command=self.tutorial)
        self.mView.mMenuHelp.entryconfigure(1, command=about)

        # Task list
        self.mView.mTaskList.mBtnAddTask.config(command=self.add_task)
        self.mView.mTaskList.mTvTaskList.bind("<Double-1>", self.on_task_double_click)
        self.mView.mTaskList.mTvTaskList.bind("<Button-1>", self.on_task_click)

        self.mRoot.protocol('WM_DELETE_WINDOW', self.quit_and_save)  # override close button

    def run(self):
        self.mRoot.title("Project Planner")
        self.mRoot.deiconify()
        if path.exists(str(self.mPath.parent) + AUTO_SAVE_PROJECT_TXT):
            try:
                self.mModel.load(str(self.mPath.parent) + AUTO_SAVE_PROJECT_TXT)
                self.task_list_update()
            except _pickle.UnpicklingError:
                messagebox.showerror("Error", "There was an error on the auto_save_project.txt file loaded!")
        if path.exists(str(self.mPath.parent) + AUTO_SAVE_PATH_TXT):
            try:
                self.mModel.load_path(str(self.mPath.parent) + AUTO_SAVE_PATH_TXT)
            except _pickle.UnpicklingError:
                messagebox.showerror("Error", "There was an error on the auto_save_path.txt file loaded!")
        self.mRoot.mainloop()

    def quit_and_save(self):
        # TODO could be better, maybe ask to save when exiting
        self.mModel.save(str(self.mPath.parent) + AUTO_SAVE_PROJECT_TXT)
        if messagebox.askyesno("Exit", "If you exit the application, any changes you have made will be lost. "
                                       "Are you sure you wish to leave?"):
            self.mRoot.destroy()

    def tutorial(self):
        print("tutorial")
        # TODO popup

    def new_project(self):
        if messagebox.askyesno("Save before Exit", "Do you want to save the current project first?"):
            self.mModel.save_as_task_list()
        else:
            self.mModel.mTaskList = []
            self.task_list_update()
            self.mModel.mSavedPath = None

    def load_project(self):
        if messagebox.askyesno("Save before Exit", "Do you want to save the current project first?"):
            self.mModel.save_as_task_list()
        else:
            try:
                self.mModel.load_task_list()
                self.task_list_update()
            except _pickle.UnpicklingError:
                messagebox.showerror("Error", "There was an error on the file loaded!")

    def save_project(self):
        if hasattr(self.mModel, 'mSavedPath') and self.mModel.mSavedPath is None:
            self.mModel.save_task_list()
        else:
            self.mModel.save_as_task_list()

    def save_as_project(self):
        self.mModel.save_as_task_list()

    def add_task(self):
        temp_root = tk.Tk()
        self.mAddTask = addTask.AddTask(temp_root)
        self.mAddTask.mBtnSubmit.config(command=self.submit_task)

    def task_list_update(self):
        # delete all tasks in view
        self.mView.mTaskList.mTvTaskList.delete(*self.mView.mTaskList.mTvTaskList.get_children())

        # add all task in view
        for t in self.mModel.mTaskList:
            self.mView.mTaskList.mTvTaskList.insert("", "end", values=(t.mTitle, t.mMode, t.mSeverity, t.mInProgress,
                                                                       t.mInitialDate, t.mDueDate))

    def submit_task(self):
        if self.mAddTask.mVarTitle.get().strip() == "":  # empty title constraint
            messagebox.showwarning(title="Warning", message="No empty titles allowed!")
        elif self.isDuplicateTitle(True):  # unique constraint
            messagebox.showwarning(title="Warning", message="No duplicate titles allowed!")
        else:
            # add task
            t = task.Task(self.mAddTask.mVarTitle.get(), self.mAddTask.mTextDescription.get("1.0", "end"),
                          self.mAddTask.mVarMode.get(), self.mAddTask.mVarAssignees.get(),
                          self.mAddTask.mScaleSeverity.get(), self.mAddTask.mVarInProgress.get(),
                          self.mAddTask.mDEInitial.get(), self.mAddTask.mDEEstimated.get())
            self.mModel.mTaskList.append(t)

            self.task_list_update()  # update task list view
            self.mAddTask.mTk.destroy()  # close add task window

    def isDuplicateTitle(self, is_add):
        if is_add:  # for add task
            title = self.mAddTask.mVarTitle.get()
        else:  # for update task
            title = self.mUpdateTask.mVarTitle.get()
        for t in self.mModel.mTaskList:
            if t.mTitle == title:
                return True
        return False

    def edit_task_view(self):
        if self.mAddTask.mVarTitle.get().strip() == "":  # empty title constraint
            messagebox.showwarning(title="Warning", message="No empty titles allowed!")
        elif self.isDuplicateTitle(False) and self.mUpdateTask.mVarTitle.get() \
                != self.mUpdateTask.mOldTitle:  # unique constraint for edit
            messagebox.showwarning(title="Warning", message="No duplicate titles allowed!")
        else:
            self.delete_task()  # delete old task

            # add task
            t = task.Task(self.mUpdateTask.mVarTitle.get(), self.mUpdateTask.mTextDescription.get("1.0", "end"),
                          self.mUpdateTask.mVarMode.get(), self.mUpdateTask.mVarAssignees.get(),
                          self.mUpdateTask.mScaleSeverity.get(), self.mUpdateTask.mVarInProgress.get(),
                          self.mUpdateTask.mDEInitial.get(), self.mUpdateTask.mDEEstimated.get())
            self.mModel.mTaskList.append(t)

            self.task_list_update()  # update task list view
            self.mUpdateTask.mTk.destroy()  # close edit task window

    def delete_task_view(self):
        self.delete_task()
        self.task_list_update()  # update task list view
        self.mUpdateTask.mTk.destroy()  # close edit task window

    def delete_task(self):
        # remove old task
        for t in self.mModel.mTaskList:
            if t.mTitle == self.mUpdateTask.mOldTitle:
                self.mModel.mTaskList.remove(t)
                break

    def on_task_click(self, instance):
        region = self.mView.mTaskList.mTvTaskList.identify("region", instance.x, instance.y)
        if region == "heading":
            if self.mView.mTaskList.mTvTaskList.identify_column(instance.x) == "#1":
                if hasattr(self, 'mTLColumnClicked') and self.mTLColumnClicked == "#1" and self.mIsReverse:
                    self.mModel.sort_by_title(False)
                    self.mIsReverse = False
                else:
                    self.mModel.sort_by_title(True)
                    self.mIsReverse = True
            elif self.mView.mTaskList.mTvTaskList.identify_column(instance.x) == "#2":
                if hasattr(self, 'mTLColumnClicked') and self.mTLColumnClicked == "#2" and self.mIsReverse:
                    self.mModel.sort_by_mode(False)
                    self.mIsReverse = False
                else:
                    self.mModel.sort_by_mode(True)
                    self.mIsReverse = True
            elif self.mView.mTaskList.mTvTaskList.identify_column(instance.x) == "#3":
                if hasattr(self, 'mTLColumnClicked') and self.mTLColumnClicked == "#3" and self.mIsReverse:
                    self.mModel.sort_by_severity(False)
                    self.mIsReverse = False
                else:
                    self.mModel.sort_by_severity(True)
                    self.mIsReverse = True
            elif self.mView.mTaskList.mTvTaskList.identify_column(instance.x) == "#4":
                if hasattr(self, 'mTLColumnClicked') and self.mTLColumnClicked == "#4" and self.mIsReverse:
                    self.mModel.sort_by_in_progress(False)
                    self.mIsReverse = False
                else:
                    self.mModel.sort_by_in_progress(True)
                    self.mIsReverse = True
            elif self.mView.mTaskList.mTvTaskList.identify_column(instance.x) == "#5":
                if hasattr(self, 'mTLColumnClicked') and self.mTLColumnClicked == "#5" and self.mIsReverse:
                    self.mModel.sort_by_initial_date(False)
                    self.mIsReverse = False
                else:
                    self.mModel.sort_by_initial_date(True)
                    self.mIsReverse = True
            elif self.mView.mTaskList.mTvTaskList.identify_column(instance.x) == "#6":
                if hasattr(self, 'mTLColumnClicked') and self.mTLColumnClicked == "#6" and self.mIsReverse:
                    self.mModel.sort_by_due_date(False)
                    self.mIsReverse = False
                else:
                    self.mModel.sort_by_due_date(True)
                    self.mIsReverse = True
            self.task_list_update()
            self.mTLColumnClicked = self.mView.mTaskList.mTvTaskList.identify_column(instance.x)

    def on_task_double_click(self, instance):
        if len(self.mView.mTaskList.mTvTaskList.selection()) > 0:
            temp_root = tk.Tk()
            item = self.mView.mTaskList.mTvTaskList.selection()[0]
            # get task
            tsk = None
            for t in self.mModel.mTaskList:
                if t.mTitle == self.mView.mTaskList.mTvTaskList.item(item, "values")[0]:
                    tsk = t
                    break
            self.mUpdateTask = UpdateTask(temp_root, tsk)
            self.mUpdateTask.mBtnSubmit.config(command=self.edit_task_view)
            self.mUpdateTask.mBtnDelete.config(command=self.delete_task_view)


def about():
    messagebox.showinfo(title="About", message="A python application for project planning for programmers to use to be "
                                               "efficient in their tasks with their team or their own.\n\nCreated by "
                                               "Ken Gil Romero, a master student of University of Washington")
