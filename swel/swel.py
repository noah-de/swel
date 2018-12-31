import numpy as np

class Swel:
    def __init__(self,E,f):
        self.Emid = self.calc_midpoint(E)
        self.fmid = self.calc_midpoint(f)
        self.df = np.diff(f)

    def calc_swh(self):
        product = self.df * self.Emid
        return 4 * np.sqrt(product.sum(axis=1))

    def calc_midpoint(self,series):
        nofirst = series[:, 1:]  # every element in a row, not the first
        nolast = series[:, :-1]  # every element in a row, not the last
        mid = 0.5 * (nolast + nofirst)
        return mid

    def flip(self,series):
        return series[::-1]
