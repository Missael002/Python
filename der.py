from Sympy import *
import numpy as np

x = Symbol('x')
a = x**2
b = x
c = 4
print("valor cuadratico:",a)
ap = a.diff(x)
print("Derivada del valor cuadratico:",ap)

print("valor lineal:",b)
bp = b.diff(x)
print("Derivada del valor lineal:",bp)

print("valor de constante:",c)
cp= c*0
print("Derivada del valor lineal:",cp)

print("La derivada de la funcion es: ",ap,"+",bp)