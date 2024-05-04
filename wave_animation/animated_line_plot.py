# animated_line_plot.py

from random import randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def diagram(f,x,N):
    plt.title("Diagram x_0 = {}".format(x))
    x_points=[x]
    y_points=[f(x)]
    ax.scatter(x_points,y_points)
    for i in range(N):
        x_points.append(y_points[-1])
        y_points.append(y_points[-1])
        x_points.append(x_points[-1])
        y_points.append(f(x_points[-1]))
    ax.scatter(x_points[-1],y_points[-1],c="red")
    ax.annotate(str(y_points[0]),(x_points[0],y_points[0]))
    ax.annotate(str(y_points[-1]),(x_points[-1],y_points[-1]))
    ax.grid()
    ax.plot(x_points,y_points, label='diagram')
    xx=np.linspace(-1,1,1000)
    ax.plot(xx,f(xx),label='ff(x)')
    ax.plot(xx,xx)
    ax.legend()

# function that draws each frame of the animation
def animate(i):

    ax.clear()

    ff = lambda x: -3 / 2 * x + 1 / 2 * x ** 3
    x = 0.01
    diagram(ff,x,i)


# create the figure and axes objects
fig, ax = plt.subplots()

# run the animation
ani = FuncAnimation(fig, animate, frames=100,repeat=False)
# r"E:\Oleg\Универ\Магістр\1 курс 2 семестр\Динамічні системи\Самостійні роботи\animation1.gif"
f = r"E:\Oleg\Универ\Магістр\1 курс 2 семестр\Динамічні системи\Самостійні роботи\animation2.gif"
writerGif = PillowWriter(fps = 5)
ani.save(f,writer = writerGif)