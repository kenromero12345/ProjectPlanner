from View.addTask import AddTask
from tkinter import ttk
import tkinter as tk


class UpdateTask(AddTask):
    def __init__(self, t, task):
        AddTask.__init__(self, t)
        self.mVarTitle.set(task.mTitle)
        self.mVarInProgress.set(task.mInProgress)
        self.mScaleSeverity.set(task.mSeverity)
        self.mVarAssignees.set(task.mAssignees)
        self.mVarMode.set(task.mMode)
        self.mDEInitial.set_date(task.mInitialDate)
        self.mDEDue.set_date(task.mDueDate)
        self.mIsBug = task.mIsBug
        self.mIsBonus = task.mIsBonus
        if self.mIsBug:
            self.bugClicked()  # duplicate needed because it changes the variable
            self.bugClicked()
        if self.mIsBonus:
            self.bonusClicked()  # duplicate needed
            self.bonusClicked()
        self.mTextDescription.insert(1.0, task.mDesc)
        self.mBtnSubmit.config(text="Update")
        self.mBtnDelete = tk.Button(self.mFrameCommand, text="Delete", bg='red', fg='white')
        self.mBtnSubmit.config(bg="orange")
        self.mBtnDelete.pack(side="right", expand=True, fill='both', padx=5, pady=5)
        if task.mIsDone:
            self.mCloseOpenBtn = tk.Button(self.mFrameCommand, text="Open", bg="orange", fg="white")
        else:
            self.mCloseOpenBtn = tk.Button(self.mFrameCommand, text="Close", bg="green", fg="white")
        self.mCloseOpenBtn.pack(side="right", expand=True, fill='both', padx=5, pady=5)
        self.mOldTitle = task.mTitle
        self.mTk.wm_title("Updating Task...")
