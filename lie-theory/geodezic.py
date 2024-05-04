import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sympy import Symbol, diff, simplify,Matrix,lambdify
from matplotlib import colormaps
from scipy.linalg import expm


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

def matrix_vector(A,vector):
    if A.shape[0] != len(vector):
        print(A.shape , vector.shape)
        raise ArithmeticError("Matrix and vector have different dimensions")

    res_vector = []
    for i in range(len(A)):
        component = 0
        for j in range(len(vector)):
            component += A[i][j] * vector[j]
        res_vector.append(component)

    return res_vector

def get_sphere(radius,N):
    u = np.linspace(0, 2 * np.pi, N)
    v = np.linspace(0, np.pi, N)

    U, V = np.meshgrid(u, v)
    x_sphere = radius*np.cos(U) * np.sin(V)
    y_sphere = radius*np.sin(U) * np.sin(V)
    z_sphere = radius*np.cos(V)
    return x_sphere, y_sphere, z_sphere


a = 1
b = -1
c = 0

d = 1
e = 1
f = 1

A = np.array([[0,a],[-a,0]])
B = np.array([[0,a,b],
              [-a,0,c],
              [-b,-c,0]])
vars = [Symbol('x'), Symbol('y')]
vars_3d = [Symbol('x'), Symbol('y'),Symbol('z')]

VF_3d = VectorField(matrix_vector(B,vars_3d),vars_3d)

VF = VectorField(matrix_vector(A,vars),vars)

b = 5


# print(colormaps)
ax = plt.figure().add_subplot(projection='3d')
x_sphere, y_sphere, z_sphere = get_sphere(b,50)
surf = ax.plot_surface(x_sphere,y_sphere,z_sphere,cmap='Blues',linewidth=0, antialiased=False,zorder = 0)


N = 12
x = np.linspace(-b,b,N)
y = np.linspace(-b,b,N)
z = np.linspace(-b,b,N)

x_sphere, y_sphere, z_sphere = get_sphere(b,N)
X, Y ,Z= np.meshgrid(x,y,z)

U = VF_3d.lambdas[0](x_sphere,y_sphere,z_sphere)
V = VF_3d.lambdas[1](x_sphere,y_sphere,z_sphere)
W = VF_3d.lambdas[2](x_sphere,y_sphere,z_sphere)


# plt.figure(figsize=(10, 10))
# plt.streamplot(X,Y,U,V, density=1.0, linewidth=None, color='#A23BEC')

ax.quiver(x_sphere,y_sphere,z_sphere,U,V,W, length=1, normalize=True,color='red',zorder = 1)

step = 0.01
t = np.arange(0,2*np.pi,step)

init_point = np.array([b,0,0])
curve = []
for i in range(len(t)):
    exp_B = expm(B*t[i])
    curve.append(matrix_vector(exp_B, init_point))
    # exp_B = np.matmul(exp_B, exp_B)
x = []
y = []
z = []
for i in range(len(curve)):
    x.append(curve[i][0])
    y.append(curve[i][1])
    z.append(curve[i][2])
ax.scatter(init_point[0],init_point[1],init_point[2], marker="o", c="green", s=150,zorder = 10)
ax.plot(x,y,z,color="yellow",linewidth=1,zorder = 10)
# Show plot with grid
# ax.grid(False)
# plt.axis('off')
# plt.grid(False)
plt.show()






