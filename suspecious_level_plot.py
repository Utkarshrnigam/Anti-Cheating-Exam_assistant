
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')



def animate(i):
    try:
        data = pd.read_csv('./final_dataset/bar_graph.csv',header=None)
        x = data.values[0]
        # print(x)
        ypos = [j for j in range(len(x))]


        plt.cla()

        plt.bar(ypos, x)

        plt.legend(loc='upper left')
        plt.tight_layout()
    except:
        pass


ani = FuncAnimation(plt.gcf(), animate, interval=500)

plt.tight_layout()
plt.show()
