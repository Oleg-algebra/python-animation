import numpy as np
import matplotlib.pyplot as plt
from sympy import lambdify, Symbol, sympify
from lie_brackets import lie_bracket

class ConstantFunction:
    def __init__(self,constant):
        self.constant = constant

    def __call__(self,*args):
        if len(args) == 0:
            raise AssertionError("need at least one argument")
        return self.constant(*args)*np.ones(args[0].shape)

def lambdify_vector_fields(VF, vars):
    lambdaVF = []
    for comp in VF:
        print(comp)
        if comp.is_constant(*vars):
            new_comp = lambdify(variables, comp, modules='numpy')
            lambdaVF.append(ConstantFunction(new_comp))
        else:
            lambdaVF.append(lambdify(variables, comp, modules='numpy'))

    return lambdaVF

x_sym = Symbol('x')
y_sym = Symbol('y')
variables = [x_sym, y_sym]

expr1 = -y_sym
expr2 = x_sym+y_sym*2
expr3 = Symbol('1')

string_expr1 = input("Enter 1-st vector field: ").split()
string_expr2 = input("Enter 2-st vector field: ").split()

print(string_expr1)

expr1 = list(map(sympify, string_expr1))
expr2 = list(map(sympify, string_expr2))

exprs = expr1 + expr2
print(exprs)
for expr in exprs:
    print(expr.is_constant(*variables))

lambdas = lambdify_vector_fields(exprs, variables)

x = np.arange(-1,1,0.1)
y = np.arange(-1,1,0.2)

X, Y = np.meshgrid(x, y)

u = lambdas[0](X,Y)
v = lambdas[1](X,Y)

# print(u)
# print(v)

plt.streamplot(X,Y,u,v,density=1.4, linewidth=None, color='#A23BEC')
plt.grid()
plt.show()