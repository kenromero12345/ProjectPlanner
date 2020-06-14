class Task:
    def __init__(self, title, desc, mode, assignees, severity, in_progress, init_date, due_date):
        self.mTitle = title
        self.mDesc = desc
        self.mMode = mode
        self.mAssignees = assignees
        self.mSeverity = severity
        self.mInProgress = in_progress
        self.mInitialDate = init_date
        self.mDueDate = due_date
