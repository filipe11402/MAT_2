from sympy import *

init_printing(use_unicode=False)

x, t, y, z = symbols("x t y z")

function_ex1 = 3*x**2

print("A FUNCAO: ")

pprint(Integral(function_ex1, (x, 2, x)))

result_ex1 = Integral(function_ex1, (x, 2, x)).doit()


#printing result
print("PRIMITIVA EX1 : {}".format(result_ex1))
