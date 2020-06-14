class Task:
    def __init__(self, title, desc, mode, assignees, severity, in_progress):
        self.title = title
        self.desc = desc
        self.mode = mode
        self.assignees = assignees
        self.severity = severity
        self.in_progress = in_progress
