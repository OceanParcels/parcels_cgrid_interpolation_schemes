import numpy as np
import matplotlib.pyplot as plt


class Particle(object):
    """Simplest Particle object.
    :param x: particle x coordinate
    :param y: particle x coordinate
    :param t: particle time
    """

    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

        self.logsize = 100
        self.xlog = np.zeros(self.logsize)
        self.ylog = np.zeros(self.logsize)
        self.tlog = np.zeros(self.logsize)
        self.ilog = 0

    def store(self):
        if self.ilog == self.logsize:
            self.logsize *= 2
            self.xlog.resize(self.logsize)
            self.ylog.resize(self.logsize)
            self.tlog.resize(self.logsize)
        self.xlog[self.ilog] = self.x
        self.ylog[self.ilog] = self.y
        self.tlog[self.ilog] = self.t
        self.ilog += 1

    def plot(self, fig):
        plt.plot(self.xlog[:self.ilog], self.ylog[:self.ilog], 'C0')
        # Adding an arrow
        if self.xlog[0] < 0:
            ind = np.abs(self.ylog[:self.ilog]) < np.abs(self.xlog[:self.ilog])
            i = ind.argmin()-1 if ind.any() else 0
            if self.ylog[i] > .97:
                i = 0
        else:
            ind = np.abs(self.ylog[:self.ilog]) > np.abs(self.xlog[:self.ilog])
            i = ind.argmin()-1 if ind.any() else 0
            if self.ylog[i] > .97:
                i = 0
        if i > 0:
            x = self.xlog[i]
            xp = self.xlog[i+1]
            y = self.ylog[i]
            yp = self.ylog[i+1]
            dx = xp-x
            dy = yp-y
            plt.arrow(x, y, dx/100., dy/100.,
                      zorder=6, head_width=.025, head_length=.04, color='C0')
        return fig
