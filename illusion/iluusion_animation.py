import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import cm
N = 50
u = np.linspace(0, 2 * np.pi, N)
v = np.linspace(0, np.pi, N)
x = 10 * np.outer(np.cos(u), np.ones(np.size(u)))
y = 10 * np.outer(np.sin(u), np.ones(np.size(u)))
z = 10 * np.outer(np.ones(np.size(u)), np.linspace(-1, 1, N))

x1 = 10 * np.outer(np.cos(u), np.sin(v))
y1 = 10 * np.outer(np.sin(u), np.sin(v))
z1 = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

def animate(i):
    if i%10 == 0:
        print("frame = {}".format(i))
    global u,v,x,y,z,x1,y1,z1
    # Make data
    ax.clear()
    # Set an equal aspect ratio
    ax.grid(False)
    plt.axis('off')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-10,10)
    if i%2 == 0:
    # Plot the surface
        ax.plot_surface(x, y, z,linewidth=0, antialiased=False,alpha = 0.5,cmap=cm.coolwarm)
    else:
        ax.plot_surface(x1, y1, z1, linewidth=0, antialiased=False, alpha=0.5)

if __name__ == "__main__":
    fps = 50
    # create the figure and axes objects
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')

    # run the animation
    ani = FuncAnimation(fig, animate, frames=100, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\illusion\illusion_animation.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")

