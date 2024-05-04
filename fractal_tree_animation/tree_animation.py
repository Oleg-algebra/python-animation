import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
initial_size = 100
branches = [{"core" : (0,-initial_size),
            "angle" : np.pi/2,
            "dist" : initial_size}]
def connect_points(tuple1,tuple2,level):

    plt.plot(tuple1,tuple2,c="C"+str(level))
def draw_branches(i):
    global branches
    dist_reduction = 0.8
    rotation_angle = np.pi/9
    if i==0:
        branch = branches[0]
        (x_0,y_0) = branch["core"]
        x_1 = x_0 + branch["dist"] * np.cos(branch["angle"])
        y_1 = y_0 + branch["dist"] * np.sin(branch["angle"])
        connect_points((x_0,x_1),(y_0,y_1),1)
        branch["end"] = (x_1,y_1)

        # branch.pop("core")
        branches = [branch]
    else:
        new_branches = []
        for branch in branches:
            for j in range(2):
                new_left_branch = {"dist": branch["dist"] * dist_reduction, "angle": branch["angle"] + (-1)**j* rotation_angle}
                x_end = branch["end"][0] + new_left_branch["dist"] * np.cos(new_left_branch["angle"])
                y_end = branch["end"][1] + new_left_branch["dist"] * np.sin(new_left_branch["angle"])
                new_left_branch["end"] = (x_end,y_end)
                connect_points((branch["end"][0],x_end),(branch["end"][1],y_end),i+1)
                new_branches.append(new_left_branch)

            # new_right_branch = {"dist": branch["dist"] * dist_reduction, "angle": branch["angle"] + rotation_angle}
            # x_end = branch["end"][0] + new_right_branch["dist"] * np.cos(new_right_branch["angle"])
            # y_end = branch["end"][1] + new_right_branch["dist"] * np.sin(new_right_branch["angle"])
            # new_right_branch["end"] = (x_end, y_end)
            # connect_points((branch["end"][0], x_end), (branch["end"][1], y_end),i+1)
            # new_branches.append(new_right_branch)

        branches = new_branches


def animate(i):
    # ax.clear()
    print("frame = {}".format(i))

    plt.xlim(-4*initial_size-10,4*initial_size+10)
    plt.ylim(-initial_size,4*initial_size)
    draw_branches(i)

if __name__ == "__main__":
    fps = 5
    # create the figure and axes objects
    fig, ax = plt.subplots()

    # run the animation
    ani = FuncAnimation(fig, animate, frames=12, repeat=False)
    f = r"E:\Oleg\Univer\PythonAnimation\fractal_tree_animation\fractal_tree_animation.gif"

    print("start")
    ani.save(f, writer='pillow',fps = fps)
    print("finish")