from sympy import *
from ex1 import result_ex1

init_printing(use_unicode=False)


print("A FUNCAO: ")

pprint(Derivative(result_ex1))

result_ex1 = diff(result_ex1)


#printing result
print("DERIVADA EX1 : {}".format(result_ex1))