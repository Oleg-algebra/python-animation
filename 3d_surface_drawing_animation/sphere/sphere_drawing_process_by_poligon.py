import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import cm

# Make data
N = 15
u = np.linspace(0, 2 * np.pi, N)
v = np.linspace(0, np.pi, N)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

j=0
k=0
def animate(i):
    if i%10 == 0:
        print("frame = {}".format(i))
    global u,v,x,y,z
    global j,k

    ax.set_aspect('equal')
    ax.grid(False)
    plt.axis('off')
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)
    ax.set_zlim(-10,10)
    # ax.set_xlabel("X-axis")
    # ax.set_ylabel("Y-axis")
    # ax.set_zlabel("Z-axis")
    # Plot the surface
    if k == N:
        k=0
        j+=1
    ax.plot_surface(x[j:j+2,k:k+2], y[j:j+2,k:k+2], z[j:j+2,k:k+2],linewidth=0, antialiased=False,alpha = 0.5,cmap=cm.coolwarm)
    k+=1

if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    # run the animation
    ani = FuncAnimation(fig, animate, frames=1, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\3d_plots\sphere\surface_drawing_process_by_poligon1.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")