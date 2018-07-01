import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from operator import add


class Human:
    point = [[0, 0]]
    dpoint = [[0, 0]]

    name = ""

    def __init__(self, name):
        self.name = name


Jos = Human("Josefin")

matplotlib.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()

for t in range(0, 1000):
    print(t)
    if np.random.rand() > 0.8:
        Jos.dpoint.append([(np.random.rand()-0.5), (np.random.rand()-0.5)])
    else:
        Jos.dpoint.append(Jos.dpoint[-1])
    Jos.point.append([sum(x) for x in zip(Jos.point[-1], Jos.dpoint[-1])])

    #ax.cla()
    #ax.plot(Jos.point[-1][0], Jos.point[-1][1], 'ob')
    ax.plot([Jos.point[-1][0], Jos.point[-2][0]], [Jos.point[-1][1], Jos.point[-2][1]],'black')
    ax.set_title('Using hyphen instead of Unicode minus')
    plt.xlim(-20,20)
    plt.ylim(-20, 20)
    plt.pause(0.01)
