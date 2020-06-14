from View.addTask import AddTask


class EditTask(AddTask):
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
        self.mOldTitle = task.mTitle
        self.mTk.wm_title("Editing Task...")
