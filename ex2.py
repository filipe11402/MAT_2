from sympy import *

init_printing(use_unicode=False)

x = Symbol("x")

function_ex1 = 3*(x**2)

print("A FUNCAO: ")

pprint(Derivative(function_ex1))

result_ex1 = diff(function_ex1)


#printing result
print("DERIVADA EX1 : {}".format(result_ex1))