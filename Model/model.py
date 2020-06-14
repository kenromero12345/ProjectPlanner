import numpy as np


class Model:

    def __init__(self):
        self.xPoint = 200
        self.yPoint = 200
        self.res = None

    def calculate(self):
        x, y = np.meshgrid(np.linspace(-5, 5, self.xPoint), np.linspace(-5, 5, self.yPoint))
        z = np.cos(x ** 2 * y ** 3)
        self.res = {"x": x, "y": y, "z": z}