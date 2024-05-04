import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

phi  = np.linspace(0,2*np.pi,100)
x = []
y = []
def draw(i):
    global  x,y
    a = 2
    b = 0.1
    angle_step = 2*np.pi/100
    r = a * np.exp(angle_step*i*b)
    x.append(r * np.cos(angle_step*i))
    y.append(r * np.sin(angle_step*i))
    plt.plot(x,y,c='red')

def animate(i):
    # ax.clear()
    print("frame = {}".format(i))
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    draw(i)

if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots()

    # run the animation
    ani = FuncAnimation(fig, animate, frames=100, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\spiral_animation\spiral.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")