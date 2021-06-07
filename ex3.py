from sympy import *


init_printing(use_unicode=False)

x, t, y, z = symbols("x t y z")

func1 = x-(x**2)

result_func1 = solve(func1)

#print(result_func1) should be [0, 1], getting the limits

showing_func1 = Integral(func1, (x, result_func1[0], result_func1[1]))
area_func1 = integrate(func1, (x, result_func1[0], result_func1[1])).doit()


print("PONTOS: {}, {}".format(result_func1[0], result_func1[1]))
pprint(showing_func1)

print("AREA: ")
print(area_func1)
