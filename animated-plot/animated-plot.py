from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegFileWriter
from matplotlib.artist import Artist

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\sokol\\AppData\\Local\\Programs\\Python\\ffmpeg-7.0-essentials_build\\bin\\ffmpeg.exe'

def func(x,t):
    return np.sin(x)*np.sin(t)+np.sin(2*x)*np.sin(2*t)

t = np.linspace(0,10,101)
x = np.linspace(0,2*np.pi,100)
y = func(x,t[0])

fig,ax = plt.subplots()

def update_frame(frame):
    ax.clear()
    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([-2, 2])
    y = func(x,round(t[frame],2))
    ax.set_title("f(x,t) = sin(x)sin(t), t = {}".format(round(t[frame],2)))
    animated_plot = ax.plot(x,y)
    return animated_plot,

animation = FuncAnimation(fig = fig,
                          func=update_frame,
                          frames=len(t),
                          interval=50)

animation.save("animated-wave.mp4", writer='ffmpeg')
plt.show()

