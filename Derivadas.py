from sympy import *
import numpy as np

x = Symbol('x')


print("Buenos dias, este programa permite calcular la derivada de una funcion cuadratica completa")

def validar(texto):
    while True:
        try:
            dato= int(input(texto))
            return dato
        except ValueError:
            print("Oops!  Inserta un número entero por favor...")

a = validar("Ingrese el valor cuadratico :")
aa= a*x**2
print("valor cuadratico:",aa)
ap = aa.diff(x)
print("Derivada del valor cuadratico:",ap)

b = validar("Ingrese el valor lineal :")
bb= b*x
print("valor cuadratico:",bb)
bp = bb.diff(x)
print("Derivada del valor lineal:",bp)

c = validar("Ingrese el valor de la constante :")
print("valor de constante:",c)
cp= c*0
print("Derivada del valor  constante:",cp)

print("La derivada de la funcion es: ",ap,"+",bp)