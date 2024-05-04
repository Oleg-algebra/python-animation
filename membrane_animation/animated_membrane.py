import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegFileWriter
from matplotlib import cm
from mpl_toolkits import mplot3d

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\sokol\\AppData\\Local\\Programs\\Python\\ffmpeg-7.0-essentials_build\\bin\\ffmpeg.exe'

def draw_membrane(membrane_func, time):
    time_step = 0.1
    t = time * time_step

    x = np.linspace(0, np.pi, 400)
    y = np.linspace(0, np.pi / 2, 400)
    X, Y = np.meshgrid(x, y)

    Z = membrane_func(X,Y,t)

    ax.set_xlim(0,np.pi)
    ax.set_ylim(0,np.pi/2)
    ax.set_zlim(-2,2)
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
    # print("frame {} finished".format(time))
def animate(i):
    ax.clear()
    a = 1
    c = 1
    b = 1
    A = 1
    ff = lambda x,y,t: c/a*np.sin(y)*np.sin(a*t)+ A/18/a**2*np.cos(3*x)*np.sin(3*y)*(1-np.cos(a*np.sqrt(18)*t))+b*np.cos(x)*np.sin(5*y)*np.cos(a*np.sqrt(26)*t)
    draw_membrane(ff, i)


if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # fig = plt.figure()
    # ax = fig.add_subplot(111,projection = '3d')

    # run the animation
    ani = FuncAnimation(fig,
                        animate,
                        frames=30,
                        repeat=True,
                        interval=150)
    f = r"membrane_animation.mp4"
    # writerGif = PillowWriter(fps=20)
    # writerGif = FFMpegFileWriter(fps = 5)
    # writerMovie = MovieWriter(fps=20)
    print("Start")
    ani.save(f, writer='ffmpeg')
    print("Finished")
    plt.show()