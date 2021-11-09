print ("Bienvenido este programa permite ingresar cierta cantidad de numeros para generar numeros aleatorios")

import random
def ValidarNumero(TextoEnPantalla):
    while True:
        try:
            dato = int(input(TextoEnPantalla))
            return dato
        except ValueError:
            print("Tiene que ser numero intenta de nuevo...")
def listaAleatorios(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(1,1000))
    return lista

n = ValidarNumero("Ingrese cuantos numeros aleatorios desea obtener")

aleatorios = listaAleatorios(n)
print(aleatorios)

with open ("NumerosAleatorios.txt", "w") as f:
    f.write(str(aleatorios)) 
    f.close()

