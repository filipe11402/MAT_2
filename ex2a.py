from sympy import *

init_printing(use_unicode=False)

x = Symbol("x")

function_ex2 = ((4*x**2) + (3*x) + 5 )/ ((x**3) + (2*x**2) + 5*x)

pprint(Integral(function_ex2, (x, 1, 2)))

result_ex2 = Integral(function_ex2, (x, 1, 2))


#printing integral
print(result_ex2.doit())
