from View.addTask import AddTask
from tkinter import ttk


class UpdateTask(AddTask):
    def __init__(self, t, task):
        AddTask.__init__(self, t)
        self.mVarTitle.set(task.mTitle)
        self.mVarInProgress.set(task.mInProgress)
        self.mScaleSeverity.set(task.mSeverity)
        self.mVarAssignees.set(task.mAssignees)
        self.mVarMode.set(task.mMode)
        self.mDEInitial.set_date(task.mInitialDate)
        self.mDEEstimated.set_date(task.mDueDate)
        self.mTextDescription.insert(1.0, task.mDesc)
        self.mBtnSubmit.config(text="Update")
        self.mBtnDelete = ttk.Button(self.mFrameCommand, text="Delete")
        self.mBtnDelete.pack(side="left", expand=True, fill='both', padx=5, pady=5)
        self.mOldTitle = task.mTitle
        self.mTk.wm_title("Updating Task...")
