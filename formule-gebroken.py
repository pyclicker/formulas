import numpy as np
from math import *
from tabel import raster as tabel
class formules():
    def __init__(self, start=0, stop=1, steps=1, formula=input('f(x) = ')):
        self.start = float(start)
        self.stop = float(stop)
        self.steps = float(steps)
        self.stop += self.steps
        self.formula = formula
        self.dict = {}
        for a in list(np.arange(step=self.steps, start=self.start, stop=self.stop)):
            formula2 = self.formula[::1]
            exec(f'try:\n   self.y = {formula2.replace("x", str(a))}\nexcept:\n   self.y = inf')
            self.dict[float(a)] = float(self.y)
    def get(self):
        return self.dict
if __name__ == '__main__':
    coords = formules(start=input('start = '), stop=input('stop = '), steps=input('steps = ')).get()
    first = list(coords.keys())
    first.insert(0, 'y ')
    second = list(coords.values())
    second.insert(0, 'x ')
    tb = tabel(first, '|')
    tb.append(second)
    tb.build()
