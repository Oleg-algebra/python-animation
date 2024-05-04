import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify,sympify,expand, Symbol,diff
from lie_brackets import lie_bracket
x_sym = Symbol("x")
y_sym = Symbol("y")
z_sym = Symbol("z")
variables = [x_sym, y_sym, z_sym]
expr = 1 + x_sym
vf1 = [x_sym, Symbol("1"), x_sym * (y_sym + 1)]
vf2 = [Symbol("1"), Symbol("0"), y_sym]



lie_field = lie_bracket(vf1, vf2, variables)
component = lambdify(variables,lie_field[2],modules="numpy")
step = 0.25
a = 1
x = np.arange(-a,a,step)
y = np.arange(-a,a,step)
z = np.arange(-a,a,step)

X,Y,Z = np.meshgrid(x,y,z)

vf1_lambda = [lambdify(variables,expr,modules='numpy') for expr in vf1]
vf2_lambda = [lambdify(variables,expr,modules='numpy') for expr in vf2]
lie_lambda = [lambdify(variables,expr,modules='numpy') for expr in lie_field]
print(vf1)
print(vf1[1].is_constant([x_sym,y_sym]))
ax = plt.figure(dpi=200).add_subplot(projection='3d')

# Make the direction data for the arrows
u = lie_lambda[0](X,Y,Z)
v = lie_lambda[1](X,Y,Z)
w = lie_lambda[2](X,Y,Z)


elev = 20
azim = -15
roll = None
ax.view_init(elev, azim, roll)
ax.quiver(X,Y,Z, u, v, w, length=0.25,normalize=True)
plt.show()

