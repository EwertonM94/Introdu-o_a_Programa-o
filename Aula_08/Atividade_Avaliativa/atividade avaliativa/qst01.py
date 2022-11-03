#[FORBELLONE, 2022] Construa um algoritmo para calcular as raízes de uma equação do 2 
# grau (Ax² + Bx + C), sendo que os valores A, B, C são fornecidos pelo usuário. 
# (considere que a equação possui duas raizes reais).

import math


a = int(input("Digite o valor do coeficiente a: "))
b = int(input("Digite o valor do coeficiente b: "))
c = int(input("Digite o valor do coeficiente c: "))

# Delta = b^2 - 4ac
delta = b**2 - 4*a*c
print("O valor de delta é: ", delta)
# x = - b +- raiz(delta)/2a
x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
print("O valor de x1 é: ", x1)
print("O valor de x2 é: ", x2)
