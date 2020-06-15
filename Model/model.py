import numpy as np


class Model:

    def __init__(self):
        self.mTaskList = []

    def sortByTitle(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mTitle)

    def sortByMode(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mMode)

    def sortByInProgress(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mInProgress)

    def sortByInitialDate(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mInitialDate)

    def sortByDueDate(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mDueDate)

    def sortBySeverity(self, reverse):
        self.mTaskList.sort(reverse=reverse, key=lambda t: t.mSeverity)

