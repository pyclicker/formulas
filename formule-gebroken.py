import numpy as np
from math import *
for a in ['matplotlib.pyplot as plt']:
    exec(f'import {a}')
class formules():
    def __init__(self,start=0,stop=1,steps=1):
        self.start = float(start)
        self.stop = float(stop)
        self.steps = float(steps)
        self.stop+=self.steps
        formule = input('f(x) = ')
        self.dict = {}
        for a in list(np.arange(step=self.steps,start=self.start,stop=self.stop)):
            formule2 = formule[::1]
            exec(f'self.y = {formule2.replace("x",str(a))}')
            self.dict[float(a)] = float(self.y)
    def get(self):
        return self.dict
    
if __name__ == '__main__':
    coords = formules(input('start = '),input('stop = '),steps=input('steps = ')).get()
    if input('Do you want a plot on your screen? Y/N  ') == 'y':
        print('you typed Y')
        plt.plot(np.array(**coords.keys),np.array(**coords.values).reshape("inf",None))
        plt.show()
    print(coords)


