import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify, Symbol,sin,cos,exp,sinh,cosh, sympify
from lie_brackets import lie_bracket
from matplotlib.animation import FuncAnimation

plt.rcParams['animation.ffmpeg_path'] = 'C:\\Users\\sokol\\AppData\\Local\\Programs\\Python\\ffmpeg-7.0-essentials_build\\bin\\ffmpeg.exe'
class ConstantFunction:
    def __init__(self,constant):
        self.constant = constant

    def __call__(self,*args):
        if len(args) == 0:
            raise AssertionError("need at least one argument")
        return self.constant(*args)*np.ones(args[0].shape)

class VectorField:
    def __init__(self,components,variables):
        self.components = components
        self.lambdas = self.lambdify_vector_fields(components,variables)
        self.variables = variables


    def lambdify_vector_fields(self,VF, vars):
        lambdaVF = []
        for comp in VF:
            if comp.is_constant(*vars):
                new_comp = lambdify(vars, comp, modules='numpy')
                lambdaVF.append(ConstantFunction(new_comp))
            else:
                lambdaVF.append(lambdify(vars, comp, modules='numpy'))

        return lambdaVF

class Animation:
    def __init__(self,VF1, VF2, variables,bounds = (-5,5),step = 0.1):
        self.VF1 = VF1
        self.VF2 = VF2
        self.variables = variables
        self.bounds = bounds
        self.step = step
        self.rows = 2
        self.cols = 2
        self.fig, self.ax = plt.subplots(nrows=self.rows, ncols=self.cols, figsize=(10, 10))
        self.VFs = []
        self.VFs_data = []
        self.configure_axes()
        self.file = open("Iterations_result.txt","w")
        self.title_template = "({})dx + ({})dy"

    def configure_axes(self):
        # Set bottom and left spines as x and y axes of coordinate system
        for i in range(self.rows):
            for j in range(self.cols):
                self.ax[i,j].spines['bottom'].set_position('zero')
                self.ax[i,j].spines['left'].set_position('zero')

                # Remove top and right spines
                self.ax[i,j].spines['top'].set_visible(False)
                self.ax[i,j].spines['right'].set_visible(False)
                self.ax[i,j].grid()

    def update_frame(self,frame):
        self.ax[1,1].clear()
        a = self.bounds[0]
        b = self.bounds[1]
        x = np.arange(a, b, self.step)
        y = np.arange(a, b, self.step)

        X, Y = np.meshgrid(x, y)

        # print(next_lie)
        self.ax[1, 1].streamplot(X, Y, *self.VFs_data[3+frame], density=1.4, linewidth=None, color='black')
        # self.ax[1, 1].set_title(f"{self.VFs[3+frame].components[0]}dx+({self.VFs[3+frame].components[1]})dy, iter= {2+frame}")
        self.ax[1, 1].set_title(f"iter= {2 + frame}")


        self.ax[1, 1].spines['bottom'].set_position('zero')
        self.ax[1, 1].spines['left'].set_position('zero')

        # Remove top and right spines
        self.ax[1, 1].spines['top'].set_visible(False)
        self.ax[1, 1].spines['right'].set_visible(False)
        self.ax[1, 1].grid()

        return self.ax,



    def animate(self,frame_numbers):
        lie_field = VectorField(lie_bracket(self.VF1.components,
                                            self.VF2.components, self.variables),
                                self.variables)
        # print(lie_field.components)

        a = self.bounds[0]
        b = self.bounds[1]
        x = np.arange(a, b, self.step)
        y = np.arange(a, b, self.step)

        X, Y = np.meshgrid(x, y)

        self.VFs = [self.VF1,self.VF2,lie_field]
        # Make the direction data for the arrows
        self.VFs_data = [[comp(X, Y) for comp in vf.lambdas] for vf in self.VFs]
        # vf2_data = [comp(X, Y) for comp in vf2.lambdas]

        self.ax[0, 0].streamplot(X, Y, *self.VFs_data[0], density=1.4, linewidth=None, color='red')
        # self.ax[0, 0].set_title(f"({self.VFs[0].components[0]})dx+({self.VFs[0].components[1]})dy")
        self.ax[0, 0].set_title(self.title_template.format(self.VFs[0].components[0], self.VFs[0].components[1]))
        # print(type(ax[0,0]))
        self.ax[0, 1].streamplot(X, Y, *self.VFs_data[1], density=1.4, linewidth=None, color='green')
        self.ax[0, 1].set_title(f"({self.VFs[1].components[0]})dx+({self.VFs[1].components[1]})dy")

        self.ax[1, 0].streamplot(X, Y, *self.VFs_data[2], density=1.4, linewidth=None, color='blue')
        self.ax[1, 0].set_title(f"({lie_field.components[0]})dx+({lie_field.components[1]})dy, iter = 1")

        for i in range(frame_numbers):
            next_lie = VectorField(lie_bracket(self.VFs[0].components, self.VFs[-1].components,
                                           self.variables), self.variables)

            next_lie_data = [comp(X, Y) for comp in next_lie.lambdas]
            self.VFs.append(next_lie)
            self.VFs_data.append(next_lie_data)

        for i in range(len(self.VFs)):
            self.file.write(f"iter= {max(0,i-1)} --- ({self.VFs[i].components[0]})dx+({self.VFs[i].components[1]})dy\n")
        self.file.close()

        # print(next_lie)
        self.ax[1, 1].streamplot(X, Y, *self.VFs_data[2], density=1.4, linewidth=None, color='black')
        self.ax[1, 1].set_title(f"{self.VFs[2].components[0]}dx+({self.VFs[2].components[1]})dy")

        animation = FuncAnimation(fig = self.fig,
                                  func=self.update_frame,
                                  frames=frame_numbers,
                                  interval=1000,
                                  repeat=True)

        animation.save("animated-lie-bracket-2.mp4", writer='ffmpeg')
        print("Animation saved")
        plt.show()


x_sym = Symbol("x")
y_sym = Symbol("y")

variables = [x_sym, y_sym]

vf1_components = list(map(sympify,input("Enter 1-st VF components: ").split()))
vf2_components = list(map(sympify,input("Enter 2-nd VF components: ").split()))
variables = list(map(Symbol, input("Enter variables names: ").split()))

vf1 = VectorField(vf1_components,variables)       #[-y_sym,x_sym]
vf2 = VectorField(vf2_components,variables)   #[x_sym, x_sym+y_sym**2]

animation = Animation(*[vf1,vf2],variables=variables,bounds=[-50,50],step=5)
frame_number = 10
animation.animate(frame_number)



