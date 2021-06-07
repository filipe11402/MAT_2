import numpy as np
import matplotlib.pyplot as plt

a = int(input("Introduza o valor para a: "))
b = int(input("Introduza o valor para b: "))

f = lambda x : np.exp(x)
N = 50
n = 50 

h = (b-a) / n
x = np.linspace(a,b,N)

left_value = 0
mid_value = 0
right_value = 0

print("SOMA DE RIETMANN PARA N=10 de {} a {}".format(a, b))


for i in range(n-1):
    left_value += f(x[i]) * h

for i in range(n-1):
    mid_value += f(x[i+1]) * h

for i in range(n-1):
    right_value += f(((x[i]) + (x[i+1]))/2) * h


print("RESULTADO DA SOMA DE RIETMANN")
print("ESQUERDA: {:.3f}".format(left_value))
print("MEIO: {:.3f}".format(mid_value))
print("DIREITA: {:.3f}".format(right_value))
