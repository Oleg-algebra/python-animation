
from sympy import diff,simplify

def derivative(vectField,vars,expr):
    if len(vars) != len(vectField):
        raise AssertionError("length mismatch")
    res = 0
    for i in range(len(vars)):
        res += vectField[i] * diff(expr,vars[i])
    return res

def lie_bracket(vecField1, vecField2, vars):
    new_vect_field = []
    for i in range(len(vecField1)):
        component = derivative(vecField1, vars, vecField2[i]) - derivative(vecField2, vars, vecField1[i])
        new_vect_field.append(simplify(component))

    return new_vect_field