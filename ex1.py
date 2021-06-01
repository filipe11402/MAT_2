from sympy import *

init_printing(use_unicode=False)

x = Symbol("x")

function_ex1 = 3*(x**2)

print("A FUNCAO: ")

pprint(Integral(function_ex1, (x, 2, x)))

result_ex1 = integrate(function_ex1, (x, 2, x))


#printing result
print("PRIMITIVA EX1 : {}".format(result_ex1))
