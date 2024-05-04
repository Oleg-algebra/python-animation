from typing import Iterable

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegFileWriter
from matplotlib.artist import Artist
from scipy.signal import square
plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\sokol\\AppData\\Local\\Programs\\Python\\ffmpeg-7.0-essentials_build\\bin\\ffmpeg.exe'

A = 1
T = 1
N = 10
Tp=0.5
omega = 2*np.pi/T

def fourier_series(t, n,a_n):
    res = np.ones(len(t))*a_n[0]
    for i in range(1,n+1):
        # print('res = ',res[:10])
        res = res + a_n[i]*np.cos(i*omega*t)
    return res

def square_wave(t):
    res = square(t*2*np.pi+np.pi/2,duty=Tp)+1
    res = res / 2
    res = res*A
    return res

a_n = [A*Tp/T]
for i in range(1,N+1):
    if i %2 == 0:
        a_n.append(0)
    else:
        a_n.append(2*A/(i*np.pi)*np.sin(i*np.pi/2))
print(a_n)
T1 = 2
t = np.linspace(-T1,T1,201)
fig,ax = plt.subplots()

animated_plot, = ax.plot(t,square_wave(t))
ax.plot(t,fourier_series(t,N,a_n))
plt.show()
def update_frame(frame):
    ax.clear()
    ax.set_xlim([min(t), max(t)])
    ax.set_ylim([-0.5, 1.5])
    ax.plot(t,square_wave(t))
    y = fourier_series(t, frame,a_n)
    ax.set_title("Fourier series n = {}".format(frame))
    animated_plot = ax.plot(t,y)
    return animated_plot,

animation = FuncAnimation(fig = fig,
                          func=update_frame,
                          frames=N,
                          interval=100)

animation.save("animated-plot.mp4", writer='ffmpeg')
