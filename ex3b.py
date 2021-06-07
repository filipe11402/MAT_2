from sympy import *


init_printing(use_unicode=False)

x, t, y, z = symbols("x t y z")

func1_solved = Eq(x**3, x)
func1 = x**3 - x

result_func1 = solve(func1_solved)

# print(result_func1) result must be [-1, 0, 1]

showing_func1_a = Integral(func1, (x, result_func1[0], result_func1[1]))
area_func1_a = integrate(func1, (x, result_func1[0], result_func1[1])).doit()

showing_func1_b = Integral(func1, (x, result_func1[2], result_func1[1]))
area_func1_b = integrate(func1, (x, result_func1[2], result_func1[1])).doit()


print("PONTOS: {}, {}".format(result_func1[0], result_func1[1], result_func1[2]))
pprint(showing_func1_a)

print("AREA 1: ")
print(area_func1_a)

pprint(showing_func1_b)

print("AREA 2: ")
print(area_func1_b)


total_area = area_func1_a + area_func1_b
print("AREA TOTAL: {}".format(total_area))
