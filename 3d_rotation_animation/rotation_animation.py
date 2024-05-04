from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

elev = azim = roll = 0
N = 20
u = np.linspace(0, 2 * np.pi, N)
v = np.linspace(0, np.pi, N)
X = 10 * np.outer(np.cos(u), np.ones(np.size(u)))
Y = 10 * np.outer(np.sin(u), np.ones(np.size(u)))
Z = 10 * np.outer(np.ones(np.size(u)), np.linspace(-1, 1, N))
def draw():
    global X,Y,Z
    # X, Y, Z = axes3d.get_test_data(0.05)
    ax.plot_wireframe(X, Y, Z)

    # Set the axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

#  for angle in range(0, 360*4 + 1):
# Rotate the axes and update
def animate(angle):
    global elev, azim, roll
    if angle % 100 == 0:
        print("frame = {}".format(angle))

    ax.clear()
    draw()
    ax.grid(False)
    plt.axis('off')

    # Normalize the angle to the range [-180, 180] for display
    angle_norm = (angle + 180) % 360 - 180

    # Cycle through a full rotation of elevation, then azimuth, roll, and all

    if angle <= 180:
        elev +=1
    elif 180 < angle <= 180*2 :
        azim += 1
    elif 180*2 < angle <= 180*3:
        roll += 1
    else:
        elev += 1
        azim += 1
        roll += 1

    # Update the axis view and title
    ax.view_init(elev, azim, roll)
    plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))


if __name__ == "__main__":
    frame_number = 180*4 + 1
    fps = 40
    # create the figure and axes objects
    # fig, ax = plt.subplots()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # run the animation
    ani = FuncAnimation(fig, animate, frames=frame_number, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\3d_rotation_animation\rotation_animation.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")

