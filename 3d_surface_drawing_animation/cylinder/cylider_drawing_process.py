import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import cm
N = 20
u = np.linspace(0, 2 * np.pi, N)
v = np.linspace(0, np.pi, N)
x = 10 * np.outer(np.cos(u), np.ones(np.size(u)))
y = 10 * np.outer(np.sin(u), np.ones(np.size(u)))
z = 10 * np.outer(np.ones(np.size(u)), np.linspace(-1, 1, N))

def animate(i):
    print("frame = {}".format(i))
    global u,v,x,y,z
    # Make data

    # print(z[:10,:10])



    # Set an equal aspect ratio
    ax.grid(False)
    plt.axis('off')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-10,10)
    # ax.set_xlabel("X-axis")
    # ax.set_ylabel("Y-axis")
    # ax.set_zlabel("Z-axis")
    # Plot the surface
    ax.plot_surface(x[i:i+2], y[i:i+2], z[i:i+2],linewidth=0, antialiased=False,alpha = 0.5,cmap=cm.coolwarm)

if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')

    # run the animation
    ani = FuncAnimation(fig, animate, frames=N, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\3d_plots\cylinder\surface_drawing_process_by_rows.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")