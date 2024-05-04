import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegFileWriter


def draw_wave(wave_func, time):
    time_step = 0.1
    t = time * time_step
    x = np.linspace(0, np.pi, 400)
    ax.set_ylim(4/6, 8/6)
    plt.plot(x, wave_func(x, t))
    # print("frame {} finished".format(time))
def animate(i):
    ax.clear()
    a = 1
    # ff = lambda x, t: np.cos(a * np.pi / 2 * t) * np.sin(np.pi / 2 * x) + np.cos(3 * a * np.pi / 2 * t) * np.sin(
    #     3 * np.pi / 2 * x)
    ff = lambda x,t: 1 + 1/6 * np.sin(6*t)*np.cos(3*x)
    draw_wave(ff, i)


if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots()

    # run the animation
    ani = FuncAnimation(fig, animate, frames=25, repeat=False)
    f = r"D:\University\PythonAnimation\wave_animation\wave_animation-2.gif"
    # writerGif = PillowWriter(fps=20)
    # writerGif = FFMpegFileWriter(fps = 5)
    # writerMovie = MovieWriter(fps=20)
    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")