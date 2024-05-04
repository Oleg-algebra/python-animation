import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

phi  = np.linspace(0,2*np.pi,100)
def draw(i):
    r = 1/(1+i)
    x = r* np.cos(phi)
    y = r * np.sin(phi)
    plt.plot(x,y,c='red')

def animate(i):
    # ax.clear()
    print("frame = {}".format(i))
    plt.xlim(-1/(1+i),1/(1+i))
    plt.ylim(-1/(1+i),1/(1+i))
    # draw(i)

if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots()
    for i in range(150):
        draw(i)
    # run the animation
    ani = FuncAnimation(fig, animate, frames=100, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\zooming_animation\zoom_animation.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")