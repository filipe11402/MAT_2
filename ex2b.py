from sympy import *

init_printing(use_unicode=False)

x = Symbol("x")

function_ex2 = (x / sqrt(1 + 3*x))

pprint(Integral(function_ex2, (x, 5, 8)))

result_ex2 = Integral(function_ex2, (x, 5, 8))


#printing integral
print(result_ex2.doit())
